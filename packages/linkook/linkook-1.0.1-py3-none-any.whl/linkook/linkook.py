# linkook.py

import os
import sys
import argparse
from typing import Dict, Any
from collections import deque

import signal
import logging
from colorama import init as colorama_init

from linkook.scanner.site_scanner import SiteScanner
from linkook.outputer.result_writer import ResultWriter
from linkook.outputer.console_printer import ConsolePrinter
from linkook.outputer.visualize_output import Neo4jVisualizer
from linkook.provider.provider_manager import ProviderManager
from linkook.outputer.console_printer import CustomHelpFormatter


def setup_logging(debug: bool):
    """
    Set up logging configuration.

    :param debug: If True, set logging level to DEBUG; else disable logging.
    """
    if debug:
        level = logging.DEBUG
        logging.basicConfig(
            level=level,
            format="[%(asctime)s] %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    else:
        logging.disable(logging.CRITICAL)


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    :return: Parsed arguments namespace.
    """
    parser = argparse.ArgumentParser(
        usage=argparse.SUPPRESS, formatter_class=CustomHelpFormatter
    )
    parser.add_argument("username", help="Username to check across social networks.")
    parser.add_argument(
        "--concise", "-c", action="store_true", help="Print more concise results."
    )
    parser.add_argument(
        "--silent",
        "-s",
        action="store_true",
        help="Suppress all output and only show summary.",
    )
    parser.add_argument(
        "--show-summary",
        "-ss",
        action="store_true",
        help="Show a summary of the scan results.",
    )
    parser.add_argument(
        "--check-breach",
        "-cb",
        action="store_true",
        help="Check if the username has been involved in a data breach, using data from HudsonRock's Cybercrime Intelligence Database",
    )
    parser.add_argument(
        "--browse",
        "-b",
        action="store_true",
        dest="browse",
        default=False,
        help="Browse to all found profiles in the default browser.",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        dest="no_color",
        default=False,
        help="Don't color terminal output.",
    )
    parser.add_argument(
        "--neo4j",
        action="store_true",
        help="Export the results to a JSON file for Neo4j visualization.",
    )
    parser.add_argument(
        "--scan-all",
        "-a",
        action="store_true",
        help="Scan all available sites in the provider.json file. If not set, only scan sites with 'isConnected' set to true.",
    )
    parser.add_argument(
        "--print-all",
        action="store_true",
        dest="print_all",
        default=False,
        help="Output sites where the username was not found.",
    )
    parser.add_argument(
        "--debug",
        "-d",
        action="store_true",
        help="Enable verbose logging for debugging.",
    )
    parser.add_argument(
        "--output",
        "-o",
        nargs="?",
        metavar="PATH",
        const="results",
        help="Directory to save the results. Default is 'results'.",
    )
    parser.add_argument(
        "--local",
        "-l",
        nargs="?",
        metavar="PATH",
        const="provider.json",
        default="linkook/provider/provider.json",
        help="Force the use of the local provider.json file, add a custom path if needed. Default is 'provider.json'.",
    )
    return parser.parse_args()


def create_output_directory(output_dir: str):
    """
    Create the output directory if it doesn't exist.

    :param output_dir: Path to the output directory.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logging.info(f"Created output directory at: {output_dir}")
    else:
        logging.info(f"Using existing output directory at: {output_dir}")


def handler(signal_received, frame):
    """
    Handle graceful exit on receiving a SIGINT (Ctrl+C).

    :param signal_received: The signal number.
    :param frame: Current stack frame.
    """
    print("\nProcess interrupted. Exiting gracefully.")
    sys.exit(0)


def scan_queue(
    user: str,
    scanner: SiteScanner,
    console_printer: ConsolePrinter,
    args: argparse.Namespace,
) -> Dict[str, Any]:
    """
    scan queue handler function, execute global provider scan and return all discovered account information.

    :param user: The username to scan.
    :param scanner: The SiteScanner instance.
    :param console_printer: The ConsolePrinter instance.
    :param args: The parsed command-line arguments.
    """

    console_printer.start(user)

    queue = deque()
    for provider_name in scanner.to_scan.keys():
        queue.append((user, provider_name))

    results = {}
    counter = 0
    other_links_flag = False
    provider_count = len(scanner.to_scan.keys())

    while queue:

        if counter == provider_count:
            other_links_flag = True
            console_printer.start_other_links()
        counter += 1

        user, provider_name = queue.popleft()

        scanner.current_provider = scanner.all_providers.get(provider_name)

        if not scanner.current_provider:
            continue

        scan_result = scanner.deep_scan(user)

        # Notify results to console
        if not args.silent:
            console_printer.update(
                {
                    "site_name": provider_name,
                    "status": "FOUND" if scan_result["found"] else "NOT FOUND",
                    "profile_url": scan_result["profile_url"],
                    "other_links": scan_result.get("other_links", {}),
                    "other_links_flag": other_links_flag,
                    "infos": scan_result.get("infos", {}),
                }
            )

        results[provider_name] = scan_result

        other_links = scan_result.get("other_links", {})

        for provider_name, linked_urls in other_links.items():
            provider = scanner.all_providers.get(provider_name)
            if not provider:
                logging.debug(f"Provider {provider_name} not found")
                continue
            if not provider.is_connected:
                logging.debug(f"Provider {provider_name} has no connection")
                continue
            if not provider.keyword:
                logging.debug(f"Provider {provider_name} has no keywords configured")
                continue
            for linked_url in linked_urls:
                logging.debug(f"Checking {linked_url}")
                if linked_url in scanner.visited_urls:
                    continue
                new_user = provider.extract_user(linked_url).pop()
                if new_user != user:
                    logging.debug(f"Adding {linked_url} to queue")
                    queue.append((new_user, provider_name))
                else:
                    logging.debug(f"User {new_user} already in queue")

    return results


def main():
    """
    Main function to orchestrate the aggregation process.
    """
    args = parse_arguments()

    # Set up logging
    setup_logging(args.debug)

    # Initialize colorama for colored console output
    if not args.no_color:
        colorama_init(autoreset=True)
    else:
        colorama_init(strip=True, convert=False)

    if not args.local:
        force_local = False
    else:
        force_local = True

    # Handle Ctrl+C gracefully
    signal.signal(signal.SIGINT, handler)

    # Initialize ConsolePrinter
    console_printer = ConsolePrinter(
        debug=args.debug,
        print_all=args.print_all,
        silent=args.silent,
        concise=args.concise,
        browse=args.browse,
    )

    console_printer.banner()

    # Initialize ProviderManager
    manager = ProviderManager(
        remote_json_url="https://raw.githubusercontent.com/JackJuly/linkook/refs/heads/main/linkook/provider/provider.json",
        local_json_path=args.local,
        force_local=force_local,
        timeout=10,
    )

    try:
        manager.load_providers()
        logging.info(f"Loaded {len(manager.get_all_providers())} providers.")
    except Exception as e:
        logging.error(f"Failed to load providers: {e}")
        sys.exit(1)

    scanner = SiteScanner(timeout=10, proxy=None)
    scanner.all_providers = manager.get_all_providers()
    scanner.to_scan = manager.filter_providers(is_connected=not args.scan_all)
    scanner.check_breach = args.check_breach

    username = args.username
    results = scan_queue(username, scanner, console_printer, args)

    print_content = {
        "username": username,
        "found_accounts": scanner.found_accounts,
        "found_usernames": scanner.found_usernames,
        "found_emails": scanner.found_emails,
    }

    if args.silent:
        args.show_summary = True

    console_printer.finish_all(print_content, args.show_summary)

    if args.neo4j:
        visualizer = Neo4jVisualizer(results)
        visualizer.all_providers = manager.get_all_providers()
        visualizer.visualize(username=username, output_file="neo4j_export.json")

    # Write results to file
    result_writer = None
    if args.output is not None:
        output_name = args.output
        # Create output directory
        create_output_directory(output_name)

        # Initialize ResultWriter
        result_writer = ResultWriter(output_name)

    if result_writer is not None:
        result_writer.write_txt(username, results)

    if args.browse:
        console_printer.browse_results(results)


if __name__ == "__main__":
    main()
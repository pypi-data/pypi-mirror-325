import requests

def check_HudsonRock(email: str) -> bool:
        """
        Check if the user's data has been leaked in the Hudson Rock database.
        """
        url = f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email?email={email}"
        associated_string = "This email address is associated with a computer that was infected by an info-stealer, all the credentials saved on this computer are at risk of being accessed by cybercriminals. Visit https://www.hudsonrock.com/free-tools to discover additional free tools and Infostealers related data."
        not_associated_string = "This email address is not associated with a computer infected by an info-stealer. Visit https://www.hudsonrock.com/free-tools to discover additional free tools and Infostealers related data."
        res = requests.get(url)
        status_code = res.status_code
        json_content = res.json()
        if status_code is None:
            return False
        if status_code == 404:
            return False
        if status_code == 200:
            if json_content["message"] == associated_string:
                return True
            elif json_content["message"] == not_associated_string:
                 return False
        return False

email = "hello@gamil.com"
# email = "jdmayuan@gamil.com"

res = check_HudsonRock(email)

print(res)
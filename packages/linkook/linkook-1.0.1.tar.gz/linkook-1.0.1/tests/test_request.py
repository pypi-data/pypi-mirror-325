import requests
import re

headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0",
        }


# "links": ["GitLab", "GitHub", "Bugcrowd", "LinkedIn", "Cobalt", "X", "Hack The Box"]

def test_request_get(url: str) -> str:
    response = requests.get(url=url, headers=headers)
    print(response.status_code)
    # print(response.text)
    return response.text


url1 = 'https://api.github.com'

url2 = "https://api.github.com/users/JackJuly"

url11 = "https://github.com/JackJuly"


url5 = "https://linktr.ee/enumbr"

url6 = "https://allmylinks.com/stok"

url3 = "https://bugcrowd.com/priyanshuxodafsdfs"


url10 = "https://www.linkedin.com/in/yuan-ma-5b140827b"

url111 = "https://t.me/2piwKHNVbb6DMOiPY2efmG"


res = test_request_get(url111)

# html = "https://x.com/Jack"


regex_user = "https://(?:twitter|x)\.com/([^'<>\"]+)"

regex = "https://(?:twitter|x)\.com/[^'<>\"]+"

regex_pattern = "(?:(?!&quot;)[^<>()\[\]'?\"\\\\])+"

regexUrl = "https://open.spotify.com/(?:intl-[a-z]{2}/)?(?:artist|user)/[^'<>\"]+"

regex2 = "Performance"

email_regex = re.compile(r"^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$")



# result1 = re.compile(email_regex).findall(res)
print(res)
# print (result1)

# result2 = re.compile(regex_user).findall(html)

# unique_links1 = set(match.strip('"') for match in result1)
# unique_links2 = set(match.strip('"') for match in result2)

# print(unique_links1)
# print(unique_links2)




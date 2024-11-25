import requests

URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Leaked-Databases/000webhost.txt"

with open("data.csv", "w") as f:
    f.write("passwords\n")
    f.write(requests.get(URL).text)

# https://pypi.org/project/requests/
import requests

#url = "http://127.0.0.1/api/index.php?codigo=8"
url = "http://127.0.0.1/api/index2.php?codigo=8"
r = requests.get(url)

print(r.json())
import requests

url = "https://icanhazdadjoke.com/"

#res = requests.get(url, headers={"Accept": "text/plain"})
res = requests.get(url, headers={"Accept": "application/json"})
# print(res.text)
data = res.json()
print(data["joke"])

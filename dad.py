import requests

url = "https://icanhazdadjoke.com/search"

#res = requests.get(url, headers={"Accept": "text/plain"})
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
)
# print(res.text)
#data = res.json()
# print(data["joke"])
data = res.json()
print(data["results"])

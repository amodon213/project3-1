import requests

try:
    url = open("k8s_url.txt",'r').read().strip()
    url += "/users/1"
    print(url)
    res = requests.get({url})

    print(res.json())

except Exception as e:
    print(e)

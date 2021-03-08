import requests

try:
    f = open("k8s_url.txt", "r")
    url = f.read() + "/users/1"
    print(url)
    res = requests.get(f'{url}')

    print(res.json())

except Exception as e:
    print(e)

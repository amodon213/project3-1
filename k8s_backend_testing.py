import requests

try:
    url = open("k8s_url.txt",'r').read()
    url = url[:-1]
    url = f'{url}/users/1'
    print(url)
    res = requests.get({url})

    print(res.json())

except Exception as e:
    print(e)

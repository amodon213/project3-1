import requests

try:
    url = open("k8s_url.txt",'r').read()
    print(url)
    print(f'{url}/users/1')
    res = requests.get(f'{url}/users/1')

    print(res.json())

except Exception as e:
    print(e)

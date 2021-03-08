import requests

try:
    url = open("k8s_url.txt",'r').read().split('\n')
    print(url)
    res = requests.get(f'{url}/users/1')

    print(res.json())

except Exception as e:
    print(e)

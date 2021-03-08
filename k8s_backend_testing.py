import requests

try:
    url = open("k8s_url.txt",'r').read()[:-1]
    print(url)
    print(f'{url[0]}/users/1')
    res = requests.get(f'{url[0]}/users/1')

    print(res.json())

except Exception as e:
    print(e)

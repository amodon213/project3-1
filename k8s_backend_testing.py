import requests

try:
    url = open("k8s_url.txt",'r').read().split('\n')
    res = requests.get(f'{url[0]}/users/1')

    print(res.json())

except Exception as e:
    print(e)

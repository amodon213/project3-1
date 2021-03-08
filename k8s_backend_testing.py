import requests

try:
    url = open("k8s_url.txt",'r').read().split('\n') + "/users/1" 
    print(url)
    res = requests.get(f'{url}')

    print(res.json())

except Exception as e:
    print(e)

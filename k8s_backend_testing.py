import requests

try:
    url = open("k8s_url.txt",'r').read().strip()
    res = requests.get(f'{url}/users/1')

    print(res.json())
    res = requests.get('http://0.0.0.0:5000/users/1')
    print(res.json())
            
except Exception as e:
    print(e)

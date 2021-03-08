import requests

try:
    with open("k8s_url.txt", "r") as f:
        url = f.read()
        
    res = requests.get(f'{url}/users/1')

    print(res.json())
    
    res = requests.get('http://0.0.0.0:5000/users/1')

    print(res.json())
except Exception as e:
    print(e)

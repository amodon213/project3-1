import requests

try:
    url = open("k8s_url.txt",'r').read().strip()
    url +=  "/users/2"
    res = requests.get(url)

    print(res.json())
    res = requests.get('http://0.0.0.0:5000/users/1')
    print(res.json())
            
except Exception as e:
    print(e)

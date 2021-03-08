import requests


def get(id):
    try:
        res = requests.get(f"http://0.0.0.0:5000/users/{id}")
        print(res, res.text)
    except:
        print("Error")


def post(id, name):
    try:
        res = requests.post(f"http://0.0.0.0:5000/users/{id}", json={"name": f"{name}"})
        print(res, res.text)
    except:
        print("Error")


def put(id, name):
    try:
        res = requests.put(f"http://0.0.0.0:5000/users/{id}", json={"name": f"{name}"})
        print(res, res.text)
    except:
        print("Error")


def delete(id):
    try:
        res = requests.delete(f"http://0.0.0.0:5000/users/{id}")
        print(res, res.text)
    except:
        print("Error")


if __name__ == '__main__':
    try:
        post(3, "Posted user1")
        get(3)
        delete(3)
    except:
        print("Test failed")

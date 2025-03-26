import requests

def greet(name):
    print(f"hello {name}!!")

def fetchTextFromUrl(url: str) -> str:
    response = requests.get(url)

    print(response.text)

def getResponseStatusFromUrl(url: str) -> str:
    response = requests.get(url)
    print(response.status_code)

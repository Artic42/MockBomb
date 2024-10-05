import requests


def sendAliveMessage() -> None:
    try:
        url = "http://lsbapi.artic42.com/bomb/stillAlive"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except Exception as e:
        print(e)



def sendDefusedMessage() -> None:
    try:
        url = "http://lsbapi.artic42.com/bomb/disarm"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except Exception as e:
        print(e)


def sendExplodedMessage() -> None:
    try:
        url = "http://lsbapi.artic42.com/bomb/explode"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except Exception as e:
            print(e)


def sendArmedMessage() -> None:
    try:
        url = "http://lsbapi.artic42.com/bomb/arm"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        return response
    except Exception as e:
            print(e)

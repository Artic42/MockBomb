import requests


def sendAliveMessage() -> None:
    url = "http://lsbapi.artic42.com/bomb/stillAlive"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def sendDefusedMessage() -> None:
    url = "http://lsbapi.artic42.com/bomb/disarm"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def sendExplodedMessage() -> None:
    url = "http://lsbapi.artic42.com/bomb/explode"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def sendArmedMessage() -> None:
    url = "http://lsbapi.artic42.com/bomb/arm"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response

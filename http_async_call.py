import requests
import threading

url = "https://webhook.site/81c75d7d-f9c7-48f6-ab55-b59b5c410e02"

def sendRequest(requestUrl):
    r = requests.get(requestUrl)
    print(r.headers['Date'])


processThread1 = threading.Thread(target=sendRequest, args=(url,))
processThread2 = threading.Thread(target=sendRequest, args=(url,))
processThread3 = threading.Thread(target=sendRequest, args=(url,))
processThread1.start()
processThread2.start()
processThread3.start()
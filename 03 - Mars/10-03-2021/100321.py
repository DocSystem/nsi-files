import requests
import httplib2

url = "http://mathgreen.fr/"

def ex1():
    r = requests.get(url)
    print(r.text)

#ex1()

def ex2():
    h = httplib2.Http()
    (headers, content) = h.request(url, "GET")
    print(headers)
    print(content)

ex2()

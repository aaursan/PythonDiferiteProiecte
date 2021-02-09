#incercarea 2
import requests
import json

class WorkWithHTTP(object):
        def __init__(self, url):
            self.url = url
        def get_values(self,payload):
            self_dictionar=payload
            print(r.status_code)
            print(r.encoding)
        def post_value(self,headers):
            self_headers=headers
            print(r.text)
            print(r.content)
            print(r.json())
            print(r.headers['content-type'])

r = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.content)
# print(r.json())
payload = {'title':'foo', 'body':'bar', 'userId':'1'}
headers = {'content-type': 'application/json'}
r = requests.post('http://jsonplaceholder.typicode.com/posts', data=json.dumps(payload), headers=headers)
print(r.status_code)
print(r.text)
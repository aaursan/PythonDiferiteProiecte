import json
import requests

class WorkWithHttp():
    def __init__(self,url):
        self.url=url
    def download(self):
        r=requests.get(self.url + '/1/commments')
        print(r.status_code)
        print(r.json())
    def upload_data(self,payload):
        if not isinstance(payload,dict):
            raise TypeError('Ecpected dict, received:%s' %type(payload))
        header={'content=type':' application/json'}
        r=requests.post(self.url,headers=header,data=json.dumps(payload))
        print(r.status_code)
        print(r.headers)
h=WorkWithHttp("https://jsonplaceholder.typicode.com/posts")
print("Atributul clasei", h.url)
h.download()
payload={'key':10}
h.upload_data(payload)
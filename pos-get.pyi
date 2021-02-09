import json
import requests
r=requests.get("")
print("status code",r.status_code)
print("content",r.content)
print("text",r.text)
print("encoding", r.encoding)
print("json info",r.json)
payload={'title':'curs python','author'='telecom'}
header=
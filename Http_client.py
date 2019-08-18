import http.client
import json

conn = http.client.HTTPSConnection('www.httpbin.org')
conn.request("GET","/")
s1 = conn.getresponse()
x = s1.status,s1.reason
print(json.dumps(x))
data1 = s1.read()
conn.request("GET","/")
s1 = conn.getresponse()
print(s1.read())

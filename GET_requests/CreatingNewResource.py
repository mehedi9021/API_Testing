import requests
import json
import jsonpath

#API url
url = 'https://reqres.in/api/users'

#read input json file
file=open('C:\\Users\\User\\PycharmProjects\\API testing\\GET_requests\\info.json','r')
json_input = file.read()
request_json=json.loads(json_input)

print(request_json)

#make post request with json input body
response=requests.post(url, request_json)

print(response.content)

#validating response code
assert response.status_code==201

#fetch header from response
print(response.headers)

print(response.headers.get('Content-Length'))

#parse response to json format
response_json = json.loads(response.text)

#pick ID using json path
id=jsonpath.jsonpath(response_json,'id')
print(id[0])




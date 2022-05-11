import requests
import json
import jsonpath

#API url
url = 'https://reqres.in/api/users/2'

#read input json file
file=open('C:\\Users\\User\\PycharmProjects\\API testing\\GET_requests\\info1.json','r')
json_input = file.read()
request_json=json.loads(json_input)

print(request_json)

#make put request with json input body
response=requests.put(url, request_json)

print(response.content)

#validating response code
assert response.status_code==200

#parse response content
response_json=json.loads(response.text)
updated_li= jsonpath.jsonpath(response_json,'updatedAt')
print(updated_li[0])






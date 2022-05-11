import requests
import json
import jsonpath

#API url
url= 'https://reqres.in/api/users?page=2'

#get request
response = requests.get(url)

print(response)

#parse response to json format
json_response= json.loads(response.text)
print(json_response)

#fetch spectific value using json path

page = jsonpath.jsonpath(json_response, 'total_pages')
print(page)

assert page[0]==2
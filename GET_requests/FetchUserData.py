import requests

#API url
url= 'https://reqres.in/api/users?page=2'

#get request
response = requests.get(url)

print(response)

#display response content

print(response.content)

#get header response content

print(response.headers)



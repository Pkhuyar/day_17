import requests

#url = "https://jsonplaceholder.typicode.com/posts"



#resposnse = requests.get(url).json()

"""converted_dict = {}

for item in resposnse:
    key = item["id"]
    converted_dict[key] = item"""

#print(resposnse[0])

url = "https://jsonplaceholder.typicode.com/posts"

user_id = 1

response = requests.get(url, params={"userId": user_id}).json()

print(response)

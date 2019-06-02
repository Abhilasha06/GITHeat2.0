import requests
from PIL import Image
url='https://codeforces.com/api/user.info?handles='

#taking the codeforces handle as input
a=input()

abc=url+a
response = requests.get(abc)
json_response = response.json()
repository = json_response['result'][0]
name=f'{repository["firstName"]}'+" "+f'{repository["lastName"]}' 
print("Name: ",name)
print(f'Rank: {repository["rank"]}')  
print(f'Rating: {repository["rating"]}') 
print(f'City: {repository["city"]}') 
print(f'Country: {repository["country"]}') 
print(f'Organization: {repository["organization"]}')    
      

url=f'{repository["titlePhoto"]}'
url="http:"+url

#displaying the profile picture
im = Image.open(requests.get(url, stream=True).raw)
im.show()
      

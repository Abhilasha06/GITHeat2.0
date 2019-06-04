import requests
from PIL import Image
url='https://codeforces.com/api/user.info?handles='

#taking the codeforces handle as input
a=input()

abc=url+a
response = requests.get(abc)
json_response = response.json()
repository = json_response['result'][0]
try:
    name=f'{repository["firstName"]}'+" "+f'{repository["lastName"]}' 
    print("Name: ",name)
except:
    print("Name: Not available")
try:
    print(f'Rank: {repository["rank"]}') 
except:
    print("Rank: Not available")
try:
    print(f'Rating: {repository["rating"]}') 
except:
    print("Rating: Not available")
try:
    print(f'City: {repository["city"]}') 
except:
    print("City: Not available")
try:
    print(f'Country: {repository["country"]}') 
except:
    print("Country: Not available")
try:
    print(f'Organization: {repository["organization"]}')    
except:
    print("Organization: Not available")
      

url=f'{repository["titlePhoto"]}'
url="http:"+url

#displaying the profile picture
im = Image.open(requests.get(url, stream=True).raw)
im.show()
      

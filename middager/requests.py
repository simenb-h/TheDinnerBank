import requests
import json
import unicodedata
import re


token = '0fd35636dcmsh456f4676fdfddd9p17f0d0jsnec16eecfa825'
r = requests.get("https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random?number=1", headers = {'X-Mashape-Key':token, "Content-Type": "application/json"})

# with open("oppskrift.yaml","w") as config: 
#             config.write(str(r.text))

# c = r.json()

# print(c['recipes'][0]['title'])
# print('___________________________')
# print(c['recipes'][0]['instructions'])
# print(c['recipes'][0]['sourceUrl'])
# print('___________________________')


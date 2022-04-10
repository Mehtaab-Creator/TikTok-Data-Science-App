#importing the tiktok python SDK
from TikTokApi import TikTokApi as tiktok 
#for exporting data into a json format
import json

#setting up the instance
api = tiktok()

#creating an empty lists for data to append too
users = []
trending = []

#finding users with a specific name
for user in api.search.users("TheRock"):
    print(user.as_dict)
    users.append(user.as_dict)
    #exporting the list into a json file
    

#pulling out specific hashtag
for video in api.hashtag(name='funny').videos():
    print(video.as_dict)
    trending.append(video.as_dict)
 
    
with open('trending_export.json', 'w') as f:
        json.dump(trending, f)

with open('user_export.json', 'w') as f:
        json.dump(users, f)

#print(trending)
#print(users)
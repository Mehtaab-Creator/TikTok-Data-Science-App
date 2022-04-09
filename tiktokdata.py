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
    users.append(user)
    #exporting the list into a json file
    #with open('user_export.json', 'w') as f:
        #json.dump(users, f)

#pulling out trending video statistics
for trending_video in api.trending.videos():
    user_stats = trending_video.author.info_full['stats']
    trending.append(trending_video)
    #exporting the list into a json file
    #with open('stats_export.json', 'w') as f:
        #json.dump(trending, f)

with open('user_export.json', 'w') as f:
        json.dump(users, f)

print(trending)
print(users)
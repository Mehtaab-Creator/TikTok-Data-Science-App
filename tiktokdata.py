#importing the tiktok python SDK
from operator import index
from TikTokApi import TikTokApi as tiktok 
#for exporting data into a json format
import json
from urllib3 import proxy_from_url
#importing data cleaning process .py 
from helpers import process_results
#import pandas to create dataframe
import pandas as pd
#import sys to extract cmd line arguments
import sys


def get_data(hashtag):
    verifyFp = 'verify_l1unfse9_sgoech18_fWLJ_4iLb_98ks_N5jaXerVeWzW'
    #setting up the instance
    api = tiktok(custom_verify_fp=verifyFp)

    #creating an empty lists for data to append too
    trending = []

    #pulling out specific hashtag
    for video in api.hashtag(name=hashtag).videos():
        print(video.as_dict)
        trending.append(video.as_dict)

    flattened_data = process_results(trending)

    #covereted processed data dict into a dataframe and then into a csv
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('hashtag_data.csv',index=False)

if __name__ == '__main__':
    #sys.argv holds all the arguments when you run a python script
    get_data(sys.argv[1])
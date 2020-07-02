import requests
import pandas as pd
import json
from functools import reduce
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('PremierLeague')
collection = db.get_collection('Premier_Defence')
player_id_collection = db.get_collection('Player_id')
criteria = [
    'outfielder_block',
    'interception',
    'total_tackle',
    'last_man_tackle',
    'total_clearance',
    'head_clearance',
    'aerial_won',
    'own_goals',
    'error_lead_to_goal',
    'penalty_conceded',
    'fouls',
    'aerial_lost'
    ]
# for i in range(12):
#     url = f'https://footballapi.pulselive.com/football/stats/ranked/players/{criteria[i]}?page=0&pageSize=1000&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true'
#     headers = {
#         'authority': 'footballapi.pulselive.com',
#         'method': 'GET',
#         'path': f'/football/players?pageSize=0&compSeasons=274&altIds=true&page=1000&type=player&id=-1&compSeasonId=274',
#         'scheme': 'https',
#         'accept': '*/*',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
#         'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#         'origin': 'https://www.premierleague.com',
#         'referer': 'https://www.premierleague.com/stats/top/players/{criteria[i]}',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'cross-site',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
#         }
#     r = requests.get(url,headers = headers)
#     print(f'crawling {criteria[y]} done!')
#     data = json.loads(r.text)
#     collection.insert_one(data)
# ------------------------------------------------------------------------

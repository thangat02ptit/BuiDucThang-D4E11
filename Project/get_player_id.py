import requests
import pandas as pd
import json
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('PremierLeague')
player_id_collection = db.get_collection('Player_id')

url = 'https://footballapi.pulselive.com/football/stats/ranked/players/goals?page=0&pageSize=1000&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true'
headers = {
        'authority': 'footballapi.pulselive.com',
        'method': 'GET',
        'path': '/football/stats/ranked/players/goals?page=0&pageSize=20&compSeasons=274&comps=1&compCodeForActivePlayer=EN_PR&altIds=true',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.premierleague.com',
        'referer': 'https://www.premierleague.com/stats/top/players/goals?se=274',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/85.0.134 Chrome/79.0.3945.134 Safari/537.36'
        }
r = requests.get(url,headers = headers)
data = json.loads(r.text)
player_id_collection.insert_one(data)
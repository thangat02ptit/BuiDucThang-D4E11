import requests 
from pymongo import MongoClient
mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('Police Call')
# client = requests.get('https://data.baltimorecity.gov/resource/xviu-ezkt.json?')
# data = client.json()
# collection.insert_many(data)
# number = collection.count({
#     "priority" : "Non-Emergency"
# })
# total = collection.count({})
# print('percent of Non-Emergency: ', (number/total) * 100, '%')


# district = {}
# for key in collection.find({}):
#     if key['district'] in district:
#         district[key['district']]+=1
#     else:
#         district[key['district']]=1
# max_district = max(district, key=district.get)
# print(max_district,district[max_district])

# all_district = collection.distinct('district')
# count_call_by_district = {}
# for district in all_district:
#     count_call_by_district[district] = collection.count_documents({'district':district})
# print(count_call_by_district)
# all_district = collection.distinct('district')
arr = collection.aggregate([
   { '$match': { 'priority': "Non-Emergency" } },
   { '$group': { '_id': "$district", 'total': { '$sum': 1 } } }
]) 
for key in arr:
    print(key)
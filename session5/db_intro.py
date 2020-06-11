from pymongo import MongoClient

client = MongoClient()

db = client.get_database('d4e11')
collection = db.get_collection('members') #tao ra collection trong database
# collection.insert_one({
#     'name' : 'dat',
#     'age': 24,
#     'gender':True
# })
# collection.insert_many([
# {
#     'name' : 'dat',
#     'age': 24,
#     'gender':True
# },
# {
#     'name' : 'dat',
#     'age': 24,
#     'gender':True
# },
# {
#     'name' : 'dat',
#     'age': 24,
#     'gender':True
# },
# ])
members = collection.find()
for member in members:
    print(member)

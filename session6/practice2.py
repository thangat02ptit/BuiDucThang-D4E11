import requests 
from pymongo import *
mongo_client = MongoClient()
db = mongo_client.get_database('d4e11')
collection = db.get_collection('movies3')

data = [
    {
    'title' : 'Fight Club',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
    ]
    },
    {
    'title' : 'Pulp Fiction',
    'writer' : 'Quentin Tarantino',
    'year' : 1994,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
    ]
    },
    {
    'title' : 'Inglorious Basterds',
    'writer' : 'Chuck Palahniuk',
    'year' : 2009,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
    ]
    },
    {
    'title' : 'The Hobbit: An Unexpected Journey',
    'writer' : 'Chuck Palahniuk',
    'year' : 2012,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
    ]
    },
    {
    'title' : 'The Hobbit: The Desolation of Smaug',
    'writer' : 'Chuck Palahniuk',
    'year' : 2013,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
    ]
    },
    {
    'title' : 'The Hobbit: The Battle of the Five Armies',
    'writer' : 'Chuck Palahniuk',
    'year' : 2012,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
    ]
    },
    {
    'title' : "Pee Wee Herman's Big Adventure",
    },
    {
    'title' : 'Avatar',
    },
]
# for i in data:
#     collection.insert_one(i)
# doc = collection.find({
#     '$or':
#         [
#             {'year':{'$lt':2000}},
#             {'year':{'$gt':2010}}
#         ]
#         })
# for i in doc:
#     print(i['title'],i['year'])

#update1
query = {'title' : 'The Hobbit: An Unexpected Journey'}
update = {
    '$set':{
        'synopsis' : "A reluctant hobbit, Bilbo Baggins, sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."
    }
}
collection.update_one(query,update)

#update2
query = {'title' : 'The Hobbit: The Desolation of Smaug'}
update = {
    '$set':{
        'synopsis' : "The dwarves, along with Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins is in possession of a mysterious and magical ring."
    }
}
collection.update_one(query,update)
#update 3
# query = {'title' : 'Pulp Fiction'}
# update = {
#     '$push':{
#         'actors' :'Samuel L. Jackson' 
#     }
# }
# collection.update_one(query,update)
a = collection.find({'synopsis': {'$regex': '.*Bilbo'}})
for i in a:
    print(i['title'])
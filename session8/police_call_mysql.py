import pymysql
from pymongo import *
mongo_client = MongoClient()
db = mongo_client.get_database('mysql_ex')
collection = db.get_collection('pollice_call')
mysql_client = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'thangcoma123',
    cursorclass = pymysql.cursors.DictCursor # khi lay du lieu ra thi se luu duoi dang dictionary
)
cursor = mysql_client.cursor()
# cursor.execute('''
#     CREATE TABLE police_call.police_call(
#         _id VARCHAR(255) PRIMARY KEY,
#         recordid VARCHAR(255),
#         callnumber VARCHAR(255),
#         calldatetime VARCHAR(255),
#         priority VARCHAR(255),
#         district VARCHAR(255),
#         description VARCHAR(255),
#         incidentlocation VARCHAR(255),
#         zipcode VARCHAR(255),
#         neighborhood VARCHAR(255),
#         policedistrict VARCHAR(255),
#         policepost VARCHAR(255),
#         councildistrict VARCHAR(255),
#         sheriffdistricts VARCHAR(255),
#         community_statistical_areas VARCHAR(255),
#         census_tracts VARCHAR(255),
#         vrizones VARCHAR(255)
#     )
# ''')
data_police_call = collection.find()
key = '_id,recordid,callnumber,calldatetime,priority,district,description,incidentlocation,zipcode,neighborhood,policedistrict,policepost,councildistrict,sheriffdistricts,community_statistical_areas,census_tracts,vrizones'
key_arr = key.split(',')
for data in data_police_call:
        data_id = str(data['_id'])
        cursor.execute(f'''
                INSERT INTO police_call.police_call(
                _id,
                recordid,
                callnumber,
                calldatetime,
                priority,
                district,
                description,
                incidentlocation,
                zipcode,
                neighborhood,
                policedistrict,
                policepost,
                councildistrict,
                sheriffdistricts,
                community_statistical_areas,
                census_tracts,
                vrizones 
            )
            VALUES(
                "{data_id}",
                "{data[ 'recordid']}",
                "{data[ 'callnumber']}",
                "{data[ 'calldatetime']}",
                "{data[ 'priority']}",
                "{data[ 'district']}",
                "{data[ 'description']}",
                "{data[ 'incidentlocation']}",
                "{data[ 'zipcode']}",
                "{data[ 'neighborhood']}",
                "{data[ 'policedistrict']}",
                "{data[ 'policepost']}",
                "{data[ 'councildistrict']}",
                "{data[ 'sheriffdistricts']}",
                "{data[ 'community_statistical_areas']}",
                "{data[ 'census_tracts']}",
                "{data['vrizones']}"
                )
            ''')
mysql_client.commit()

        
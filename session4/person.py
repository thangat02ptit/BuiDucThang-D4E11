person = ['dat',96,'Viettel',1,False,True]

#dictionary, object, map,....
person = {
    'name': 'dat', 
    'yob': {
        'year': 1996,
        'month': 7,
        'day': 22,
    }, 
    'company': ['Viettel','Vinaphone'],
    'key': None
}
# read


#create
person['relationship'] = True



#update
person['yob']['month'] = 4
#delete
del person['key']
for key in person:
   print(key,person[key])

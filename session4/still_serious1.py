inventory = {
'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
#1
inventory['pocket'] = ['seashell','strange berry','lint']
#2
inventory['backpack'].remove('dagger')
#3
a = str(inventory['gold']).split()
a.append('50')
inventory['gold'] = a
for i in range (len(inventory['gold'])):
    inventory['gold'][i] = int(inventory['gold'][i])
print(inventory['gold'])

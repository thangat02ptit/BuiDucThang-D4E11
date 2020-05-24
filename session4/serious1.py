name = input('your full name: ')
name = name.lower()
arr_name = name.split(' ')
print(arr_name)
for i in arr_name:
    if i != '':
        print(i.capitalize(), end = ' ')
dictionary = {
    'k':'khong',
    'any': 'anh yeu',
    'eny': 'em yeu',
    'vk': 'vo',
    'ck': 'chong',
    'ik': 'di',
    'mk': 'minh',
}
while True:
    print("***************")
    for i in dictionary:
        print(i, end = ' ')
    print('\n')
    key = input("your code? ")
    if key in dictionary.keys():
        print(dictionary[key])
    else:
        choice = input('not found, contribute? (Y/N): ')
        if (choice == 'Y' or choice == 'y'):
            new_value = input('enter your trans: ')
            dictionary[key] = new_value

    print('\n')

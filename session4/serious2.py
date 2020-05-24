bal = input("enter your balance: ")
while bal[0] == '0' and len(bal) > 1:
    bal = bal.replace('0','')
newbal = ''
while len(bal) >= 4:
    newbal = ',' + bal[len(bal)-3 : len(bal)] + newbal
    bal = bal[:len(bal)-3]
print('$',bal, end = '')
print(newbal)
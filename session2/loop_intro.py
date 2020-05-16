# n = int(input("enter your number:"))
# total = 0
# for i in range(n+1):
#     total += i
# print("total = ",total)
from getpass import getpass
username = 'mindx'
password = 'password'
check = False
while (check == False):
    enterun= input("username:")
    enterpw = getpass()
    if (enterun ==  username) and (enterpw == password):
        print("very true, here we go")
        check = True
    else:
        print("Pw or un is incorrect, please try again")

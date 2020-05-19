from getpass import getpass
from random import*
text = getpass("enter your quizz: ")
text_quiz = text.split() #tim dau ',' de chia va cho vao list
arr = list(text)
shuffle(arr)
for i in arr:
    print(i,end = ' ')
print("\n",end = '')
guess = input("guess the text: ")
if (text == guess):
    print("Congrat!")
else:
    print("Wrong!")
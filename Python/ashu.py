import time

print("hello how are you \'fslkds\' and where are you from", end=" , ")
print("And what do you want")
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
a = int(time.strftime('%H'))

if(a < 12 ):
    print("Good Morning ")
elif(a >= 12 and a < 20):
    print("Good Afternoon")
else:
    print("Good Night")

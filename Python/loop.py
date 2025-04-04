for i in range(1, 23, 2):
    print(i, end=", ")

name = (1,2,3,4,5)
print(type(name))
for i in name:
    print(i) 

i = int(input('Enter a interger value'))
while(i > 0):
    print(i, end="\t")
    break
i +=1


# do while loop

i = 0;
while True:
    print(i)
    i += 1
    if i % 100 == 0:
        break
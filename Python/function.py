# a = 10
# b = 9

# def Gmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def hello (a,b):
#     pass

# def isGreater(a,b):
#     if a > b:
#         print("First value is greater than second value")
#     else:
#         print("Second value is greater than first value")

# Gmean(a,b)
# isGreater(a,b)


# Arguments
def average(a= 10,b = 6):
    print("The averge is", (a+b)/2)

print(__name__)
if __name__ == "__main__":
    average()

def average1(*num):
    # print(type(num))
    sum = 0
    for i in num:
        sum += i 
    # print("Average of two number is ", sum / len(num))
    return sum / len(num)

a = average1(1,2,3,4)
print(a)



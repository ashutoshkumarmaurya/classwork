# # Recursion means use a function in that function 
# # ek function ko usi function me call karna (call itself)

# # Calculate factorial---
# def factorial(n):
#     if (n ==0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))    
# print(factorial(5))    
# print(factorial(6))    


# fibonacci series--
 
def fibonacci(n):
    # this is for generate the fibonacci series--
    n1 = 0
    n2 = 1
    count = 0
    if(n == 0):
        return n1
    elif(n == 1):
        return n2
    else:
        while count < n:
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
    
    # below logic calculate fibonacci for a particular value  using Recursion----

    # if(n == 0):
    #     return 0
    # elif(n == 1):
    #     return 1
    # else:
    #     return fibonacci(n-1)+fibonacci(n-2)



n = int(input("Enter a value "))
print(fibonacci(n))
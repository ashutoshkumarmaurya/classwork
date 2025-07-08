# def func1():
#     a = input("Enter a number")

#     try:
#         for i in range(1,11):
#             print(f"{a} X {i} = {int(a) * i}")
#             return 1
#     except Exception as e:
#         # print("You are entered wrong no.")
#         print(e)
#         return 0

#     # finally:
#     #     print("Always this executed")
#     print("Alright")

# x = func1()
# print(x)












# a = input("Enter a value")
# for i in a:
#     print(i)
# else:
#     print("no a right value")




# raising error in program ----
 
a = input("Enter a value between 0 to 10 \t")
if (a == "quite"):
    print(a)
elif (int(a) < 0 or int(a) > 10 ):
    raise ValueError("You are enter out of range ")
else:
    print(int(a))
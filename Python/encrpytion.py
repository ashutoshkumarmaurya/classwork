# import random
# import string


# # random_chars = ''.join(random.choices(string.ascii_letters, k=3))

# # print(random_chars)

# # print(dir(random))
# st = input("Enter a message")
# words = st.split(" ")
# coding = input("Enter 1 of encoding or 0 for decoding")
# coding = True if coding == "1" else False
# if(coding):
#     nword = []
#     for word in words:
#         if(len(word)>= 3):
#             r1 = ''.join(random.sample(string.ascii_letters, k=3))
#             r2 = ''.join(random.sample(string.ascii_letters, k=3))
#             stnew = r1+ word[1:] + word[0] + r2
#             nword.append(stnew)
#         else:
#             nword.append(word[::-1])
#     print(" ".join(nword))
# else:
#     nword = []
#     for word in words:
#         if(len(word)>= 3):
#             stnew =  word[3:-3]
#             stnew = stnew[-1] + stnew[:-1]
#             nword.append(stnew)
#         else:
#              nword.append(word[::-1])
#     print(" ".join(nword))





print(23*4)


# alphabet_dict = {chr(i): i - 64 for i in range(65, 91)}
# print(alphabet_dict)


alphabet_dict = {}
for i in range(26):
    alphabet_dict[chr(65 + i)] = i + 1

print(alphabet_dict)
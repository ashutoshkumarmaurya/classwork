# List   (list  is ordered and changeble)----

# a = [1,2,54,7,8,99,88,7]
# b = a.copy()
# print(b)
# a.reverse()

# a.sort(reverse= True)
# # a.extend(b

# c = a + b
# a.append(100)
# print(a,len(a))
# print(c)

# list = [i for i in range(5)]
# print(list)
# if 4 in list:
#     print("4 present in list")

# list = [i for i in range(5) if i % 2 == 0]
# print(list)


# Tuple  (tuple is ordered and unchangeble)----

# a = (1,322,4,4,56,534,3)
# print(a, type(a))




# Set (set is unordered and unchangeble)---



# a = {3,34,5,54,4,4,5,332}
# print(len(a))
# print(type(a), a)


# b = {} # when create a set using blank curly bracket then it is a dict..
# print(type(b))

# c =set()
# print(type(c))

# methods or opreations in sets---
# a3 = 56
# a1 = {2,3,545,3,32}
# a2 = {56,56,656,544,4546}
# print(a1.add(a3),a1,a3)
# print(a2.union(a1))
# print(a2.update(a1),a2)

# print(a2.intersection(a1))
# print(a2.intersection_update(a1),a2)

# print(a1.symmetric_difference(a2))
# print(a1.isdisjoint(a2))

city = {"haryana", "delhi","noida", "faridabad", "sonipath","goa"}
city1 = {"haryana", "faridabad","goa"}
city2 = {"allahabad","paratabgarh","civilines","delhi"}

# print(city1.issubset(city))
# print(city1.issuperset(city))
# print(city.issuperset(city1))

# '''remove and discard both are delete a value in the set 
#    but the difference is remove through error when value is not in set 
#    and discard is not give error'''
# print(city.remove("noidaa"))
# print(city.discard("noidaa"))
# a = city.pop()
# print(city)
# print(a)

# DEL is used for delete entire set
# del city2
# print(city2)

# clear() is used for delete all value from the set
# city2.clear()
# print(city2)



# dict is ordered and key value pair ----

# rank = {
#     1 : "Ashutosh",
#     2 : "ram",
#     3 : "shyam"
# }
# print(rank)
# print(rank[1])  #this is use for access the value using key and when key are not valid it show error
# print(rank.get(4))  #this is use for access the value using key and when key are not valid it don't  show error

# print(rank.keys())
# print(rank.values())

# for key in  rank.keys():
#     print(f" The value corresponding to the key {key} is {rank[key]}")

# print(rank.items())
# for key , value in rank.items():
#     print(f" The value corresponding to the key {key} is {value}")

ep1 = {12:21,334:23,334343:6767,98:656}
ep2 = {34:43,67:87,654:989,5665:676}

# print(ep1.update(ep2))
print(ep1)
ep1.popitem()        #   it delete the last key and value in dict
ep1.pop(12)
print(ep1)  
#  it's use in previous time---
info = "My name is {} and I am from {}"
name = "Ashutosh"
address = "Prayagraj"
# print(info.format(name , address))

#  latest we use "f-string"---
print(f"My name is {name} and I am from {address}")

price = 420.44434
txt = f"take only two place in decimal {price:.3f}"
print(txt)

# Want to print using bracket--
print(f"My name is {{name}} and I am from {address}")

print(f"{5*5*5}")

# Implementing  KBC type  question and answer and along with their prize money

questions = [
    ["Who is King of fruits ? ", "Apple", "None", "Pineapple", "Mango",4],
    ["Who is King of forest ? ", "Tiger", "FOx", "Elephant", "Lion",4],
    ["Who is National animal of our nation ? ", "FOx", "Elephant", "Lion", "Tiger",4],
    ["Who is father of nation ? ", "PM", "CM", "DM", "President",4],
    ["Who is King of fruits ? ", "Apple", "None", "Pineapple", "Mango",4],
    ["Who is King of forest ? ", "Tiger", "FOx", "Elephant", "Lion",4],
    ["Who is National animal of our nation ? ", "FOx", "Elephant", "Lion", "Tiger",4],
    ["Who is father of nation ? ", "PM", "CM", "DM", "President",4],
    ["Who is King of fruits ? ", "Apple", "None", "Pineapple", "Mango",4],
    ["Who is King of forest ? ", "Tiger", "FOx", "Elephant", "Lion",4],
    ["Who is National animal of our nation ? ", "FOx", "Elephant", "Lion", "Tiger",4],
    ["Who is father of nation ? ", "PM", "CM", "DM", "President",4]
]

levels = [1000,2000,5000,10000,20000,50000,100000,1000000,5000000,10000000]
money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]} and the question is \n {question[0]}")
    print(f"a.  {question[1]}                 b. {question[2]}")
    print(f"c.  {question[3]}                 d. {question[4]}")

    reply = int(input("Enter your answer (1 - 4) or 0 to quit"))
    if (reply == 0 ):
        print("You are choose for quit so ")
        if (i == 0):
            money = 0
            break
        money = levels[i-1 ]
        break

    elif (reply == question[-1]):
        print(f"Correct answer, you won Rs.{levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 32000
        elif (i == 9):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money }")

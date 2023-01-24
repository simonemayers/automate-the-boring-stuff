# spam = 0
# while spam < 5:
#     print("Hello World!")
#     spam = spam + 1

# name = ""
# while name != "your name":
#     print("please type you name")
#     name = input()
# print("Thank you!")

spam = 0
while spam < 5:
    spam = spam +1
    if spam == 3:
        continue
    print("spam is " + str(spam))

name = "Bob"
if name == "Alice":
    print("Hi Alice")
print("Done")

password = "fisfh"
if password == "fish":
    print("access granted")
else:
    print("wrong password")

name = "Bob"
age = 3000
if name == "Alice":
    print("hi allice")
elif age < 12:
    print("you are not alice, kiddo.")
elif age > 2000:
    print("old")


print("Enter a name.")
name = input()
if name:
    print("thank you for entering you name")
else:
    print("you did not enter a name")

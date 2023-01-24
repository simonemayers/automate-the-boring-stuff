def hello():
    print("Howdy")
    print("Howdy!!!")
    print("Hello there.")

hello()

def hello(name):
    print("hello " + name)

hello("alice")
hello("bob")

def plusOne(number):
    return number + 1

newNumber = plusOne(5)
print(newNumber)

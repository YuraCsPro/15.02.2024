import random
def main():
    a=input("Enter first Number")
    b = input("Enter first Number")
    total=add(a,b)
    print(total)

def add(a,b):
    from random import choice
    number = random.randint(1,4)
    if number == 1:
        return int(a) + int(b)
    if number == 2:
        return int(a) - int(b)
    if number == 3:
        return int(a) / int(b)
    if number == 4:
        return int(a) / int(b)
main()


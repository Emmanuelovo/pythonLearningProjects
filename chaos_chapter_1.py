# chaos.py
# This is a function to illustrate the behaviours of random numbers
def main():
    print("This is a program to illustrate the chaotic behaviour of numbers")
    x = eval(input("Enter a number from 0 to 1:"))
    y = eval(input("Enter a number from 0 to 1:"))

    n = eval(input("How many values do want me to print?:"))

    for i in range(n):
        x = 2.0 * x *(1 - x)
        y = 2.0 * x *(1 - x)
        print(x,  y)

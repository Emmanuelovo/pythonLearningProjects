#this program calculates the future value of investment into the future 10 years

def main():
    # Title of prpogram
    print("This program calculates future value of investment")
    print("10 years into the future")

    # Getting inputs
    principal = eval(input("Enter the initial deposit: "))
    apr = eval(input("Enter the ineterest rate in decimal: "))
    invst_period = eval(input("How many years do you want this investment for: "))

    # Processing the inputs
    for i in range(invst_period):
        principal = principal * (1 + apr)

    # Producing the output
    # Notice That I am using the multiple format specifiers in the print out statement
    # this is because the curly braces '{}' help me specify multiple variables inside
    # this the print state,ent
    # and as you know python interpetes from left to right like C, so
    # all the corresponding values get replaced in the order that you specify
    print('The Return after {} years is: {} '.format(invst_period, principal))

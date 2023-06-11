#this program calculates the future value of investment into the future 10 years

def main():
    # Title of prpogram
    print("This program calculates future value of investment")
    print("10 years into the future")

    # Getting inputs
    principal = eval(input("How much are you investing?: "))
    apr = eval(input("What's the annual R.O.I?: "))
    year = eval(input("How many years is this investment for?: "))
    total = 0
    result = 0
    
    # Processing the inputs
    principal = principal * (1 + apr)
    result = year * principal
    print("Total at the end of {} years is: {}".format(year, result))
        
""""
    COMMENT SECTION
        principal = principal * (1 + apr)
        result = principal
        total += result

        get first year,
        compute it
        add it to result

        get 2nd year,
        compute it,
        add it to result

        
        
    # result += principal
    # Producing the output
    # Notice That I am using the multiple format specifiers in the print out statement
    # this is because the curly braces '{}' help me specify multiple variables inside
    # this the print state,ent
    # and as you know python interpetes from left to right like C, so
    # all the corresponding values get replaced in the order that you specify
    print('The Return after {} years is: {} '.format(invst_period, result))
    print('The sum of {} years is: '.format(invst_period,total))
"""

#this program calculates the future value of investment into the future 10 years

def main():
    # Title of prpogram
    print("This program calculates future value of investment")
    print("10 years into the future")

    # Getting inputs
    principal = eval(input("How much are you investing?: "))
    yearly_rate = eval(input("What's the annual rate?: "))
    quarterly_period = eval(input("How many times in a year is the rate compounded?: "))
    r_p = yearly_rate/quarterly_period
    result = 0
    
    # Processing the inputs
    for i in range(10):
        principal = principal * (r_p / 100)
        
    print("Total accrued result after 10 years is: {}".format(principal))
        
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

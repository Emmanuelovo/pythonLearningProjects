# This program converts the weather from celcius to fahrenheit
# Key points
# 0 degree Celcius = 32 degree fahrenheit (Freezing)
# 100 degree Celcius = 212 degree fahrenheit (Boiling)

#       EXTRA FUNCTIONALITIES THAT MY PROGRAM CAN DO
# if fahrenheit is less 53, cold
    # print ("wear thick clothes that will keep you warm")
# if fahrenheit is greater than 53 but less 104, warm
    # print("wear mild clothes, with cool colors")
# if fahrenheit is greater than 104 but less than 212!, Boiling hot
    # print("wear very light clothes, get Air conditional")

# I placed the assignment of celcius outside the for loop so that:
# 1. it acts as the first index position.
# 2. it will count as the 5th iteration in the loop.
# 3. once the 5 iterations are executed, the loop ends.

# Hence for every Iteration of the loop, the user provides an input.
# I used 'celcius' as assignment variable, in the 'celcius = 9/5 * celcius + 32'
# (instead of 'fahrenheit') so that the loop can repeat itself

def main():
    print("This program is designed to convert the Temperature reading")
    print("Type Celcius reading in increament of 10 degrees")
    print("Starting from 0 degrees to 100 degrees,")
    print("Once the Loop starts")
    
    
    celcius = eval(input("What is the CELCIUS temperature?: "))

    for i in range(10):
        celcius = 9/5 * celcius + 32
        print("The Fahrenheit temperature is: ", celcius)
        celcius = eval(input("What is the CELCIUS temperature?: "))
        
  
#       if celcius <= 52:        
#           print("Weather in Fahrenheit is: ", celcius)
#           print("Wear Thick clothes as the Weather is cold")
#       elif celcius > 52 and celcius <= 100:
#           print("Weather in fahrenheit is: ", celcius)
#           print("Wear mild clothes, the weather is not too cold")
#       elif celcius > 101 and celcius <= 212:
#           print("The Weather is very HOT!")
#           print("Please get an Air Conditional FAST!")

input("press <Enter> key to quit")

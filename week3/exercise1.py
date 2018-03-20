# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""




def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from just using range()
    """
    returnList = [] #Only works with For loop

    for i in range(start, stop, step):
        returnList.append(i)
    return returnList 

    returnList = []

    start += step
     
    while start < stop:
        returnList.append(start)
        start += step

    return(start, returnList)


    

def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """
    rangelist = []
    while start < stop:
        rangelist.append(start)
        start += step
    return rangelist


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    rangeList = []
    while start < stop:
        rangeList.append(start)
        start += 2
    return(rangeList)



def gene_krupa_range(start, stop, even_step, odd_step):
    """Make a range that has two step sizes.
    start=1,stop=20,even_step=3,odd_step=6

    [1,7,10,16,19] (1st elemnt, 2nd element...) 

    [1,4,10,13,19] (0th element,1stelem....)

    make a list that instead of having evenly spaced steps
    has odd steps be one size and even steps be another.
    """
    rangeList = []
    

    i = 0

    while start < stop:
        if i == 0:
            rangeList.append(start)
            start += odd_step
            i = 1
        else:
            rangeList.append(start)
            start += even_step
            i = 0
        
    return(rangeList)



def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK
    """
    number = int(input("Enter a number between " + str(low) + " and " + str(high) + ": "))

    while number <= int(low) or number >= int(high):
        
        number = int(input("Invalid. Enter a number between " + str(low) + " and " + str(high) + ": "))
    print('OK')
    return(number) 
    
    


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number (e.g. "cow",
    "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            input_number = int(input(message))
            print("Thanks! {} looks good.".format(input_number))
            return input_number
        except Exception as x:
            print("Try again ({})".format(x))



def super_asker(low, high):
    """Robust asking function.

    Combine stubborn_asker and not_number_rejector to make a function
    that does it all!
    """
    response = input("Enter a number between " + str(low) + " and " + str(high) + ": ")

    while response.isdigit() == False:

        print("Invalid. Not a number")

        response = input("Invalid. Enter a number between " + str(low) + " and " + str(high) + ": ")

    response = int(response)

    while response <= low or response >= high:
        
        response = input("Invalid. Enter a number between " + str(low) + " and " + str(high) + ": ")

        while response.isdigit() == False:
            
            print("Invalid. Not a number")
            
            response = input("Invalid. Enter a number between " + str(low) + " and " + str(high) + ": ")
            
        response = int(response)

    print("Ok")
    return(response)


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from
    

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\ngene_krupa_range", gene_krupa_range(1, 20, 2, 5))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a nunber: ")
    print("\nsuper_asker")
    super_asker(33, 42)

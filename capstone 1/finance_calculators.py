import math
import sys

# print welcome message
print("Choose either 'investment' or 'bond' from the menu below to proceed\n\
    \ninvestment\t- to calculate the amount of interest you will earn on your investment\
    \nbond      \t- to calculate the amount you will have to pay on a home loan")

# register user´s choice
user_choice = (input("Write either 'investment' or 'bond' and hit enter to proceed:\n")).lower()

# handle exceptions
if user_choice != 'investment' and user_choice != 'bond':
    print("ERROR: Your input is not recognised. please start again.")
    sys.exit()

# Use case 1: investment-------------------------------------------------
if user_choice == "investment":

    # user inputs cash amount
    deposit = float(input("Please input the amount of money you would deposit:\n"))

    # user inputs interest rate
    rate = float(input("Please input the interest % you choose:\n"))

    # user inputs amount of years for the plan as an int
    years = int(input("Please input the amount of years for your plan:\n"))

    interest = input("Now please enter:\n\
        'simple'   - if you want simple interest\n\
        'compound' - if you want a compound interest:\n").lower()

    # case simple
    if interest == 'simple':
        # calculate payback
        payback = deposit * (1 + (rate/100 * years))
    
    # case compound
    elif interest == 'compound':
        # calculate payback
        payback = deposit * (math.pow((1 + rate/100), years))
    
        # case string not recognised
    else:
        print("Your interest rate is not recognised, please start again")
        sys.exit()

    # print resutls for invvestmeent operations:
    print(f"You chose an {user_choice} with {interest} interest.\n\
        If you deposit R{deposit} for {years} years at a {rate} interest rate you will get R{round(payback,2)} back at the end of the contract.")

    

# Use case 2: bond-------------------------------------------------

else:
    # user inputs present value of the house
    house_value = float(input("Please enter the current value fo the property (R):\n"))

    # user inputs the interest 
    interest_rate = float(input("Please enter the interest rate (%) you desire:\n"))

    # user inputs number of months they plan to take to repay the bond
    months = int(input("Please enter the number of months for the bond:\n"))

    # Calculate how much money the user will have to repay each month and output the answer
    monthly_pay = (interest_rate / 100 / 12 * house_value) / (1 - math.pow((1 + interest_rate / 100 / 12),-months))

    # print outcome of the operation
    print(f"Resume for your bond:\n\
        For a house value of R{house_value}, an interest rate of {interest_rate}%, and a timeframe of {months} months:\n\
        You will need to pay R{round(monthly_pay,2)} per month")


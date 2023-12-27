import math

menu = '''
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan'''
print(menu)
# user should choose between investment or bond calculator
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
print(choice)

if choice == "investment":
    # p is the amount one is depositing
    p = float(input('please enter the amount you would like to deposit: '))
    # r is the interest rate
    r = float(input('please enter the rate excluding the % symbol: '))/100
    # t is the number of years
    t = int(input("please enter the number of investment years: "))
# user should choose between simple and compound interest if their choice was investment calculator
    interest = input('please enter either compound or simple interest: ').lower()
    if interest == 'simple':
        simple = p *(1 + r*t)
        print(simple)

    elif interest == 'compound':
        compound = p * math.pow((1+r),t)
        print(compound)

    else:
        print("invalid input")

elif choice == 'bond':
    # p is the present value of the house
    p = int(input('please enter the present value of the house: '))
    # i is the monthly interest rate
    i = float(input('please enter the interest rate excluding the % symbol: '))/100
    i = i/12
    # n is the number of months
    n = int(input('please enter the amount of months it will take to repay: '))

    MonthlyPay = (i * p)/(1 -(1+i)**(-n))
    print(MonthlyPay)

else:
    print('invalid choice')
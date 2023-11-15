#Name: Edward Watson & Joey Lindgren
#Program Purpose: This program finds the cost of movie tickets
# Price for small pizza: $9.99
# Price for medium pizza: $12.99
# Price for large pizza: $17.99
# Price for extra large pizza: $21.99
# Price for drink: $3.99
# Price for breadsticks: $6.99
# Sales tax rate: 5.5%

import datetime

################# define global variables #####################

SM = 9.99
MED = 12.99
LRG = 17.99
XL  = 21.99
PR_DRINKS = 3.99
PR_BRSTX = 6.99
SALE_TAX = .055
num_small = 0
cost_small=0
num_medium = 0
cost_medium=0
num_large = 0
cost_large = 0
num_xl = 0
cost_xl = 0
num_drinks = 0
cost_drinks = 0
num_breadstix = 0
cost_breadstix = 0
type_pizza = 0
more = 0
subtotal = 0
taxamt = 0
total = 0

################# define program funtions #####################

def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_result()

        askAgain = input("\nWould you like to order again (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more = False
            print ("Thank you for order. Enjoy your Food!")



def get_user_data():
    global nuMED, num_drinks, num_breadstix, type_pizza, num_small, num_medium, num_large, num_xl
    
    type_pizza = int(input("Type of Pizza would like \n1 for Small \n2 for Medium \n3 for Large \n4 for Extra - Large\nSize: "))
    if type_pizza == 1:
        num_small = int(input("Number of Small pizzas: "))

    elif type_pizza == 2:
        num_medium = int(input("Number of Medium pizzas: "))

    elif type_pizza ==  3:
        num_large = int(input("Number of Large pizzas: "))
    

    elif type_pizza == 4:
        num_xl = int(input("Number of Extra Large pizzas: "))
        
    else:
        print('This option is not available')
        get_user_data()

    more = int(input("\nWould you like to order a different size?\n1 for Yes\n2 for No\nInput: "))
    if more == 1:
        get_user_data()

    else:
        num_drinks = int(input("\nNumber of drinks: "))
        num_breadstix = int(input("Number of breadsticks: "))


def perform_calculations():

    global cost_small, cost_medium, cost_large, cost_xl, cost_drinks, cost_breadstix, taxamt, total, subtotal
    cost_small = num_small*SM
    cost_medium= num_medium*MED
    cost_large= num_large*LRG
    cost_xl= num_xl*XL 
    cost_drinks= num_drinks*PR_DRINKS
    cost_breadstix= num_breadstix*PR_BRSTX
    subtotal = cost_small+cost_medium+cost_large+cost_xl+cost_drinks+cost_breadstix
    taxamt = subtotal*SALE_TAX
    total = subtotal+taxamt

def display_result():  
    moneyformat  = '8,.2f'
    print ('******* Palermo Pizza *******')
    print ('Small Pizza    '+ str(num_small)+'x       $' + format(cost_small, moneyformat))
    print ('Medium Pizza   '+ str(num_medium)+'x      $' + format(cost_medium, moneyformat))
    print ('Large Pizza    '+ str(num_large)+'x       $' + format(cost_large, moneyformat))
    print ('X-Large Pizza  '+ str(num_xl)+'x          $' + format(cost_xl, moneyformat))
    print ('Drinks         '+ str(num_drinks)+'x      $' + format(cost_drinks, moneyformat))
    print ('Bread Sticks   '+ str(num_breadstix)+'x   $' + format(cost_breadstix, moneyformat))
    print ('Subtotal:      $'+format(subtotal, moneyformat))
    print ('Tax:           $'+format(taxamt, moneyformat))
    print ('Total:         $'+format(total, moneyformat))
    print (str(datetime.datetime.now()))

########## call on main program to execute ##########

main()
    


        

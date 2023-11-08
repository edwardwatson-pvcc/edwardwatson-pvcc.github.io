# Name: Edward Watson
# Prog Purpose: This program finds the cost of a customers Palermo Pizza Order

# PIZZA Pricing
#-------------------------------------
# Pizza:
#  1. Small $9.99
#  2. Medium   $12.99
#  3. Large   $17.99
#  4. Extra Large   $21.99

#  5. Drinks   $3.99 each
#  6. Order of Breadsticks $6.99

import datetime

############# define global variables #############
# define Pizza prices
PR_SM = 9.99
PR_MED = 12.99
PR_LG = 17.99
PR_XLG = 21.99

PR_DRINK = 3.99
PR_BREAD = 6.99

#define global variables

############ define program functions #############
def main():
    more = True
    while more:
        get_pizza_data()
        perform_pizza_calculations()
        display_pizza_results()
       
        askAgain = input("\nWould you like to order another pizza(Y/N)?: ")
        if askAgain.upper() == "N":
            more = False
            print('Thank you for ordering Palermo Pizza! ')
            
############# Pizza funtions ############

def get_pizza_data():
    global pizza_type, drink_sel, breadstick_sel
    pizzamenu = "\n** Pizza Sizes: \n\t1.Small Pizza \n\t2.Medium Pizza \n\t3.Large Pizza \n\t4.Extra Large Pizza"
    pizza_type = int(input(pizzamenu + "\n** Choose your pizza size: "))

    drink_sel = input("\tWould you like to order a drink with your" + pizza_type + " (Y/N)? ")
    if drink_sel.upper() == "Y":
            drink_type = int(input("\tHow many drinks would you like? "))
            
    breadstick_sel = input("\tWould you like an order of breadsticks?" + " (Y/N)? ")
    if breadstick_sel.upper() == "Y":
            breadstick_type = int(input("\tHow many orders of breadsticks would you like? "))    
        
def perform_pizza_calculations():
    global pizza_cost, drink_cost, breadstick_cost, sub_total, Sales_tax_amt, total

   
    if pizza_type == 1:
        pizza_cost = PR_SM
        
    elif pizza_type == 2:
        pizza_cost = PR_MED

    elif pizza_type == 3:
        pizza_cost = PR_LG

    else pizza_type == 4:
        pizza_cost = PR_XLG
        
    if drink_sel == "Y":
        drink_cost = PR_DRINK * drink_type

    else drink_type == "N":
        drink_cost = 0.00

    if breadstick_type = "Y":
        breadstick_cost = PR_BREAD * breadstick_type

    else breadstick_type == "N":
        breadstick_cost = 0.00

    
    #####find total
    subtotal = pizza_cost + drink_cost + breadstick_cost
    sales tax = subtotal * 0.055
    total = subtotal + sales tax


def display_pizza_results():
    print("---------------------")
    print('***Palermo Pizza***')
    print('***datetime***')
    print('Number of Pizzas: 1')
    print('Number of Drinks: ') + (drink_type)
    print('Number of Breadsticks: ') + (breadstick_type)
    print('Subtotal: $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax: $ ' + format(sales tax, '8,.2f'))
    print('Total Cost: $ ' + format(total, '8,.2f'))
        


########## call on main program to execute ##########
main()

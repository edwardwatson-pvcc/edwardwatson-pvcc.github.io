# Name: Edward Watson
# Name: Wyatt Pennington
# Prog Purpose: This program finds the cost of movie tickets
#  PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
#define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0
total = 0
balance = 0

############## define program functions #############
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global  tuition, capfee, insfee, actfee, total, balance #balance is total minus scholarship
    if inout == 1:
        tuition = RATE_TUITION_IN * numcredits
    elif inout == 2:
        tuition = RATE_TUITION_OUT * numcredits
    capfee = numcredits * RATE_CAPITAL_FEE
    insfee = numcredits * RATE_INSTITUTION_FEE
    actfee = numcredits * RATE_ACTIVITY_FEE
    total = tuition + capfee + insfee + actfee
    balance = total - scholarshipamt
    


def display_results():
    print ('Piedmont Virginia Community College')
    print ('Tuition $ ' + format(tuition,'8,.2f'))
    print ('Capital Fee $ ' + format(capfee,'8,.2f'))
    print ('Instituiton Fee $ ' + format(insfee,'8,.2f'))
    print ('Activity Fee $ ' + format(actfee,'8,.2f'))
    print ('Total $ ' + format(total,'8,.2f'))
    print ('Scholarship Amount $ ' + format (scholarshipamt, '8,.2f'))
    print ('Remaining Balance $ ' + format(balance,'8,.2f'))
    

######## call on main program to execute ########
main()

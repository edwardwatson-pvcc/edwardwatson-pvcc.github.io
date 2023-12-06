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

outfile = 'tuition-webpage.html'

############## define program functions #############
def main():

    open_outfile()
    more = True

    while more:
        get_user_data()
        perform_calculations()
        create_output_file()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_student = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-image: url(wp-tuition.png);">\n')

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
    
def create_output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border="4"   style ="background-color: #FFFFFF;  font-family: arial; margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>PVCC Tuition Rates</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Community College ***\n')
    
    f.write(tr + 'Tuition $ ' + endtd + format(tuition,currency) + endtr)
    f.write(tr + 'Capital Fee $ ' + endtd + format(capfee,currency) + endtr)
    f.write(tr + 'Instituition Fee $ ' + endtd + format(insfee,currency)  + endtr)
    f.write(tr + 'Activity Fee $ ' + endtd + format(actfee,currency)  + endtr)
    f.write(tr + 'Total $ ' + endtd + format(total,currency)  + endtr)
    f.write(tr + 'Scholarship Amount $ ' + endtd + format(scholarshipamt,currency)  + endtr)
    f.write(tr + 'Remaining Balance Fee $ ' + endtd + format(balance,currency)  + endtr)

    f.write(colsp + 'Date/Time: '+ day_time + endtr)
    f.write('</table><br />')
    

######## call on main program to execute ########
main()

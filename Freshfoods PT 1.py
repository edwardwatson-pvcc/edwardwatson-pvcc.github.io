#NAME: Edward Watson
#PROG PUPROSE: 

import datetime

########### LISTS OF DATA ###########
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
     "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

############## NEW LISTS FOR CALC AMOUNTS ############

gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0 

############## TUPLES OF CONSTANT ############
#             C       S      J     M 
# indexs      0       1      2     3
PAY_RATE = ( 16.50, 15.75, 15.75, 19.50 )

#          FED   STATE  SS    MED   RET
#index      0     1     2      3    4
DEB_RATE = (.12, .03, .062, .0145, .04 ) 

############## DEFINE MAIN PROGRAM ##############

def main():
    perform_calc()
    display_results()

def perform_calc():
    global total_gross, total_net

    for i in range(num_emps):

        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]

        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]

        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]

        else:
            pay = hours[i] * PAY_RATE[3]

        ############ CALC DEDUCTIONS 
        fed = pay * DEB_RATE[0]
        state = pay * DEB_RATE[1]
        social = pay * DEB_RATE[2]
        medi_care = pay * DEB_RATE[3]
        retire = pay * DEB_RATE[4]

        
        net = pay - fed - state - social - medi_care - retire
        

        #add totals
        total_gross += pay
        total_net += net 

        #add amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(social)
        medicare.append(medi_care)
        ret401k.append(retire)
        net_pay.append(net)


def display_results():
    currency = '7,.2f'
    currency2 = '12,.2f'
    line = '----------------------------------------------------------------------'
    tab = "\t"

    print(line)
    print('*********************** FRESH FOODS MARKET ***************************')
    print('--------------------- WEEKLY PAYROLL REPORT --------------------------')
    print(tab + tab + str(datetime.datetime.now()))
    print(line)
    titles1 = " Emp Name " + tab + tab + " Job Code " + tab + " Gross Income " + tab
    titles2 = " Fed Inc Tax " + tab + " State Inc Tax " + tab + " Social Security " + tab + "Medicare"  + tab + " 401k Contribution " + tab + " Net Pay "

    print(titles1 + titles2)
    for i in range(num_emps):
        data1 = emp[i] +  "          " + job[i] + tab + tab + format(gross_pay[i], currency) + tab + tab + "  " + format(fed_tax[i], currency) + tab + "   "  
        data2 = format(state_tax[i], currency) + tab + "    " + format(soc_sec[i], currency) + tab + "       " + format(medicare[i], currency) + tab + tab
        data3 = "    " + format(ret401k[i], currency) + "  " + tab + tab + format(net_pay[i], currency) 
        print(data1+ data2 + data3)
    print(line)
    print('********************* TOTAL GROSS: $' + format(total_gross, currency2))
    print('********************* TOTAL Net  : $' + format(total_net, currency2))
            
########## CALL ON MAIN TO EXECUTE ##########            
main()  

#Name: Edward Watson
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195, 250, 350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065, 0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])

        if room_type == "SR":
            subtotal = ROOM_RATES[0] * num_nights
        elif room_type == "DR":
            subtotal = ROOM_RATES[1] * num_nights
        else:
            subtotal = ROOM_RATES[2] * num_nights

        salestax = subtotal * TAX_RATES[0]
        occupancy = subtotal * TAX_RATES[1]
        total = subtotal + salestax + occupancy
             
        grandtotal += total

        guest[i].append(subtotal)
        guest[i].append(salestax)
        guest[i].append(occupancy)
        guest[i].append(total)


def open_out_file():        
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right;} body{background-image: url("crystal.png");}</style> </head>\n')
    f.write('<body>\n')
    f.write('<h1 style="text-align: center;">Emerald Beach Hotel & Resort</h1>\n')
    f.write('<table border="1" style="margin: auto;">\n')

def create_output_html():
    global f, grandtotal
    
    currency_format = "${:8,.2f}"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr style="background-color: green; border: 2px solid black;"><td>'
    th = '<th style="background-color: green; border: 2px solid black;">'
    td = '</td><td>'
    endtr = '</td></tr>\n'

    f.write('<tr>' + th + 'Last Name' + th + 'First Name' + th + 'Room Type' + th + 'Nights' + th + 'Subtotal' + th + 'Sales Tax' + th + 'Occupancy Tax' + th + 'Total' + '</tr>\n')

    for g in guest:
        g = list(map(str, g))  # Convert all values to strings
        f.write(tr + td.join(g) + endtr)

    grandtotal_str = currency_format.format(grandtotal)
    f.write('<tr style="background-color: green; border: 2px solid black;"><td colspan="7" style="text-align: right;"><strong>Grand Total:</strong></td><td>{}</td></tr>\n'.format(grandtotal_str))
    f.write('</table><br />')
    f.write('</body></html>')
    f.close()
    print('Open ' + outfile + ' to view data.')


##call on main program to execute##
main()

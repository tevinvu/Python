#!/usr/bin/python3
#Find out how much to a pay off a house mortgage
#some source code and idea from David Beazley

import math
import sys
#read in the principal, payment by Month and the rate:
if len(sys.argv) != 4:
    raise SystemExit("""Usage: 01-MortgageCalculator.py principal paymentByMonth rate. 
                        Example: python3 01-MortgageCalculator.py 700000 3532.11 0.05""")
#convert the argument into float 
principal = float(sys.argv[1])
payment = float(sys.argv[2])
rate = float(sys.argv[3])
total_paid = 0

#Calculation part
while principal > 0:
    interest = principal * (rate/12)
    principal = principal + interest - payment
    total_paid += payment
    total_paid_dollars = math.ceil(total_paid)

#Print out the total paid in dollars with/without cents
print ("Total paid with dollars and cents: $ {:,.2f}".format(total_paid))
print("Total paid with dollars: $ {:,.0f}".format(total_paid_dollars))


 
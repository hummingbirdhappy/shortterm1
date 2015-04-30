"""
File: voccola_huang_gasoline.py
Author: Libby Voccola and Grace Huang
Description:
    Prints the pounds of carbon dioxide produced by a given number of gallons of gasoline.
    Prints number of barrels of crude oil required to produce given gallons of gasoline.
    Prints current average cost in U.S. (USD) for given gallons of gasoline.
"""
# ask user to input number of gallons of gasoline
gas_gallons = float(raw_input('Please enter the number of gallons of gasoline: '))

#One gallon of gasoline produces approximately 19.64 pounds of carbon dioxide
carbon_dioxide_pounds = 19.64*gas_gallons

#output number of pounds of carbon dioxide produced
print gas_gallons, 'gallons of gasoline produces approximately', carbon_dioxide_pounds, 'pounds of carbon dioxide.'

#One barrel of crude oil yields about 19 gallons of gasoline
crude_oil_barrels = gas_gallons/19

#output barrels of crude oil required
print 'To produce', gas_gallons, 'gallons of gasoline, about', crude_oil_barrels, 'barrels of crude oil are required.'

#One gallon of gasoline costs approximately 2.580 dollars
average_cost = gas_gallons*2.580

#output average cost in U.S (USD)
print gas_gallons, 'gallons of gasoline costs about', average_cost,'dollars in the U.S.'



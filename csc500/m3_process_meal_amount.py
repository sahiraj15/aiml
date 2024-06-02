import logging as log

# Dictionaries are most appropriate data structure for the purpose
tax_summary = {'meal_price': float(input("Enter the meal price : ")), 'waiter_incentive': 0.18, 'sales_tax': 0.07}

tip_amount = tax_summary['waiter_incentive'] * tax_summary['meal_price']
tax_amount = tax_summary['sales_tax'] * tax_summary['meal_price']

print("Meal price   : {0:0.2f}".format(tax_summary['meal_price']))
print("Tip amount   : {0:0.2f}".format(tip_amount))
print("Tax amount   : {0:0.2f}".format(tax_amount))
print("Total Amount : {0:0.2f}".format(tax_summary['meal_price'] + tip_amount + tax_amount))

import os
import sys

number_of_loyal_points = 0

purchased_quantity = input("Enter the number of books purchased: ")
if (float(purchased_quantity) - float(purchased_quantity).__trunc__()) != 0:
    raise "Received decimal number, Enter your input in Integers format only."
elif float(purchased_quantity) < 0:
    raise "Enter an integer value greater than 0."


purchased_quantity = int(purchased_quantity)
if purchased_quantity < 2:
    number_of_loyal_points = 0
elif purchased_quantity < 4:
    number_of_loyal_points = 5
elif purchased_quantity < 6:
    number_of_loyal_points = 15
elif purchased_quantity < 8:
    number_of_loyal_points = 30
else:
    number_of_loyal_points = 60

if purchased_quantity > 1:
    book_string = 'books'
else:
    book_string = 'book'

print("")
print("You purchased {} {} in this month.".format(purchased_quantity, book_string))
print("Number of points awarded: {}.".format(number_of_loyal_points, book_string))


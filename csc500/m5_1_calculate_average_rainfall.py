import os
import sys
import numpy as np

num_of_months = 12
rainfall_stats_list = []

num_of_years = input("Enter the number of years (Integers only): ")
if (float(num_of_years) - float(num_of_years).__trunc__()) != 0:
    raise "Received decimal number, Integers are the only legitimate values."
elif float(num_of_years) <= 0:
    raise "Enter an integer value greater than 0."

# Data Intake
for yr_num in range(1, int(num_of_years) + 1):
    for mon_num in range(1,num_of_months + 1):
        monthly_recorded_rainfall = float(input("Enter the rainfall in inches for Year-Month {}-{}: ".format(yr_num, mon_num)))
        rainfall_stats_list.append(monthly_recorded_rainfall)

# Calculate averages
rainfall_array = np.array(rainfall_stats_list)

print("")
print("Rainfall statistics are collected for {} months.".format(rainfall_array.size))
print("Total rainfall recorded: {:.2f}".format(rainfall_array.sum()))
print("Average rainfall per month: {:.2f}".format(rainfall_array.sum()/rainfall_array.size))
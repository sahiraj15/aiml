
num1 = float(input("Enter the first number (numerator for Division operation) : "))

print('Note : For Division operation the denominator shall be any number other than 0.')
num2 = float(input("Enter the second number (denominator for Division operation) : "))

print('')
number_multiplication = num1 * num2
print('Multiplication of', num1, 'and', num2, ':', number_multiplication)

print('')
if num2 == 0:
    print("Division operation cannot be performed, please enter any value other than 0 and retry.")
    exit(35)
else:
    number_division = num1 / num2
    print('Division of', num1, 'and', num2, ':', number_division)

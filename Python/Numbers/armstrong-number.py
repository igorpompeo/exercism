def is_armstrong_number(number):
    # step 1: split the number into individual digits
    digits = [int(digit) for digit in str(number)]
    # step 2: calculate the sum of the cubes of the digits
    num_digits = len(digits)
    sum_of_cubes = sum(digit**num_digits for digit in digits)
    # step 3: check if the sum of cubes is equal to the original number
    return sum_of_cubes == number

# Test the function
num = input("Wrote a number to check if is / not an Armstrong number: ")
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
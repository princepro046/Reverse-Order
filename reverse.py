def count_digits(number):
    # Ensure the number is positive for counting digits
    if number == 0:
        return 1  # Special case for 0, as it has 1 digit

    count = 0
    while number > 0:
        number = number // 10  # Remove the last digit
        count += 1  # Increment the digit count
    
    return count

# Taking input from the user
number = int(input("Enter a number: "))

# Counting the digits in the number
digit_count = count_digits(abs(number))  # Use absolute value to handle negative numbers

# Printing the result
print(f"The number {number} has {digit_count} digits.")

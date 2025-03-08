# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    # TODO: Implement this function
    return max(num1, num2, num3)

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    # TODO: Implement this function
    return min(num1, num2, num3)

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    # TODO: Implement this function
  if number > 0: 
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    # TODO: Implement this function
  result = ''
  for i in range (rows):
    for j in range (i + 1):
      result += '*' 
    result += '\n'  
  return result.rstrip()

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    # TODO: Implement this function
    result = ''
    num = 1
    while num <= limit and num <= 20:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n" # Convert number to string for consistency
        num += 1
    return result.rstrip()

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
  total = 0
  for n in range (start, end + 1):
    if n % 2 == 0:
      total += n
  return total

def addRange():
  try:
    # Get the first number and validate it
    number1 = input('Enter the first number: ')
    while not number1.lstrip('-').isdigit() or int(number1) <= 0:  # Ensures that it's a positive integer
      print('Error: The first number must be a positive integer')
      number1 = input('Enter the first number: ')
    number1 = int(number1)  # Transform the input to an integer after validating

    # Get the second number and validate it
    number2 = input('Enter the second number: ')
    while not number2.lstrip('-').isdigit() or int(number2) < 0 or int(number2) >= number1: # Checks if the input is a number less than number1 and >= 0
      print(f'Error: The second number must be a non-negative integer smaller than {number1}')
      number2 = input('Enter the second number: ')
    number2 = int(number2)  # Transform the input to an integer after validating

    numbers = []
    
    # Get the numbers within the range [number2, number1) and validate
    number = int(input('Enter a number: '))
    while number >= number2 and number < number1:  # Checks if the number is within the desired range
      numbers.append(number)  # Add the number to the list
      number = int(input('Enter a number: '))  # Get the next number

    # Print the sum of the numbers
    print(f'SUM of {numbers} = {sum(numbers)}')
  
  except ValueError:
    print('Error: Invalid input. Please enter a valid number.')


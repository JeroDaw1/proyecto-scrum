def division():
  try:
    # Validate the first number
    number1 = input('Enter the first number: ')
    while not number1.lstrip('-').isdigit():  # Check if it is a positive integer
      print('Error: The first number must be an integer')
      number1 = input('Enter the first number: ')
    number1 = int(number1)  # Convert to integer

    # Validate the second number
    number2 = input('Enter the second number: ')
    while not number2.isdigit() or number2 == '0':  # Check if it is a positive integer and not zero
      print('Error: The second number must be a positive integer and not zero')
      number2 = input('Enter the second number: ')
    number2 = int(number2)  # Convert to integer

    # Perform the division
    result = number1 / number2
    print(f'{number1} ÷ {number2} = {result}')
  
  except ZeroDivisionError:
    print('Error: Cannot divide by zero')  # Handle the case of division by zero
  except ValueError:
    print('Error: Invalid input. Please enter integers only.')

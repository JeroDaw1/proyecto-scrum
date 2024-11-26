def division():
  try:
    number1 = input('Enter the first number: ')
    while not (number1.lstrip('-').isdigit() and (number1[0] == '-' or number1)):  # Checks if the input is an integer
      print('Error: The first number must be a positive integer')
      number1 = input('Enter the first number: ')

    number1 = int(number1)  # Convert input to integer after validating

    number2 = input('Enter the second number: ')
    while not number2.isdigit() or number2 == '0':  # Checks if the input is a positive integer
      print('Error: The second number must be a positive integer')
      number2 = input('Enter the second number: ')

    number2 = int(number2)  # Convert input to integer after validating

    print(f'{number1} ÷ {number2} = {number1 / number2}')
  except ValueError:
    print('Error: Cannot substract')

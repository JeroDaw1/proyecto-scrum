def multTable():
  # Ask the user to enter a positive integer
  number = input('Enter a positive integer: ')
  
  # Validate if the input is a positive integer
  while not number.isdigit() or int(number) <= 0:
    print('Error: Please enter a valid positive integer.')
    number = input('Enter a positive integer: ')
  
  number = int(number)  # Convert the input to an integer

  # Print the multiplication table for the number
  print(f'\nMultiplication table for {number}:')
  for i in range(11):
    print(f'{number} x {i} = {number * i}')

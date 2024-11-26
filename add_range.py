def addRange():
    try:
        # Get the first number and validate it
        number1 = input('Enter the first number: ')
        while not number1.lstrip('-').isdigit() or int(number1) <= 0:  # Checks if the input is an integer
            print('Error: The first number must be an integer')
            number1 = input('Enter the first number: ')
        number1 = int(number1)  # Transform the input to an integer after validating

        # Get the second number and validate it
        number2 = input('Enter the second number: ')
        while not number2.lstrip('-').isdigit() or int(number2) <= 0 or int(number2) >= number1: # Checks if the input is an integer between number1 and number2
            print(f'Error: The second number must be an integer smaller than {number1}')
            number2 = input('Enter the second number: ')
        number2 = int(number2)  # Transform the input to an integer after validating

        numbers = []
        
        # Get the numbers and validate them until the user enters a number greater than number2 and smaller than number1
        number = int(input('Enter a number: '))
        while number > number2 and number < number1:
            numbers.append(number)  # Add the number to the list
            number = int(input('Enter a number: '))  # Get the next number

        # Print the sum of the numbers
        print(f'SUM of {numbers} = {sum(numbers)}')
    
    except ValueError:
        print('Error: Invalid input. Please enter a valid number.')
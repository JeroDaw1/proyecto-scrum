from addition import *
from substraction import *
from multiplication import *
from division import *
from add_range import *
from counting_numbers import *
from mult_table import *
from powers import *
from sumto2n1 import *
from sumToN import *

print('Welcome!\n')
print('Calculator operations you can perform:')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')
print('5. Add range')
print('6. Counting numbers')
print('7. Multiplication Table')
print('8. Powers')
print('9. SumTo2N1')
print('10. SumToN')
print('11. Temperatures')
print('12. Exit')

option = -1
while option < 1 or option > 12:
  try:
    option = input('Choose an option: ').strip()  # strip to remove leading/trailing spaces

    if not option:  # If the input is empty (user presses Enter without typing)
      print('Error: You must choose an option between 1 and 12.')
      option = -1
      continue
    
    # Check if the input is a valid integer
    option = int(option)

    if option < 1 or option > 12:
      print('Error: Invalid option. Enter a number between 1 and 12.')
      continue

  except ValueError:
    print('Error: Invalid option. Please enter a valid number.')

  # Handle each option accordingly
  if option == 1:
    addition()
  elif option == 2:
    substraction()
  elif option == 3:
    multiplication()
  elif option == 4:
    division()
  elif option == 5:
    addRange()
  elif option == 6:
    countingNumbers()
  elif option == 7:
    multTable()
  elif option == 8:
    powers()
  elif option == 9:
    sumTo2N1()
  elif option == 10:
    sumToN()
  elif option == 11:
    try:
      print('Temperatures')
    except ValueError:
      print('Error: Cannot handle temperatures.')

  elif option == 12:
    print('Exiting...')

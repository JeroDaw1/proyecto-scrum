from addition import *

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
while option <= 0 or option > 12:
  try:
    option = input('Choose an option: ')

    if option != option.strip():
      print('Error: Invalid option. Enter an option between 1 and 12')
      option = -1
      continue

    option = int(option)

    if option < 1 or option > 12:
      print('Error: Invalid option. Enter an option between 1 and 12')
      continue

  except ValueError:
    print('Error: Invalid option')

  if option == 1:
    addition()
  elif option == 2:
    try:
      print('Resta')
    except ValueError:
      print('Error: No se puede restar')

  elif option == 3:
    try:
      print('Multiplicacion')
    except ValueError:
      print('Error: No se puede multiplicar')

  elif option == 4:
    try:
      print('Division')
    except ValueError:
      print('Error: No se puede dividir')

  elif option == 5:
    try:
      print('Agregar rango')
    except ValueError:
      print('Error: No se puede agregar rango')

  elif option == 6:
    try:
      print('Contador de números')
    except ValueError:
      print('Error: No se puede contar')

  elif option == 7:
    try:
      print('Tabla de multiplicar')
    except ValueError:
      print('Error: No se puede multiplicar')

  elif option == 8:
    try:
      print('Potencias')
    except ValueError:
      print('Error: No se puede potenciar')

  elif option == 9:
    try:
      print('Sumar a 2N1')
    except ValueError:
      print('Error: No se puede sumar')

  elif option == 10:
    try:
      print('Sumar a N')
    except ValueError:
      print('Error: No se puede sumar')

  elif option == 11:
    try:
      print('Temperaturas')
    except ValueError:
      print('Error: No se puede sumar')

  elif option == 12:
    print('Saliendo...')

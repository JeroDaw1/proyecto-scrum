print('¡Bienvenid@!\n')
print('Operaciones de calculadora que puedes realizar:')
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')
print('5. Agregar rango')
print('6. Contador de números')
print('7. Tabla de multiplicar')
print('8. Potencias')
print('9. Sumar a 2N1')
print('10. Sumar a N')
print('11. Temperaturas')
print('12. Salir')

option = -1
while option <= 0 or option > 12:
  try:
    option = int(input('Elige una opción: '))
    if option < 1 or option > 12:
      print('Error: Opción invalida. Introduce una opción entre 1 y 12')
      continue
  except ValueError:
    print('Error: Opción invalida')

  if option == 1:
    try:
      print('Suma')
    except ValueError:
      print('Error: No se puede sumar')

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

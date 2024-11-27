def countingNumbers():
  counter = 0
  
  while True:
    try:
      # Get a number from the user
      number = int(input("Introduce a number (0 to exit): "))
      
      # If the number is 0, we break the loop
      if number == 0:
        break
      
      # If the number is not 0, we increment the counter
      counter += 1
        
    except ValueError:
      # If an error occurs when trying to convert to an integer, we show a message
      print("¡Error! Debes introducir un número entero válido.")
  
  # We show the amount of numbers entered, excluding the zero
  print(f"You have entered {counter} numbers.")


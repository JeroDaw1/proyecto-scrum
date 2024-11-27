def powers():
  while True:
    try:
      # Ask the user for the base number (a positive integer)
      base = input("Enter the base (positive integer): ").strip()
      
      # Check if the input is a valid positive integer
      if not base.isdigit() or int(base) <= 0:
        print("Error: The base must be a positive integer. Please try again.")
        continue
      
      base = int(base)  # Convert the base to an integer
      
      break  # If the base is valid, break out of the loop

    except ValueError:
      # This block won't be reached because we are checking with .isdigit(), but it's here for safety
      print("Error: The base must be a positive integer. Please try again.")
  
  while True:
    try:
      # Ask the user for the exponent (a positive integer)
      exponent = input("Enter the exponent (positive integer): ").strip()
      
      # Check if the input is a valid positive integer
      if not exponent.isdigit() or int(exponent) <= 0:
        print("Error: The exponent must be a positive integer. Please try again.")
        continue
      
      exponent = int(exponent)  # Convert the exponent to an integer
      
      break  # If the exponent is valid, break out of the loop

    except ValueError:
      # This block won't be reached because we are checking with .isdigit(), but it's here for safety
      print("Error: The exponent must be a positive integer. Please try again.")
  
  # Calculate the power using a loop (base ** exponent)
  result = 1
  for _ in range(exponent):
    result *= base  # Multiply the result by the base for the exponent times

  # Display the result
  print(f"{base} raised to the power of {exponent} is {result}")

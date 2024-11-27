def sumTo2N1():
  while True:
    try:
      # Ask the user for the number N (a positive integer)
      N = input("Enter a positive integer N: ").strip()
      
      # Check if the input is a valid positive integer
      if not N.isdigit() or int(N) <= 0:
        print("Error: N must be a positive integer. Please try again.")
        continue

      N = int(N)  # Convert N to an integer
      
      break  # If N is valid, break out of the loop

    except ValueError:
      # This block won't be reached because we are checking with .isdigit(), but it's here for safety
      print("Error: N must be a positive integer. Please try again.")

  # Initialize sum and the list to keep track of odd numbers
  total_sum = 0
  odd_numbers = []
  
  # Add odd numbers from 1 up to N (if N is odd)
  for i in range(1, N + 1, 2):
    odd_numbers.append(str(i))  # Add the odd number as a string for easy formatting
    total_sum += i  # Sum the odd numbers

  # Subtract 1 from the sum
  total_sum -= 1

  # Create the formatted string for the sum sequence
  expression = " + ".join(odd_numbers) + " - 1"
  
  # Print the result in the desired format
  print(f"{expression} = {total_sum}")

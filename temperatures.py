def temperatures():
  # List to store the 6 temperature values
  temperatureList = []
  hours = [0, 4, 8, 12, 16, 20]  # Simulated times of the day

  print("Please enter temperatures for different times of the day (every 4 hours):")

  # Loop to ask for 6 temperature values
  for hour in hours:
    while True:
      userInput = input(f"Temperature at {hour}:00: ").strip()
      if userInput.isdigit():
        temperatureList.append(int(userInput))
        break
      else:
        print("Invalid input. Please enter a positive integer.")

  # Calculate average, maximum, and minimum temperature
  average = sum(temperatureList) / len(temperatureList)
  maxTemp = max(temperatureList)
  minTemp = min(temperatureList)

  # Display results
  print(f"\nAverage temperature: {average:.2f}")
  print(f"Maximum temperature: {maxTemp}")
  print(f"Minimum temperature: {minTemp}")

# List of temperatures recorded over a week
temperatures = [15, 18, 21, 19, 22, 16, 17]

# Check if there was any day with a temperature above 20 degrees
temperature_above_20 = False
for temp in temperatures:
    if temp > 20:
        temperature_above_20 = True
        break

print("Was there any day above 20 degrees?", temperature_above_20)

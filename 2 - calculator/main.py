print("Welcome to the tip calculator\n")
bill = float(input("What was the total bill? "))
perc = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total = bill * (perc / 100 + 1) / people

t = "{:.2f}".format(total)
print(f"Each person should pay: ${t}")
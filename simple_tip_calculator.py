print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 15 20 25 "))
people = int(input("How many people to split the bill? "))

total_bill = (tip/100 * bill + bill) / people

print(f"Your total bill is: ${total_bill:.2f} per person.")



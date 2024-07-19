#Write your code below this line 👇
print("Welcome to the tip calculator!")
# Getting inputs from the user
y = float(input("What was the total bill? $"))
z = int(input("How much tip would you like to give? 10, 12, or 15? "))
x = int(input("How many people to split the bill? "))

# Calculating the amount each person should pay
if z == 10:
    a = (y / x) * 1.10
    a = f"{a:.2f}"
    print(f"Each person should pay: ${a}")
elif z == 12:
    a = (y / x) * 1.12
    a = f"{a:.2f}"
    print(f"Each person should pay: ${a}")
elif z == 15:
    a = (y / x) * 1.15
    a = f"{a:.2f}"
    print(f"Each person should pay: ${a}")
else:
    print("Invalid tip percentage entered.")

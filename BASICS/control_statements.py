# Control Statement in Python:

# Single way selection statement:
# if condition: (do this or nothing)

order = 550
minimum_order = 500
delivery_charge = 50

if order > minimum_order:
    delivery_charge = 0 # free delivery

total_order = order + delivery_charge
print(total_order)

# Two way selection statement:
# if - else condition:  (do this or do that)
marks = 75
passing_marks = 40
if marks > passing_marks:
    print("You havd passed the exam")
    print("Congratulations!")
else:
    print("You had failed the exam")
    print("Try again next time")

# Multi-way selection statement:
# if - elif - else condition:   
# (do this or do something else as followed)

# example 1
product = input("Enter the product name: ")
if product == "laptop":
    print("You have selected a laptop")
elif product == "mobile":
    print("You have selected a mobile")
elif product == "tablet":
    print("You have selected a tablet")
else:
    print("Selected an unknown product")

# example 2
number = 45
if number > 0:
    print("POSITIVE NUMBER")
elif number == 0:
    print("ZERO/NEUTRAL NUMBER")
else:
    print("NEGATIVE NUMBER")

# example 3
# Nested if-else statement:
district = "Tanjore"
city = "Kumbakonam"

if district == "Tanjore":
    print("You're in Tanjore District")
    if city == "Kumbakonam":
        print("You're in Kumbakonam City")
    elif city == "Pattukottai":
        print("You're in Pattukottai City")
    else:
        print("You're in Tanjore City")

elif district == "Madurai":
    print("You're in Madurai District")
    if city == "Madurai":
        print("You're in Madurai City")
    elif city == "Tirumangalam":
        print("You're in Tirumangalam City")
    else:
        print("You're in Melur City")

elif district == "Trichy":
    print("You're in Trichy District")
    if city == "Kumbakonam":
        print("You're in Manapparai City")
    elif city == "Trichy":
        print("You're in Trichy City")
    else:
        print("You're in Srirangam City")

else:
    print("You're in unknown district")

# Short hand if-else statement:
# Ternary Operator:
lucky_number = 369  # (or) lucky_number = 786
print("Lucky number is 369") if lucky_number == 369 else print("Lucky number is 786")

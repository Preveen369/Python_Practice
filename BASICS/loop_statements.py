# Looping (Iteration) statements

# 1. while loop: looping items based on condition

i = 0
while i <= 6:   # loop - condition
    i += 1 
    if i==3:
        # break  # exit the loop when i is 3
        continue    # skip the curr iteration when i is 3
    print(i)
else:   # executed when loop finished normally
    print("Loop completed successfully")


# 2. for loop: looping items from the sequence type
# and either loops over stmts., certain times

# stop: break; skip: continue;

l1 = [10, 20, 30, 40, 50, 60]

for each_num in l1:
    print(each_num)

word = "Python"
for each_char in word:
    print(each_char)
else:
    print("Loop completed successfully")


# range() function: generates a sequence of numbers
# range(end)
# range(start, end)
# range(start, end, step)

for num in range(4, 9, 2):
    print(num)


# Nested for/while loops:

color = ["red", "blue", "green"]
vehicles = ["car", "bike", "bus"]

for each_color in color:
    for each_vehicle in vehicles:
        print(each_color, each_vehicle)


# assert statement: used for debugging purposes
# It tests a condition and raises an "AssertionError" if the condition is false.

number = 100
# number = -100  # result in AssertionError
assert number > 0, "Number isn't POSITIVE"

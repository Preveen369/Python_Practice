# input(), filter() and map() functions in python:

# input() function => allows user to enter input from command line

obj_name = input("Enter the name of object: ")
print(obj_name)
num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))
result = num1 + num2
print("Sum: ", result)


# filter() function => used to apply the function on each of items and returns
# "iterator", with only those items which returns "true" when passed in function

def isPrime(num):
    if (num % 2 != 0):
        return True
    else:
        return False

numbers = [1,2,3,4,5,6,7,8,9,10]
prime_nums = list(filter(lambda num : num % 2 != 0, numbers))
prime_nums = list(filter(isPrime, numbers))

prime_nums = []

for num in numbers:
    if isPrime(num):
        prime_nums.append(num)
        
print(prime_nums)


# map() function => used to apply the function on each of items, returns
# "iterator", with results applied on each of the items

dec_nums = [10,11,12,13,14,15,16]
nums_list = []

# nums_list = list(map(str, dec_nums))

for num in dec_nums:
    nums_list.append(str(num))

print(nums_list)
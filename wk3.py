# sum_value = 5 + 8
# sum_2 = (2 + (sum_value))
# print(sum_2)

# my_list = [1,2,3,4] # Initialize my_list

# my_list_2 = [5,6,7,8] # Initialize my_list_2

# my_list = my_list + my_list_2 # Take the current value of my_list and add my_list_2 to it

# print(my_list) # Prints: [1, 2, 3, 4, 5, 6, 7, 8]

# name = "Hello " # Set name variable to an string 'hello '

# name = name + "World!" # Take the current name value and add 'world' to it

# print(name) # Prints: Hello World!

# print(5 - 3)

# my_list = [1,2,3,4] # Initialize my_list

# my_list = my_list * 3 # Take my_list and multiply it by 3

# # print(my_list) # Prints: [1,2,3,4,1,2,3,4,1,2,3,4]
# # print(5 / 2)
# # print(5 // 3)


# variable_1 = 5 # Initialize the variable to 5
# print(variable_1)


# variable_1 = variable_1 + 5 # Take the current value of the variable and add 5
# print(variable_1)


# variable_1 = variable_1 - 5 # Take the current value of the variable and subtract 5
# print(variable_1)

# variable_1 += 20 # Take the current value of the variable and add 20
# print(variable_1)

# variable_1 -= 5 # Take the current value of the variable and subtract 5
# print(variable_1)

# variable_1 = variable_1 / 2 # Take the current value of the variable and floating point divide by 2
# print(variable_1)


# variable_1 = variable_1 // 2 # Take the current value of the variable and integer divide by 2
# print(variable_1)

# variable_1 //= 2.5 # Take the current value of the variable and integer divide by 2
# print(variable_1)

# print(5 % 3)
# print(5 // 3)

# print(5 > 3) # Prints: True; since 5 is greater than 3

# result = 5 > 3 # You can store the result in a variable

# print(result) # Prints: True

# print(3 > 5) # Prints: False; since 3 is NOT greater than 5

# print(5 >= 5) # Prints: False; since 5 is NOT greater than 5 (they are equal)

# print(5 >= 3) # Prints: True; since 5 is greater than 3

# result = 5 >= 3 # You can store the result in a variable

# print(result) # Prints: True

# print(3 >= 5) # Prints: False; since 3 is NOT greater than 5

# print(5 >= 5) # Prints: True; since 5 is equal to 5

# print(5 < 3) # Prints: False; since 5 is NOT less than 3

# result = 5 < 3 # You can store the result in a variable

# print(result) # Prints: False

# print(3 < 5) # Prints: True; since 3 is less than 5

# print(5 < 5) # Prints: False; since 5 is NOT less than 5 (they are equal)

# print(not 5 < 3) # Prints: True; since the statement 5 < 3 evaluates to False

# result = not 5 < 3 # You can store the result in a variable

# print(result) # Prints: True

# # print(not 3 < 5) # Prints: False; Since the statement 3 < 5 evaluates to True

# print(5 < 3 and 8 > 6) # Prints: False; since both statements evaluate to False

# print(5 > 3 and 8 > 6) # Prints: True; since the first statement evaluates to True


# print(5 < 3 or 8 > 6) # Prints: True; since both statements evaluate to True

# print(5 > 3 or 8 > 6) # Prints: True; since the second statement evaluates to True

# name = input("John") # Take someones name from the command line

# print("john" in name) # Prints: True if john is name given, or False otherwise

# print(4 in [1,2,3]) # Prints: False since no 4 is present in the list

# print(4 in [1,2,3,4]) # Prints: True since 4 is present in the list

# x = 2 # Setting up the x variable

# if x < 3:
#     x += 2 # This will run if x < 3, otherwise it will be skipped over

# print(x) # Since this is on a lower indentation level, this code will run regardless

# if x < 3:
#     x += 2 # This will run if x < 3, otherwise it will be skipped over

# print(x) # Since this is on a lower indentation level, this code will run regardless

# x = 2 # Setting up the x variable

# if x < 3:
#     x += 2 # This will run if x < 3, otherwise it will be skipped over
# else:
#     x -= 1 # This will run if x is not less than 3

# print(x) # Since this is on a lower indentation level, this code will run regardless

# if x < 3:
#     x += 2 # This will run if x < 3, otherwise it will be skipped over
# else:
#     x -= 1 # This will run if x is not less than 3

# print(x) # Since this is on a lower indentation level, this code will run regardless


# user_value = int(input("Enter a number between 0 and 5: "))

# if user_value == 0:
#     print("Zero")
# elif user_value == 1:
#     print("One")
# elif user_value == 2:
#     print("Two")
# elif user_value == 3:
#     print("Three")
# elif user_value == 4:
#     print("Four")
# elif user_value == 5:
#     print("Five")
# else: # If value is not between 0 and 5
#     print("Value provided is not between 0 and 5!")


# EXCERCISES FOR WEEK 3

"""
    =========== Exercise 1 =============

    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""

result = 0
number_1 = 5
number_1 += 6

# Do more operations on number 1 until it equals eleven

result = number_1
print(result == 11)


"""
    =========== Exercise 2 =============

    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.

    For example if someone put in 8, then it would print 'eight'.
    
    Hint: Use if, elif and else statements.
"""


user_value = int(input("Enter a number between 0 and 10: "))

if user_value == 0:
    print("Zero")
elif user_value == 1:
    print("One")
elif user_value == 2:
    print("Two")
elif user_value == 3:
    print("Three")
elif user_value == 4:
    print("Four")
elif user_value == 5:
    print("Five")
elif user_value == 6:
    print("Six")
elif user_value == 7:
    print("Seven")
elif user_value == 8:
    print("Eight")
elif user_value == 9:
    print("Nine")
elif user_value == 10:
    print("Ten")
else: # If value is not between 0 and 10
    print("Value provided is not between 0 and 10!")


"""
    =========== Exercise 3 =============

    Before running the code below try to
    figure out which print statement will
    execute and why. Then uncomment the code
    and check if you were right.
"""

number = 0
number += 15
number //= 2
number *= 6
number -= 4

if number < 10:
    print("Less than 10")

elif 10 <= number <= 20:
    print("Between 10 and 20")

elif 20 <= number <= 30:
    print("Between 20 and 30")

elif 30 <= number <= 40:
    print("Between 30 and 40")

else:
    print("¯\_(ツ)_/¯")
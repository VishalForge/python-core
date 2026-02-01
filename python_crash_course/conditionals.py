'''
 Topic = if statements
 chapter = 5
 Source =Python crash course 2nd Edition
 Examples of conditional statements

'''

# Basic if statement
age = 18

if age >= 18:
    print("You are allowed to vote")


# if-else statement
age = 16

if age >= 18:
    print("You are allowed to vote")
else:
    print("You are not allowed to vote")


# if-elif-else chain
age = 13

if age >= 18:
    print("You can read adult books")
elif age >= 13:
    print("You can access teen contents")
else:
    print("You can only access kids content")



# Multiple independent if statements
requested_toppings = ["chilli", "onion", "capsicum"]

if "chilli" in requested_toppings:
    print("Adding chilli")
if "onion" in requested_toppings:
    print("Adding onion")
if "capsicum" in requested_toppings:
    print("Adding capsicum")



# Using if inside a loop
users = ['ram', 'roy', 'zara']

for user in users:
    if user == 'ram':
        print(f"Hello {user.title()}, welcome back!")
    else:
        print(f"Hello {user.title()}")




# Checking for an empty list
users = []

if users:
    for user in users:
        print("Hello {user.title()}")
else:
    print("No user found")



# Using multiple lists with if-else statement
brands = ["bmw", "audi"]
requested = ["nano", "hyundai"]

for item in requested:
    if item in brands:
        print(f"We have {item}")
    else:
        print(f"Sorry, we don't have {item.title()}")
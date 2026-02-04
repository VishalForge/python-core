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




# Equality and Inequality checks

# Equality (==) checks VALUE, not meaning
a = 4
print(a == 4)   # True
print(a == 10)   # False


# Inequality (!=)
requested_items = ['clove', 'banana shake']

if 'banana shake' != 'apple juice':
    print("Different items")



# Logical operators: AND / OR
age = 18
has_id = True

# AND = both conditions must be True
if age >= 18 and has_id:
    print("Allowed entry")

# OR = at least one condition must be true
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access granted")





# if-elif-else chain
# Python stops checking after the first True condition.

age = 13
book = "Reverend Insanity"

if age >= 18:
    print(f"You can read {book}")
elif age >= 13:
    print('Restricted access')
else:
    print("Access denied")



# Multiple independent if statements
# Each condition is checked separately. Useful when multiple actions may apply.
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







# Membership test
locations = ['uk', 'us', 'norway']
submit_location = ['japan']

# 'not in' checks absence
if submit_location not in locations:
    print(f"{submit_location} is not in the allowed list")


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
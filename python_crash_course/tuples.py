# This file contains the Tuple operations that I learned from python crash course 2nd edition book.



# Tuple contains the data in them and makes them immutable. Tuple are used for storing values that should not be changed throughout the program.
# Tuple is defined using paraenthesis and it stores data inside it and makes it immutable.

name = ("roy", "Vasi") # This is an example of a tuple.

name[0] = 'kavi' # It will cause an Error because Tuple are immutable.
print(name)

number = (45,) # Even if a tuple consist of only one element it has to be defined by a trailing comma. Because tuples are defined by the presence of comma.
print(type(number))  # type method will tell that this is a tuple.

num = (1) # This is not a tuple because it is not followed by a trailing comma.
print(type(num)) # Type method tells that this is an integer.


# Looping through a tuple 
guests = ('ram', 'roy', 'zara')
for guest in guests:
    print(guest.title())
    print("You are invited for the party.")


# The values of the tuple can't change but we can reassign the new values for the new tuple with the same variable name. 
guests = ('goku', 'zoro', 'luffy')
for guest in guests:
    print(f"You are an invited person Mr. {guest.title()}")






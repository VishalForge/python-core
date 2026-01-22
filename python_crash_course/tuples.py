# This file contains the Tuple operations that I learned from python crash course 2nd edition book.



# Tuple is basically the list that is immutable.
# Tuple is defined using paraenthesis and it stores data inside it and makes it immutable.

name = ("roy", "Vasi") # This is an example of a tuple.

number = (45,) # Even if a tuple consist of only one element it has to be defined by a trailing comma. Because tuples are defined by the presence of comma.

# Looping through a tuple 
guests = ('ram', 'roy', 'zara')
for guest in guests:
    print(guest.title())
    print("You are invited for the party.")


# The values of the tuple can't change but we can reassign the new values for the new tuple with the same variable name. It's called Writing over a Tuple.
guests = ('goku', 'zoro', 'luffy')
for guest in guests:
    print(f"You are an invited person Mr. {guest.title()}")



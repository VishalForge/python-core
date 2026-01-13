# Lists basics - Python Crash Course (ch. 3-4)
# This file demonstrates list operations I learned.


 # List is a collection of items in a particular order and it is mutable.

numbers = [1, 2, 3, 4]

# modifying the lis by using the index position of a item.
numbers[1] = 6

# append() method adds what we want to add at the end of the list.
numbers.append(7)

#insert() method inserts a element to the list to our desired index position in the list. This method doesn't remove any existing elements from the list instead it just displaces their positions.
numbers.insert(0, 8)
print(numbers)

# del statement can permanently deletes the element from the list if we know it's index.
del numbers[1]

# pop() method removes the last item from the list but it let's you use the removed item's value.
popped_number = numbers.pop()
print(popped_number)

# We can even remove any position's item from the list by using the pop() method if we assign it's index to the pop() method.
numbers.pop(2)

# We can remove an item from the list if we only knwe it's value by using remove method.
numbers.remove('eight')

print(numbers)


movies = ['dhurandhar', 'interstellar', 'batman']

# sort() method sort the list in alphabetical order. It changes the list permanently.
movies.sort()

# We can also use sort method to sort our list permanently in reverse alphabetical order.
movies.sort(reverse=True)

# sorted() function also sort the list in alphabetical orde BUT it changes the list Temporarily.
print("Here is the original list:")
print(movies)

print("\nHere is the sorted list:")
print(sorted(movies))

# We can also sort list temporarily using reverse=True in sorted() method.
print(sorted(movies, reverse=True))

# We can easily work with list using python's for loop.
for movie in movies:
    print(movie)
# In this we create a variable called movie and assign the values of the list to it. It loops through the list till the last value of the list is also assigned to the variable movie.

# We can also prints statements with thw values of the list.
for movie in movies:
    print(f"{movie.title()}, this was such a great movie!")

print("I don't usually watch movies but these are ones I've watched many times") # This statement will be printed after the loop ends because it's written outside the whitespace of the for loop.


# range() function is used to create numerical lists. range() fuction follows off-by-one behaviour.
# To create list using range() finction we use list() function.
numbers = list(range(1, 7))
print(numbers)

# If we pass a third argument to the range() function then it will use that third argument to skip numbers in given range.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# we can use list comprehension to generate a list using one line of code that will combine many different things into just one line likefor loop ,range fuction and appending.
cubes = [value**3 for value in range(1, 11)]
print(cubes)


# We can also work with a part of a list by making a slice of it. To create a slice you define first and the last elements you want to work with. This also follows off-by-one behaviour.
actors = ['RDJ', 'chris', 'charles', 'scarlett']
print(actors[0:3])

print(actors[2:]) # it will start from index 2 and will go to the end of the list.
print(actors[:3]) # it will start from 0 and will go till index 2.
print(actors[-3:]) # it will print last three elements of the list.

# We can also loop through a slice.
for actor in actors[:2]:
    print(actor.title())

# We can copy a list and create another one by using [:]
copy_list = actors[:]
copy_list.append('vishal')

print(actors)
print(copy_list)
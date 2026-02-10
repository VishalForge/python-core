''' 
Chapter - 6
Source - Python Crash Course Book

'''

#----- Dictionary Basics & Access --------
person_details = {'name' : 'Roy', 'age' : 21, 'city' : 'gobi', 'favorite_anime' : 'dororo'}

print(person_details['name'])
print(person_details['age'])
print(person_details['city'])
print(person_details['favorite_anime'])

print(f"Person's details are:\nname: {person_details['name']}\nage: {person_details['age']}\ncity: {person_details['city'].title()}\nfavorite anime: {person_details['favorite_anime'].title()}")


# Avoiding keyerror using get() method

# print(person_details['occupation'])  # This will generate a KeyErrror
print(person_details.get('occupation', 'No occupation key exist'))





# ----- Adding & Modifying Key-Value pairs -----
employee_credentials = {}

employee_credentials['name'] = 'Sam'
employee_credentials['role'] = 'Data_scientist'
employee_credentials['age'] = 24
employee_credentials['salary'] = '120K'

print(employee_credentials)

employee_credentials['salary'] = '140K'

print(employee_credentials)


# Conditional modification
game = {'name' : 'GTA_5', 'status' : 'Inactive'}

if game['status'] == 'Inactive':
    game['status'] = 'Active'
elif game['status'] == 'Active':
    print("The game is active")

print(game['status'])




#------Removing Key-Value pairs------

user = {'name' : 'luffy', 'age' : 21, 'rank' : 'platinum', 'gems' : '2K'}

print(user)

del user['age']
print(user.get('age', 'key does not exist'))



#-----Looping through Dictionaries------

# Using items() method to loop through Keys & Values
favorite_anime = {
    'jack':'dragon_ball',
    'olivia':'demon_slayer',
    'oggy':'one_piece'
    }

for name, anime in favorite_anime.items():
    print(f"\nSo, your name is : {name.title()}")
    print(f"And your favorit anime is : {anime.title()}")


# Using keys() to loop through keys
for name in sorted(favorite_anime.keys()):
    print(f"{name}, you have taken the poll!")


# Using values() and set to loop through all the Values in a dictionary
favorite_movies = {
    'jack':'titanic',
    'sam':'titanic',
    'roy':'god_father',
    'vish':'interstellar'
    }

print("These are the mentioned movies:")
for movies in set(favorite_movies.values()):
    print(movies)



#----List as dictionary values
attributes = {
    'goku': ['martial arts', 'hakai', 'ui', 'flight'],
    'saitama': ['super strength', 'baldness']
    }

for character, abilities in attributes.items():
    print(f"\n{character.title()}'s abilities are:")
    for ability in abilities:
        print(f"\t{ability.title()}")

    if 'flight' in abilities:
            print("\tThat's amazing")



#-----List of dictionaries-----
character_1 = {'name':'goku', 'universe':'dragon_ball', 'power_level':500000}
character_2 = {'name':'saitama', 'universe':'one_punch', 'power_level':450000}

profiles = [character_1, character_2]

for profile in profiles:
    if profile['power_level'] >= 500000:
        print(f"{profile['name'].title()}: You are very strong!")
    if profile['power_level'] >= 450000:
        print(f"{profile['name'].title()}: You are close to Goku!")



#-----Nested Dictionaries------
users = {
    'ninja' : {'email': 'abc@gmail.com', 'location': 'japan', 'age':23},
    'fang yuan' : {'email': 'xyz@gmail.com', 'location': 'ri', 'age':550}
    }

for username, info in users.items():
    print(f"{username.title()}'s details are:")
    print(f"\temail: {info['email']}\n\tlocation: {info['location'].title()}\n\tage: {info['age']}")

users['fang yuan'] ['location'] = 'northern plains'
print(f"New location: {users['fang yuan'] ['location']}")

# Defensive lookup for optional nested data
print(f"Power level of Fang Yuan: {users.get('fang yuan', {}).get('power level', 'key does not exist')}")




#-----Realistic Mini-Scenario------
languages = {
    'jack':'python',
    'rose':'c++',
    'sam':'java',
    'alex':'go'
    }

for name, language in languages.items():
    print(f"{name.title()} voted for {language.title()}")

if 'sam' not in languages:
    print("Sam, take our poll!")
"""
Lesson 6: Functions
Chapter 8
- Defining a function using def
- Calling a function
- Passing information to a function through arguments
- Return values from a function using return
- Avoiding errors with functions
- Exercise 8-3. and 8-4. : make_shirt()
- Exercise 8-5. : describe_pet()
This file is a module that contains functions that can be imported and used in other files. It is not meant to be run as a standalone program. The functions defined in this file can be imported and used in other files, such as lesson6_functions.ipynb, to demonstrate how to use functions in Python.
"""

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")  


# --- Exercise 8-3. and 8-4. ---
def make_shirt(message,size = "L"):
    """Print the size of the shirt and the message on it."""
    print(f"\nThe size of the shirt is {size}.")
    print(f"The message on the shirt is \t'{message}'.")


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name: # make the middle name optional
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# --- Exercise 8-6 ---
def city_country(city,country):
    """Return a string of the form 'City, Country'."""
    formatted_city_country = f"{city}, {country}"
    return formatted_city_country.title()


# --- Exercise 8-7 ---
def make_album(artist_name,album_title,number_of_tracks=''):
    """Return a dictionary of information about an album."""
    album ={
        'artist_name':artist_name,'album_title':album_title,
    }
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album


# Pasing a list to a function
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)



# Modifying a list in a function and the list is permanently modified.
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# --- Exercise 8-9., 8-10. and 8-11. ---
def show_magicians(names):
    """Print the name of the magician in the list."""
    for name in names:
        print(name.title())


def make_great(names):
    """Add 'the Great' to each magician's name in the list. Modify the list of names in place."""
    for i in range(len(names)):
        names[i] = 'the Great ' + names[i]


# --- Exercise 8-11. ---
def make_new_great(names):
    """Add 'the Great' to each magician's name in the list. Return a new list with the changes."""
    return [f"the Great {name}" for name in names]



## mixing positional and arbitrary arguments
def make_pizza(size,*toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


# using arbitrary keyword arguments **extra_info for key = value pairs
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


# --- Exercise 8-12. --- 
def sandwich(*items):
    print("The sandwich is ordered with the following ingredients")
    for item in items:
        print("-" + item)


# --- Exercise 8-14. ---
def car_info(manufacturer, model, **other_info):
    """Store information about a car in a dictionary and return it."""
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    car.update(other_info) # use update({key-value pairs}) to add the other_info dictionary to the car dictionary.
    return car


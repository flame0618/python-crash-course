"""
Lesson 4: Python Basics from Crash Course by Eric Matthes 
Chapter 6
Topics:
- dictionaries
- Nesting: a list of dictionaries, a list in a dictionary, a dictionary in a dictionary
- Exercise 6-1. to 6-11.  
"""
def main(): 
    # Define a dictionarey 
    alien_0 = {'color':'green','points':5}
    print(alien_0['color'])
    print(alien_0['points'])
    new_points = alien_0['points']
    print(f"you just earned {new_points} points!")

    # Modify values in a dictionary
    alien_0['color'] = 'yellow'
    print(f"The alien is now {alien_0['color']}.")

    # Add new key-value pair 
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    print(alien_0)

    #  Moving an alien using dictionary
    ## Define an empty dictionary and add key-value
    alien_0 = {}
    alien_0['x_position'] = 0
    alien_0['y_position'] = 25
    alien_0['speed'] = 'medium'
    alien_0['points'] = 5
    print(f"\nOrigional x-position: {alien_0['x_position']}")
    ## Move the alien to the right. 
    ## Determin how far to move the alien based on its current speed. 
    if alien_0['speed'] == 'slow':
        x_increment = 1
    elif alien_0['speed'] == 'medium':
        x_increment = 2
    else: 
        ## This must be a fast alien
        x_increment = 3
    ## New position is the old x_position + x_increment
    alien_0['x_position'] += x_increment
    print(f"New x-position: {alien_0['x_position']}")

    # Removing Key-Value pairs
    print(alien_0)
    del alien_0['points']
    print(f"del alien_0['points'] deletes a pair: \n{alien_0}")

    # Stying: Need more than one line to define a dictionary, 
    # press enter after the opening brace. 
    favourite_languages = {
        'jen':'python',
        'sarah':'c',
        'edward':'ruby',
        'phil':'python'
    }
    print(f"Sarah's favourite language is {favourite_languages['sarah'].title()}")
    # Breaking long print statement to increase readability.
    print(f"Jen's favourite language is" 
        f"{favourite_languages['jen'].title()}.")


    # --- Exercise 6-1. to 6-4. ---
    amis_kohls = {}
    amis_kohls['first_name'] = 'kohls'
    amis_kohls['last_name'] = 'noord'
    amis_kohls['age'] = 28
    amis_kohls['height'] = 165 
    amis_kohls['city'] = 'kyoto'
    print(amis_kohls)
    python_glossary = {
        'string':'a series of words',
        'list':'a collection of items in numerical order',
        'dictionary':'a collection of items in key-value pairs',
        'loop':'a block of code that repeats',
        'if statement':'a block of code that executes if the condition is True',
        'boolean':'a value that can be either True or False',
        'styling':'make your code readable and beautiful'
    }
    print(python_glossary)
    # Looping through a dictionary
    for word, definition in python_glossary.items():
        print(f"\n Key: {word.title()} \n Value: {definition}")

    # Looping through a dictionary to print only keys or values
    # dictionary.items() method returns a list of key-value pairs.
    # dictionary.keys() method returns a list of keys.
    # dictionary.values() method returns a list of values.
    print(amis_kohls.items())
    print(amis_kohls.keys())
    print(amis_kohls.values())
    # loop through a dictionary to print only keys or values
    for k,v in amis_kohls.items():
        print(f"\nKey: {k} \nValue: {v}")
    # dictionary.keys() method returns a list of keys in the dictionary.  
    for k in amis_kohls.keys():
        print(f"Key: {k}")

    if 'erin' not in favourite_languages.keys():
        print("\nErin, please take our poll!")

    # Sorting a dictionary by keys or values
    ## sorted() function returns a sorted list of the specified iterable object.
    for name in sorted(favourite_languages.keys()):
        print(f"{name.title()}, thank you for taking the poll.")
    ## To get a list of values without duplicates, use set() function to remove duplicates.
    for language in set(favourite_languages.values()):
        print(language)

    # --- Exercise 6-5. ---
    rivers= {'nile':'egypt', 'amazon':'brazil', 'yangtze':'china','long':'china'}
    for river, country in rivers.items():
        print(f"The {river.title()} runs through {country.title()}")
    print("The rivers in the dictionary are:")
    for river in sorted(rivers.keys()):
        print(river.title())
    print("The countries in the dictionary are:")
    for country in sorted(set(rivers.values())):
        print(country.title())
    # --- Exercise 6-6. ---
    names = ['sarah', 'phil', 'jen', 'edward', 'erin','kohls']
    for name in names:
        if name in favourite_languages.keys():
            print(f"{name.title()} thanks you for talking the poll.")
        else:
            print(f"{name.title()} please take the poll")

    # Nesting:  a list of dictionaries
    alien_0 = {'color':'green','points':5}
    alien_1 = {'color':'yellow','points':10}
    alien_2 = {'color':'red','points':15}
    aliens = [alien_0, alien_1, alien_2]
    print(aliens)
    for alien in aliens:
        print(alien)

    ## making a list of 30 aliens
    aliens = []
    for alien_number in range(30):
        new_alien = {'color':'green','points':5, 'speed':'slow','number':alien_number}
        aliens.append(new_alien)
    ### show the first 5 aliens
    for alien in aliens[:5]:
        print(alien)
    print("...")
    ### show how many aliens have been created
    print(f"The total number of aliens: {len(aliens)}")

    ### modify aliens
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'medium'
            alien['points'] = 10
    ### show the first 5 aliens
    for alien in aliens[:5]:
        print(alien)
    print("...")

    # Nesting:  a list in a dictionary
    ## store information about a pizza being ordered. 
    pizza = {
        'crust':'thick',
        'toppings':['mushrooms','extra cheese'],
    }
    ## summarize the order. 
    print(f"You ordered a {pizza['crust']} crust pizza" 
        f"with the following toppings: "
        )
    for topping in pizza['toppings']:
        print(f"\t{topping}")

    favourite_languages = {
        "jen":['python','ruby'],
        'sarah':['c'],
        'edward':['ruby','c'],
        'phil': ['python','haskell']
    }

    ## multiple prefered languages
    for name, languages in favourite_languages.items():
        print(f"\n{name.title()}'s favourites are:")
        for language in languages:
            print(f"\t {language.title()}")

    # nesting: a dictionary in a dictionary
    users = {
        'aeinstien': {
            'first':'albert',
            'last':'einstein',
            'location':'princeton',
        },
        'mcurie': {
            'first':'marie',
            'last':'curie',
            'location':'paris',
        },
    }
    for username, user_info in users.items():
        print(f"\nUsername: {username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']
        print(f"Full name: {full_name.title()}"
            f"\nLocation: {location.title()}")
        
    # --- Exercise 6-7. ---
    amis_alice = {}
    amis_alice['first_name'] = 'alice'
    amis_alice['last_name'] = 'fond'
    amis_alice['age'] = 39
    amis_alice['height'] = 160 
    amis_alice['city'] = 'belgium'

    amis_eddie = {}
    amis_eddie['first_name'] = 'eddie'
    amis_eddie['last_name'] = 'jos'
    amis_eddie['age'] = 90
    amis_eddie['height'] = 180 
    amis_eddie['city'] = 'austrilia'

    amis_kohls = {}
    amis_kohls['first_name'] = 'kohls'
    amis_kohls['last_name'] = 'noord'
    amis_kohls['age'] = 28
    amis_kohls['height'] = 165 
    amis_kohls['city'] = 'kyoto'

    people = [amis_alice,amis_eddie,amis_kohls]

    for ami in people:
        print("\n")
        for k,v in ami.items():
            print(f"{k.title()}:{str(v).title()}")

    # --- Exercise 6-8. ---

    dog = {
    'owner':'alice',
    'age': 5,
    'breed':'labrador',
    }
    cat = {
    'owner':'eddie',
    'age': 3,
    'breed':'persian',
    }
    rabbit = {
    'owner':'kohls',
    'age': 2,
    'breed':'netherland dwarf',
    }
    pets = [dog, cat, rabbit]
    for pet in pets:
        print("\n") 
        for k,v in pet.items():
            print(f"{k.title()}:{str(v).title()}")

    # --- Exercise 6-9. ---
    print("I skip exercise 6-9, since it is similar to exercise 6-8.")
    # --- Exercise 6-10. ---
    print("I skip exercise 6-10, since it is similar to exercise 6-8.")
    # --- Exercise 6-11. ---
    cities = {
        'tokyo':{
            'country':'japan',
            'population': 37_000_000,
            'fact':'the largest metropolitan area in the world',
        },
        'paris':{
            'country':'france',
            'population': 11_000_000,
            'fact':'the city of love',
        },
        'kyoto':{
            'country':'japan',
            'population': 1_500_000,
            'fact':'the city of ten thousand shrines',
        },
    }
    for city, info in cities.items():
        print(f"\nThe info about {city.title()} is as follows")
        for k,v in info.items():
            print(f"{k.title()}: {v}")

if __name__ == "__main__":
    main()
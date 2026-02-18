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
"""
import lesson6_functions_module as l6

def main():
    l6.describe_pet('willie')
    l6.describe_pet(pet_name='harry', animal_type='hamster')

    l6.make_shirt('I love Python')
    l6.make_shirt(size='M', message='Python is great!')
    l6.make_shirt(message='Python is my favorite language.', size='S')

    musician1 = l6.get_formatted_name('jimi', 'hendrix')
    musician2 = l6.get_formatted_name('john', 'hooker', 'lee')
    print(musician1)
    print(musician2)

    musician1 = l6.build_person('jimi', 'hendrix')
    musician2 = l6.build_person('john', 'hooker', age=91)
    print(musician1)
    print(musician2)

    # This is an infinite loop!
    while True:
        print("\nPlease tell me your name:")
        f_name = input("First name (enter 'q' to quit at anytime.): ")
        if f_name == 'q':
            print("Quit requested")
            break
        l_name = input("Last name (enter 'q' to quit at anytime.): ")
        if l_name == 'q':
            print("Quit requested")
            break
        formatted_name = l6.get_formatted_name(f_name,l_name)
        print(f"\nHello, {formatted_name}!")

    print(l6.city_country('santiago', 'chile'))
    print(l6.city_country('paris', 'france'))
    print(l6.city_country('tokyo', 'japan'))

    print(l6.make_album('the beatles', 'abbey road'))
    print(l6.make_album('pink floyd', 'the dark side of the moon', number_of_tracks=10))

    # --- Exercise 8-8 ---
    while True:
        artist_name = input("1. Artist name (enter q to quit anytime): ")
        if artist_name.lower() == 'q': # allow Q and q to quit.
            print("Quit requested")
            break
        album_title = input("2. Album title (enter q to quit anytime): ")
        if album_title.lower() == 'q': 
            print("Quit requested")
            break
        album = l6.make_album(artist_name,album_title)
        print(album)

    usernames = ['hannah', 'ty', 'margot']
    l6.greet_users(usernames)

    

    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []

    ## by define two functions, the main part of the code is cleaner and easier to read and easy to change.
    l6.print_models(unprinted_designs, completed_models)
    l6.show_completed_models(completed_models)
    print(f"unprinted_designs: {unprinted_designs}")
    print(f"completed_models: {completed_models}")

    # preventing a function from modifying a list by passing a copy of the list to the function.
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
    completed_models = []
    l6.print_models(unprinted_designs[:], completed_models) # the slice notation [:] makes a copy of the list to pass to the function.
    l6.show_completed_models(completed_models)
    print(f"unprinted_designs: {unprinted_designs}")
    print(f"completed_models: {completed_models}")    

    magicians = ['alice', 'david', 'carolina']
    l6.show_magicians(magicians)
    l6.make_great(magicians)
    l6.show_magicians(magicians)

    magicians = ['alice', 'david', 'carolina']
    great_magicians = l6.make_new_great(magicians) # The function make_new_great() does not modify the original list magicians, but returns a new list great_magicians with the changes. so no [:] is needed when passing magicians to make_new_great(). 
    l6.show_magicians(magicians)
    l6.show_magicians(great_magicians)

    l6.make_pizza(16, 'pepperoni')
    l6.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    user_profile = l6.build_profile('albert', 'einstein', 
                             location='princeton', 
                             field='physics')
    print(user_profile) 

    l6.sandwich('lettuce', 'tomato', 'ham', 'cheese')

    car = l6.car_info('subaru', 'outback', color='blue', tow_package=True)
    print(car)
    
if __name__ == "__main__":
    main()
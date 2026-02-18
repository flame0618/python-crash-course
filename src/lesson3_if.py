"""
Lesson 3: If Statements
Topics:
- if statements
- if-elif-else chain
- Using multiple lists in if statements
- Checking that a list is not empty
- Using if statements with lists
- Exercise 5-1. to 5-11. in Chapter 5 of Crash Course by Eric Matthes   
"""

def main():
    pizzas = ['Pepperoni', 'Mushroom', 'Sausage', 'Pineapple']
    print('Mushroom' in pizzas)
    print('Olives' not in pizzas)

    # --- Exercise 5-1. and 5-2. Conditional Tests ---
    bike = 'Trek'
    print(f"Is bike == 'Trek'? I predict True. {bike == 'Trek'}")
    print(f"Is bike == 'Scott'? I predict False. {bike == 'Scott'}")
    numbers = [i for i in range(1, 11)]
    print(f"Is 5 in numbers? I predict True. {5 in numbers}")
    print(f"Is 15 bigger than any number in numbers? {15 > max(numbers)}")
    print(f"Is 10 less or equal than any number in numbers? {10 <= min(numbers)}")
    print (f"Is 10 not in numbers?  {10 not in numbers}")

    # --- Exercise 5-3. to 5-5. --- 
    alien_color = ['green', 'yellow', 'red']
    for color in alien_color:
        if color == 'green':
            print('You just earned 5 points!')
        elif color == 'yellow':
            print('You just earned 10 points!')
        else:
            print(f"You just failed. The alien color is {color}")

    # --- Exercise 5-6. ---
    age = 25
    if age < 2:
        print('The person is a baby.')
    elif age < 4:
        print('The person is a toddler.')
    elif age < 13:
        print('The person is a kid.')
    elif age < 20:
        print('The person is a teenager.')
    elif age < 65:
        print('The person is an adult.')

    # --- Exercise 5-7. ---
    favourite_fruits = ['apple', 'banana', 'orange']
    test_fruits = ['apple', 'grape', 'orange', 'watermelon', 'banana']
    for fruit in test_fruits:
        if fruit in favourite_fruits:
            print(f"You really like {fruit}!")

    # if statements with lists
    requested_toppings = ['mushrooms','green peppers','extra cheese']
    for topping in requested_toppings:
        if topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")  
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")

    # Checking that a list is not empty
    requested_toppings = []
    if requested_toppings:
        for topping in requested_toppings:
            print(f"Adding {topping}.")
        print("\nFinished making your pizza!")
    else:
        print("Requested_toppings is empty. \nAre you sure you want a plain pizza?")

    # Using multiple lists 
    available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
    requested_toppings = ['mushrooms','french fries','extra cheese']
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
    print("\nFinished making your pizza!")

    # --- Exercise 5-8. to 5-10.--- 
    usernames = ['admin', 'edward', 'alice', 'bob', 'charlie']
    usernames =[]
    if usernames:
        for username in usernames:
            if username == 'admin':
                print("Hello admin would you like to see a status report?")
            else:
                print(f"Hello {username.title()}, thank you for logging in again.")
    else:
        print("We need to find some users!")
    current_users = ['admin', 'edward', 'alice', 'bob', 'charlie']
    new_users = ['david', 'Edward', 'frank', 'grace', 'henry']
    for new_user in new_users:
        if new_user.lower() in [user.lower() for user in current_users]:
            print(f"The username {new_user} is already taken. Please enter a new username.")
        else:
            print(f"The username {new_user} is available.")

    # --- Exercise 5-11. ---
    numbers = [i for i in range(1, 10)]
    for number in numbers:
        if number == 1:
            print(f"{number}st")
        elif number == 2:
            print(f"{number}nd")
        elif number == 3:
            print(f"{number}rd")
        else:
            print(f"{number}th")
if __name__ == "__main__":
    main()

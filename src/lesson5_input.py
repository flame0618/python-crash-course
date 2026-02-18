"""
Lesson 5: input() and while loops
Chapter 7

- Using the input() function to get user input
- Using while loops to repeat code as long as certain conditions are true
- Using break and continue in loops
"""
def price(age):
    if age < 3:
        print("The ticket is free")
    elif age < 12:
        print("The ticket is $10")
    else:
        print("The ticket is $15")

def main():
    name = input("Please enter your name: ")
    print(f"Hello, {name.title()}!")

    prompt = "If you tell us who you are, we can personalize the messages you see."
    prompt += "\nWhat is your first name? "
    name = input(prompt)
    print(f"\nHello, {name.title()}!")

    # while loops
    current_number = 1
    while current_number <= 5:
        print(5-current_number)
        current_number += 1

    promt = "\nTell me something, and I will repeat it back to you:"
    promt += "\nEnter 'quit' to end the program. "
    message = ""
    while message != 'quit':
        message = input(promt)
        if message != 'quit':
            print(message)

    # avoiding infinite loops
    '''
    x = 1
    while x <= 5:
        print(x)
    '''

    # --- Exercise 7-6. ---
    promt = "\nEnter your age and I will tell you the ticket price:"

    # use try-except block to catch the error safely
    try: 
        while True:
            age = input(promt)
            age = int(age)
            price(age)
    except ValueError:
        print(f"The input '{age}' is not an age")

    # --- Exercise 7-8. ---
    sandwich_orders = ['tuna', 'turkey', 'ham', 'chicken']
    finished_sandwiches = []
    while sandwich_orders:
        current_sandwitch = sandwich_orders.pop()
        print(f"I am making your {current_sandwitch} sandwich.")
        finished_sandwiches.append(current_sandwitch)
    print("\nThe following sandwiches have been made:")
    for finished_sandwitch in finished_sandwiches:
        print(finished_sandwitch)

    # --- Exercise 7-9. ---
    sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ham', 'pastrami', 'chicken']
    print("Sorry, we are out of pastrami today.")
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    print(sandwich_orders)

    # --- Exercise 7-10. ---
    responses = {}
    polling_active = True

    while polling_active:
        name = input("\nWhat is your name? ")
        response = input("If you could visit one place in the world, where would you go? ")

        responses[name.lower()] = response.lower()

        repeat = input("Would you like to let another person respond? (yes/no) ")
        if repeat != 'yes':
            polling_active = False
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name.title()} would like to visit {response.title()}.")
    

if __name__ == "__main__":
    main()
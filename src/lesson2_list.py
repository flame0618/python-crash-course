"""
Lesson 2: Python Basics from Crash Course by Eric Matthes 
Chapter 3-4

Topics:
- lists
- loops and list comprehensions
- Copy a list by slicing
"""
def main():
    # --- modification of guest list Exercise 3-4. to  3-7.---
    guests = ['kolin', 'christ', 'sarah', 'lisa']
    guests[:] = [guests[i].title() for i in range(len(guests))]
    for i in range(len(guests)):
        print(f"Bonjour {guests[i]}, aimeriez-vous dîner avec moi ce soir?")
    print(f"Malheureusement, {guests.pop(0)} ne peut pas venir ce soir.")
    print(f"The list of the guests is now: {guests}.")
    for i in range(len(guests)):
        print(f"Bonjour {guests[i]}, nous peut adapter à une table plus grande, allors, nous allons inviter plus de gens.")
    guests.insert(0, 'franklin')
    guests.insert(2, 'vlad')
    guests.append('maria')
    guests[:] = [guests[i].title() for i in range(len(guests))]
    print(f"The list of the guests is now: {guests}.")
    for i in range(len(guests)):
        print(f"Bonjour {guests[i]}, aimeriez-vous dîner avec moi ce soir?")
    print("Malheureusement, je ne peux inviter que deux personnes pour le dîner ce soir.")
    while len(guests) >2:
        print(f"Bonjour {guests.pop()}, Je suis désolé, mais je ne peux pas inviter vous à dîner ce soir.")
    for i in range(len(guests)):
        print(f"Bonjour {guests[i]}, vous êtes toujours invité à dîner avec moi ce soir.")
    del guests[:]
    print(f" det guests[:] gives {guests}")

    # --- Exercise 3-8. to  3-10.---
    places = ['paris', 'london', 'new york', 'tokyo', 'sydney']
    places[:] = [places[i].title() for i in range(len(places))]
    print(f"Original list: \n{places}")
    print(f"Sorted list using sorted(): \n{sorted(places)}")
    print(f"Original list is not changed: \n{places}")
    print(f"Sorted list using sorted(,reverse=True): \n{sorted(places, reverse=True)}")
    print(f"Original list is not changed: \n{places}")
    places.reverse()
    print(f"Reverse list using reverse() and the original list is changed: \n{places}")
    places.reverse()
    print(f"Reverse list using reverse() again and the original list is changed back: \n{places}")
    places.sort()
    print(f"Sorted list using sort() and the original list is changed: \n{places}")
    places.sort(reverse=True)
    print(f"Sorted list using sort(,reverse=True) and the original list is changed: \n{places}")
    print(f"The number of cities is {len(places)}")
    print("Exercise 3-10 is boring and I skipped it.")

    # --- loops and list comprehensions ---
    for place in places:
        print(f"I would like to visit {place}.")
    print(f"for place in places, this line is not indented: \n print(place): {place}.")

    # --- Exercise 4-1. ---
    pizzas = ['pepperoni', 'mushroom', 'pineapple']
    for pizza in pizzas:
        print(f"I like {pizza} pizza.")
    print("I really love pizza!")

    # --- Making numerical lists with the range() function ---
    # --- Exercise 4-4. ---
    one_million = [i for i in range(1,1000001)]
    print(f" check the list starts with 1 and ends with 1m:\n{min(one_million)}, {max(one_million)}")
    # --- Exercise 4-5. ---
    print(f"sum from 1 to 1m: {sum(one_million)}")
    # --- Exercise 4-6. ---
    odd_numbers = [i for i in range(1,5,2)]
    for odd_number in odd_numbers:
        print(odd_number)
    # --- Exercise 4-7. ---
    mutiples_of_3 = [i for i in range(3,31,3)]
    print(mutiples_of_3)
    # --- Exercise 4-8. ---
    cubes = [i**3 for i in range(1,11)]
    print(cubes)

    # --- Copy a list by slicing ---
    my_foods = ['pizza', 'falafel']
    friend_foods = my_foods[:]
    friend_foods.append('ice cream')
    print(f"My favorite foods are: {my_foods}")
    print(f"My friend's favorite foods are: {friend_foods}")
    print("without slicing in the following code, the two lists will be the same \n because they point to the same list in memory.")
    friend_foods = my_foods
    friend_foods.append('ice cream')
    print(f"My favorite foods are: {my_foods}")
    print(f"My friend's favorite foods are: {friend_foods}")

if __name__ == "__main__":
    main()    
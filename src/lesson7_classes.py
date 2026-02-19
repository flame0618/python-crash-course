
from random import randint
from collections import OrderedDict

import lesson7_modules as l7
# defining a class
class Dog(): # Capitalized class name by convention
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age): # Python runs this method automatically when we create a new instance of Dog
    # self is a reference to the instance being created.
        """Initialize name and age attributes."""
        self.name = name # create an attibute that is global to the class
        self.age = age # Any variable prefixed with self is available to every method in the class, and is then attached to the instance being created.
        
    def sit(self): # create a method
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self): # Instance method must have self as its first parameter.
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


class Die():
    """A model of perfect die"""
    def __init__(self,sides=6):
        """one arttibute sides of a die"""
        self.sides = sides
    
    def roll_die(self):
        """roll the die and show the number of the side that is upfront"""
        print(randint(1,self.sides)) # Use the randint() function to generate a random integer between 1 and the number of sides on the die (inclusive). 


def main():
    my_dog = Dog('Willie', 6) # Create an instance of the Dog class and assign it to the variable my_dog. We pass 'Willie' and 6 as arguments to the __init__ method, which initializes the name and age attributes of the my_dog object.

    # Accessing Attributes
    print(f"My dog's name is {my_dog.name}.") 
    print(f"My dog is {my_dog.age} years old.") 

    # Calling Methods
    my_dog.sit() # Call the sit() method of the my_dog object.
    my_dog.roll_over() # Call the roll_over() method of the my_dog object

    my_new_car = l7.Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())

    my_new_car.read_odometer()
    my_new_car.update_odometer(23)
    my_new_car.read_odometer()
    my_new_car.increment_odometer(10)
    my_new_car.read_odometer()  

    my_tesla = l7.ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()

    # --- Exercise 9-11. ---
    admin_user = l7.Admin("edward", "smith")
    admin_user.describe_user()
    admin_user.privileges.show_privileges()

    favorite_languages = OrderedDict()
    favorite_languages['jen'] = 'python'
    favorite_languages['sarah'] = 'c'
    favorite_languages['edward'] = 'ruby'
    favorite_languages['phil'] = 'python'  

    for name, language in favorite_languages.items():
        print(f"{name.title()}'s favorite language is {language.title()}.")

    die = Die()
    print(f"defaut die with {die.sides} sides")
    die.roll_die()
    die.roll_die()
    die.roll_die()
    die.roll_die()

    die10 = Die(10) 
    print(f"Die with {die10.sides} sides")
    die10.roll_die()
    die10.roll_die()
    die10.roll_die()
    die10.roll_die()

    die20 = Die(20) 
    print(f"Die with {die20.sides} sides")
    die20.roll_die()
    die20.roll_die()
    die20.roll_die()
    die20.roll_die()

if __name__ == "__main__":
    main()
from lesson7_modules_super import *

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """A statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        """Exercise 9-9. check the battery size and set the capacity to 85 if not already"""
        if self.battery_size >= 85:
            print(f"The battery is healthy no need to change")
        else:
            self.battery_size = 85
            print(f"The battery is changed to 85.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric cars."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make,model,year)
        self.battery = Battery() # Create an instance of the Battery class as an attribute of the ElectricCar class
    
    def get_car_range(self): # Locate the method under ElectricCar() or Battery()? How to represent the real world in code?
        """Print a statement about the range this battery provides."""
        if self.battery.battery_size == 75:
            range = 260
        elif self.battery.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


class IceCreamStand(Restaurant):
    """A simple model for a ice cream stand as a kind of restaurant"""

    def __init__(self, name, cuisine_type, flavors=None):
        """Initilize the arttibutes"""
        super().__init__(name,cuisine_type)
        self.flavors = flavors if flavors is not None else []

    def describe_flavors(self):
        """print the flavors"""
        print(f"The ice cream shop {self.name} has the following flavors: ")
        print(", ".join(self.flavors)) # Join the list of flavors into a single string with commas separating each flavor.


class Privileges():
    """A simple model to list privileges"""

    def __init__(self,privileges=None):
        """Initialize the attributes"""
        self.privileges = privileges if privileges is not None else ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """print the privileges of an Admin"""
        print("The privileges are: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """model admin as a special user"""

    def __init__(self, first_name, last_name):
        """Initialize the arttibutes of an Admin"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
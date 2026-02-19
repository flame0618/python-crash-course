"""This file contains the classes and functions used in lesson 7: classes and object-oriented programming."""

"""A class that can be used to represent a car."""
class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles < 0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles  

# Instance as an Attribute
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

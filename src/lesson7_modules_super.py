class Restaurant():
    """Model a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize restaurant name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print information about the restaurant."""
        article = 'an' if self.cuisine_type[0].lower() in 'aeiou' else 'a'
        print(f"{self.name.title()} is {article} {self.cuisine_type.title()} restaurant.")

    def open_restaurant(self):
        """Print a message that the restaurant is open."""
        print(f"The restaurant {self.name.title()} is open.")


class User():
    """Model a user."""

    def __init__(self, first_name, last_name):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")


class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to descibe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Set a default value for an attribute

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
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
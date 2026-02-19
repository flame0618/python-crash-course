"""User classes."""
class User():
    """Model a user."""

    def __init__(self, first_name, last_name):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name.title()} {self.last_name.title()}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name.title()}! Welcome back.")
    
    def increment_login_attempts(self):
        """counting total login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """reset login_attemptes to be 0"""
        self.login_attempts = 0

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
# ===============================================
# Assignment 1: Design Your Own Class (Superhero)
# ===============================================

# 1. Parent Class: The base for our Superhero
class Person:
    """A general class for a person, to be inherited by other classes."""

    def __init__(self, name, age):
        """Initializes a Person with a name and age."""
        self.name = name
        self.age = age
        print(f"A new person named {self.name} has been created.")

    def introduce(self):
        """A method to introduce the person."""
        return f"Hi, my name is {self.name} and I am {self.age} years old."

# 2. Child Class: The Superhero class inherits from Person
class Superhero(Person):
    """
    A Superhero class that inherits from Person, adding powers and a superhero name.
    This demonstrates inheritance.
    """

    def __init__(self, name, age, superhero_name, superpower):
        # Call the parent class's constructor to initialize inherited attributes
        super().__init__(name, age)
        self.superhero_name = superhero_name
        self.superpower = superpower
        self._secret_identity = f"The true identity of {self.superhero_name} is {self.name}."  # Encapsulation with a "protected" attribute
        print(f"{self.superhero_name} is now ready to save the day!")

    def display_info(self):
        """A method to display the superhero's public information."""
        print(f"Superhero: {self.superhero_name}")
        print(f"Superpower: {self.superpower}")
        print("-" * 20)

    def reveal_identity(self):
        """A method to reveal the secret identity (accesses the 'protected' attribute)."""
        print(self._secret_identity)

# Create an instance of the Superhero class
print("--- Assignment 1 Output ---")
superman = Superhero("Clark Kent", 35, "Superman", "Flight and super strength")
print(superman.introduce())
superman.display_info()
superman.reveal_identity()


# ==================================================
# Assignment 2: Polymorphism Challenge (Vehicles)
# ==================================================

# 1. Base Class: A common blueprint for our vehicles
class Vehicle:
    """A base class for all vehicles with a common 'move' method."""
    def move(self):
        """This method will be overridden by child classes."""
        raise NotImplementedError("Subclass must implement abstract method.")

# 2. Child Class: Car
class Car(Vehicle):
    """A Car class that moves by 'driving'."""
    def move(self):
        """Overrides the parent's move method with a specific implementation."""
        return "The car is driving down the road. "

# 3. Child Class: Plane
class Plane(Vehicle):
    """A Plane class that moves by 'flying'."""
    def move(self):
        """Overrides the parent's move method with a specific implementation."""
        return "The plane is flying through the sky. "

# 4. Child Class: Boat
class Boat(Vehicle):
    """A Boat class that moves by 'sailing'."""
    def move(self):
        """Overrides the parent's move method with a specific implementation."""
        return "The boat is sailing across the sea. "

# Create a list of different vehicle objects
vehicles = [Car(), Plane(), Boat()]

# Iterate through the list and call the same 'move' method on each object
# The output will be different for each due to polymorphism.
print("\n--- Assignment 2 Output (Polymorphism) ---")
for vehicle in vehicles:
    print(vehicle.move())

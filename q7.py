
class Car:                                                              # Task 1: Define a class named Car
    def __init__(self, make, model, year):                              # Initialize attributes
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):                                             # Create a method
        print("Year Make Model: ", self.year, self.make, self.model)    # Print information about the car as "Year Make Model"

x = Car("Toyota", "Corolla", "2020")                  # Task 2: Create an instance
x.describe_car()                                                        # Task 2: Call describe_car method

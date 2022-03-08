# Class
# Attribute
# Method
# Object
# Inheritance

class car:
    # Create a class Constructor
    def __init__(self, year, mpg, speed, capacity) -> None:
    # attributes
        self.year = year        # car model's year
        self.mpg =  mpg         # mileage
        self.speed = speed      # current speed
        self.capacity = capacity 
    
    # methods
        def accelerate(self):
            return self.speed + 20

        def brake(self):
            return self.speed - 50
        
        def getCapacity(self):
            print("Car's capacity is " + self.capacity)



# Creating a object from class
car1 = car(2016, 20, 100)

# Setting methods for the object
car1.accelerate()
120
car1.brake()
50

# Inheritance
class Van(car):
    pass

    def isVan(self):
        return(True)
    
    




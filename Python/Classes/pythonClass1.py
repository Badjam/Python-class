class Robot:
    def __init__(self, name, color, weight): # This function represents the constructor of the class like in java programing language
# It is advisable as common practice to name the arguments in the same way the attributes
        self.name = name # name, color, weight are called attributes
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("My name is: "+ self.name)

# This is the default constructor for the class Robot
# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jery"
# r2.color = "blue"
# r2.weight = 40
# r2.name = "Barracuda" # This value (Barracuda) will be printed instead of the first assigned value which is 'Jery'



# r1.introduce_self()
# r2.introduce_self() # This will only print the last assigned value to the variable name which is 'Barracuda'

r1 = Robot("Tom", "red", 30)
r2 = Robot("Jery", "blue",40)

r1.introduce_self()
r2.introduce_self()
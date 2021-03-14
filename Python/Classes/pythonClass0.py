class Robot:
    def introduce_self(self):
        print("My name is: "+ self.name)
        
        
r1 = Robot()
r1.name = "Tom"
r1.color = "red"
r1.weight = 30

r2 = Robot()
r2.name = "Jery"
r2.color = "blue"
r2.weight = 40
r2.name = "Barracuda" # This value (Barracuda) will be overwrite the first assigned value which is 'Jery'



r1.introduce_self()
r2.introduce_self() # This will only print the last assigned value to the variable name which is 'Barracuda'

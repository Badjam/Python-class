'''Classes assignment '''

''' Please I do not understand very well the class and inheritance in python but in JAVA
I understand it perfectly. Please I need your help to understand the concept'''

class Vehicle:
    def __init__(self, Make = "Balin", Model ='Karas', Year = 1020, Weight = 1.5):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
    
    def NeedMaintenance(self,Maintenance =False):
        self.Maintenance = Maintenance
    
    
    
    def TripsSinceMaintenance(self, TripDistance = 0):
        self.TripDistance = TripDistance


class Cars(Vehicle):
    def __init__(self,Make, Model, Year, Weight):
        Vehicle.__init__(self,Make, Model, Year, Weight)
    
    def Drive(self,is_Driving = True):
        self.is_Driving =is_Driving
        
    
    def Stop(self, TripDistance, is_Driving = False):
        self.TripDistance = TripDistance
        self.is_Driving = is_Driving
        if self.is_Driving == False:
            self.TripDistance +=1
            if self.TripDistance >=100:
                Maintenance = True
            else:
                Maintenance = False
            
            return TripDistance
        else:
            TripDistance = 0
            return TripDistance
    
    def Repair(self,Maintenance = 0, TripDistance = False):
        self.Maintenance = Maintenance
        self.TripDistance = TripDistance




class Planes(Vehicle):
    def __init__(self, Maintenance =False):
        Vehicle.__init__(self, Maintenance)
        self.Maintenance = Maintenance
        
    
    def Flying(self, flying):
        self.flaying = flying
        if self.Maintenance == True:
            self.flaying = False
            return ("The plane can't fly until it's repaired.")
        else:
            self.flying = True
            return flying
        
    def Landing(self, landing):
        self.landing = landing



Range_Rover = Cars("Gondwana", "Barracuda", 1850, 5.8)
print(Range_Rover.Make)
print(Range_Rover.Model)
print(Range_Rover.Year)
print(Range_Rover.Weight)

Range_Rover.Drive(True)
print(Range_Rover.is_Driving)

Range_Rover.Stop(0)
print(Range_Rover.is_Driving)

Range_Rover.TripsSinceMaintenance(0)
print(Range_Rover.TripDistance)

Lexus = Cars("Boromo", "NGinging", 1780, 9.27)
print(Lexus.Make)
print(Lexus.Model)
print(Lexus.Year)
print(Lexus.Weight)

Lexus.Drive(False)
print(Lexus.is_Driving)

Lexus.Stop(1)
print(Lexus.is_Driving)

Lexus.TripsSinceMaintenance(0)
print(Lexus.TripDistance)


Benz = Cars("Tchop-Tchop", "Kalala", 1501, 12.90)
print(Benz.Make)
print(Benz.Model)
print(Benz.Year)
print(Benz.Weight)

Benz.Drive(False)
print(Benz.is_Driving)

Benz.Stop(1)
print(Benz.is_Driving)

Benz.TripsSinceMaintenance(0)

Jet = Planes(True)
Jet.Flying(False)
print(Jet.Flying(True))

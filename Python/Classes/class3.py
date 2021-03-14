class Team:
    def __init__(self, myTeamName, myTeamOrigin):
        self.TeamName = myTeamName
        self.TeamOrigin = myTeamOrigin
    
    
    
    def DefineTeamName(self, myTeamName):
        self.TeamName = myTeamName
    
    
    def DefineTeamOrigin(self, myTeamOrigin):
        self.TeamOrigin= myTeamOrigin


myTeam1 = Team("Chimen", "Gondwana")

myTeam2 = Team("Kalala", "Djoromican")

print(myTeam1.TeamName)

myTeam1.DefineTeamName("Barracuda")
print(myTeam1.TeamName)
print(myTeam1.TeamOrigin)

myTeam1.DefineTeamOrigin("Gondwana")
print(myTeam2.TeamName)

print(myTeam2.TeamOrigin)
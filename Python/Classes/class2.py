class Team:
    def __init__(self, Name, Origin):
        self.TeamName = "myTeamName"
        self.TeamOrigin = "myTeamOrigin"
    
    
    
    def DefineTeamName(self, myTeamName):
        self.TeamName = myTeamName
    
    
    def DefineTeamOrigin(self, myTeamOrigin):
        self.TeamOrigin= myTeamOrigin


myTeam = Team("Chimen", "Gondwana")

print(myTeam.TeamName)

myTeam.DefineTeamName("Barracuda")
print(myTeam.TeamName)
print(myTeam.TeamOrigin)

myTeam.DefineTeamOrigin("Gondwana")
print(myTeam.TeamOrigin)
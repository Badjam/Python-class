'''if stattement structure'''

# if condition:
#     Action
# print()


# Example 1

click = False
Like = 0
click = True
if click == True:
    Like = Like + 1
    click = False

# print(Like)


Temperature = 20
Thermo = 15
# print(Thermo)

if Temperature <= 15:
    Thermo = Thermo + 5

# print(Thermo)


if Temperature >= 20:
    Thermo = Thermo - 3
    
# print(Thermo)


Time = "Day"
Sleepy = False
Pajamas = "Off"

if Time == "Night" and Sleepy == True:
    Pajamas = "on"

# print(Pajamas)

Time = "Night"
Sleepy = True
Pajamas = "Off"

if Time == "Night" and Sleepy == True:
    Pajamas = "on"

print(Pajamas)



Time = "Night"
Sleepy = False
Pajamas = "Off"

if Time == "Night" and Sleepy == True:
    Pajamas = "on"

# print(Pajamas)



Time = "Day"
Sleepy = True
Pajamas = "Off"

if Time == "Night" or Sleepy == True:
    Pajamas = "on"

# print(Pajamas)


Time = "Day"
Sleepy = False
Pajamas = "Off"

if Time == "Night" or Sleepy == True:
    Pajamas = "on"

# print(Pajamas)



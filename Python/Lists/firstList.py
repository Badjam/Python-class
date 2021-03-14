# This is list in python 
Score = [90, 12, 34, 45, 20, 76]
#print(Score)

# Print element index 5
myList = [90, 12, 34, 45, 20, 76]
#print(myList[5])


# Access range of values from 0 - 4 not including 4
numbers = [90, 12, 34, 45, 20, 76]
#print(numbers[0:4])

# Access range of values from 4 - 6 not including 6
Score = [90, 12, 34, 45, 20, 76]
#print(Score[4:6])


# Access range of values from 3 to the end of the  list 
winning = [90, 12, 34, 45, 20, 76]
#print(winning[3:])


# Access range of values from the begening to the position 3 of the  list 
Score = [90, 12, 34, 45, 20, 76]
#print(Score[:3])


# Change the value of element indext 2 from 34 to 50 of the list 
Score = [90, 12, 34, 45, 20, 76]

Score[2] = 50
print(Score)


# Replace the value of elements indext 2 to 4 by an empty list 
Score = [90, 12, 34, 45, 20, 76]

Score[2:4] = []
print(Score)

# Replace the value of elements indext 1 to 3 by an a range values list 
Score = [90, 12, 34, 45, 20, 76]

Score[1:3] = [56, 78,25]
print(Score)

# access the last element of the list 
Score = [90, 12, 34, 45, 20.79, 76]

Score[-5]
print(Score)

# Insert string elements inside an integer list
hello = [90, 12, 34, 45, 20, 76]

hello[1:2] = ["Hello","World"]
print(hello)


# Insert a list inside a list
Score = [90, 12, 34, 45, 20, 76]

Score[2] = ["Hello","World"]
print(Score)


# Access an element of the list inside the main list
Score = [90, 12, 34, 45.9, 20, 76]

Score[2] = ["Hello", "World"]
print(Score)
print(Score[2][0])


# Add an element at the end of the list
Score = [90, 12, 34, 45, 20, 76]

Score.append(77)
print(Score)


# Add an string element at the end of the integer list
badjam = [90, 12, 34, 45, 20, 76]

badjam.append("Badjam")
print(badjam)


# Access the last element of the list 
Score = [90, 12, 34.7, 45, 20, 76]

print(Score[-5])


lis = [['a', 'b']]
print(lis[0][0])

lis = [['a', 'b']]
print(lis[-1][-1])
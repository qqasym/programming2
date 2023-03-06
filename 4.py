file = open("./404/4.py", "r")
Counter = 0
 
# Reading from file
Content = file.read()
CoList = Content.split("\n")
 
for i in CoList:
    if i:
        Counter += 1
 
print("This is the number of lines in the file")
print(Counter)
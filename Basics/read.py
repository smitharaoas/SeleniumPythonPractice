file = open('Test.txt')

#print(file.read())

#print(file.read(5))

#print(file.readline())


#print(file.readlines())

lineData = file.readline()

# while lineData!="" :
#     print(lineData)
#     lineData = file.readline()

for lineData in file.readlines() :
    print(lineData)


file.close()
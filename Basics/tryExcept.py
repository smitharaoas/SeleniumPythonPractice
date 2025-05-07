try :
    with open("file.txt","r") as reader:
        reader.read()
# print custom message in exception
except:
    print ("File does not exist")

try:
    with open("file.txt", "r") as reader:
        reader.read()
# print system generated message in exception
except Exception as e:
    print(e)
# With incorrect file name checking if finally is executed
finally:
    print("Test completed false")
# With correct file name checking if finally is executed
try:
    with open("Test.txt", "r") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Test completed True")
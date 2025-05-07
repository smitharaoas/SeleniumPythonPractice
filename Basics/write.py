with open('Test.txt','r') as reader:
    content = reader.readlines()
    print(content)
    with open('Test.txt','w') as writer:
        for line in reversed(content):
            print("Hello")
            print(line)
            writer.write(line)

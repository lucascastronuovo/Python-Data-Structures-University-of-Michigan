inp = input("Enter file name: ")

try:
    text = open(inp)
    textr = text.read()

    for line in text:
        line = line.rstrip()
        print(line.upper())

except:
    print("File cannot be opened: ", inp)
    quit()

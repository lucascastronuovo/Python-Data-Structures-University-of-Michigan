count = 0

fname = input("Enter file name: ")

text = open(fname)
textr = text.read()

for line in text:
    if not line.startswith("From"):
        continue

    if line.startswith("From:"):
        continue


    else:

        line = line.split()

        count = count + 1

        print(line[1])

print("There were", count, "lines in the file with From as the first word")

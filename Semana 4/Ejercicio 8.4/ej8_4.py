fname = input("Enter file name: ")

text = open(fname)
textr = text.read()


words1 = list()
words = list()
for line in text:
    line = line.strip()
    words = line.split()

    for i in words:
        if i not in words1:
            words1.append(i)

        else:
            continue

words1.sort()

print(words1)

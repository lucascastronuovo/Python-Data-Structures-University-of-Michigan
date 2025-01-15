fname = input("Enter file name: ")

text = open(fname)

hours = dict()
for line in text:
    if not line.startswith("From"):
        continue


    elif line.startswith("From:"):
        continue

    else:
        words = line.split()
        for word in words:
            if word.find(":") == -1:
                continue

            else:
                x = word.split(":")
                hour = x[0]
                hours[hour] = hours.get(hour, 0) + 1

lst = list()

for h, count in hours.items():
    lst.append((h, count))

lst = sorted(lst)

for key, value in lst:
    print(key, value)

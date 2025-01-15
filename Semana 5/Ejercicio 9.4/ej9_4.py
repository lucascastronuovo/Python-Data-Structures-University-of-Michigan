fname = input("Enter file name: ")

text = open(fname)

mails = dict()

for line in text:
    if not line.startswith("From:""):
        continue
    else:
        words = line.split()

        for word in words:
            if word.find("@") == -1:
                continue
            else:
                mails[word] = mails.get(word, 0) + 1

bmail = None
bcount = None

for mail,count in mails.items():
    if bcount is None or count > bcount:
        bcount = count
        bmail = mail
    else:
        continue

print(bmail, bcount)

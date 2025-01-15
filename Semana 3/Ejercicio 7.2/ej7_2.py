num2 = 0
total = 0
inp = input("Enter file name: ")

try:
    text = open(inp)
    textr = text.read()

    for line in text:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        total = total + 1
        prin = line.find("0.")

        numst = line[prin:]

        num1 = float(numst)
        num2 = num2 + num1

    average = num2 / total
    print("Average spam confidence:", average)

except:
    print("File cannot be opened: ", inp)
    quit()

text = "X-DSPAM-Confidence:    0.8475"

prin = text.find("0")

x = text[prin : ]

y = float(x)

print(y)

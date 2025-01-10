amount = int(input("Enter the amount of shifts:"))
try:
    text = input("Enter a text:")
    text = text.lower()
    text = list(text)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(text)):
        index = alphabet.index(text[i])
        text[i] = alphabet[(index + amount) % 26]
except:
    raise ValueError("Invalid input")
print("".join(text))
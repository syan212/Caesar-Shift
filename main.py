alphabet = "abcdefghijklmnopqrstuvwxyz"

try:
    amount = int(input("Enter the shift amount: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit(1)

text = input("Enter a text:").lower()
result = ""
for i, char in enumerate(text):
    if char not in alphabet:
        result += char
    else:
        result += alphabet[(alphabet.index(char) + amount) % 26]

print(result)

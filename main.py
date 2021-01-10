import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

var1 = []
for n in range(len(letters)):
  if n < nr_letters:
    var1.append(random.choice(letters))

var2 = []
for n in range(len(numbers)):
  if n < nr_numbers:
    var1.append(random.choice(numbers))

var3 = []
for n in range(len(symbols)):
  if n < nr_symbols:
    var1.append(random.choice(symbols))

var4 = var1 + var2 + var3

random.shuffle(var4)

var5=("".join(var4))
print(var5)
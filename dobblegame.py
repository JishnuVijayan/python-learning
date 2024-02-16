import string
import random

symbols = list(string.ascii_letters)
card_1 = [0] * 5
card_2 = [0] * 5

position_1 = random.randint(0, 4)
position_2 = random.randint(0, 4)

same_letter = random.choice(symbols)
symbols.remove(same_letter)

if position_1 == position_2:
    card_1[position_1] = same_letter
    card_2[position_2] = same_letter
else:
    card_1[position_1] = same_letter
    card_2[position_2] = same_letter
    alphabet_1 = random.choice(symbols)
    card_1[position_2] = alphabet_1
    symbols.remove(alphabet_1)
    alphabet_2 = random.choice(symbols)
    card_2[position_1] = alphabet_2
    symbols.remove(alphabet_2)

i = 0
while i < 5:
    if i != position_1:
        new_alphabet_1 = random.choice(symbols)
        card_1[i] = new_alphabet_1
        symbols.remove(new_alphabet_1)
    if i != position_2:
        new_alphabet_2 = random.choice(symbols)
        card_2[i] = new_alphabet_2
        symbols.remove(new_alphabet_2)
    i = i + 1

print(card_1)
print(card_2)

guess = input("Enter the same symbol: ")

if guess == same_letter:
    print("You are correct")
else:
    print("Wrong answer")

guess_count = 5
no_of_clues = 5
word = "BLUE WHALE"
guessed_word = ""
i = 1

clues = {
    1: "It's a animal",
    2: "It's a sea creature",
    3: "2 word",
    4: "It's Big",
    5: "Largest animal",
}

while guessed_word != word :
    if guess_count != 0:
        print ("Number of clues and Guess left is " + str(guess_count))
        print(clues.get(i))
        guessed_word = input("Enter the guess: ").upper()

        guess_count = guess_count - 1
        no_of_clues = no_of_clues -1
        i += 1
    else:
        print("Attempts are Over")

if guessed_word == word:
    print(word + " is the correct word")
else:
    print("Retry")
import random
words = ["python", "apple", "cat", "internship", "book"]

word = random.choice(words)

guessed = ""
chances = 6

print("Welcome to Hangman Game!")
print("Guess the hidden word")

while chances > 0:

    display = ""

    for letter in word:
        if letter in guessed:
            display = display + letter
        else:
            display = display + "_"

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You won!")
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed = guessed + guess
        print("Correct guess!")
    else:
        chances = chances - 1
        print("Wrong guess!")
        print("Chances left:", chances)

if chances == 0:
    print("\nGame Over!")
    print("The word was:", word)

import random

def choose_word():
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if set(word_to_guess) == set(guessed_letters):
                print("Congratulations! You've guessed the word:", word_to_guess)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts remaining.")

        print(display_word(word_to_guess, guessed_letters))

    if attempts == 0:
        print("Game over. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()

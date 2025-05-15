import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current snowman stage and the guessed letters.
    """
    #Display the snowman stage for the current number of mistakes.
    print("\n" + STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")


def play_game():
    """Runs the main game loop."""
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")

    mistakes = 0
    guessed_letters = []

    while mistakes < len(STAGES) - 1:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You saved the snowman!")
            return

    # If loop ends, player lost
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game Over! The word was: ", secret_word)
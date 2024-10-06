#Assignment 3: Hangman Game
import random

def words(file):
    with open(file,"r") as file:
        words = file.read().splitlines()
    return words

def random_words(words, length):
    for word in words:
        if len(word) == length:
            return random.choice(words)
        else:
            return None

def display_word_state(word, correct_guesses):
    for letter in word:
        if letter in correct_guesses:
            return " ".join(display_word_state)
        else:
            return "_" 
        
def draw_hangman(incorrect_guesses):
    stages = [
        """
          -----
          |   |
              |
              |
              |
              |
        --------
        """, """
          -----
          |   |
          O   |
              |
              |
              |
        --------
        """, """
          -----
          |   |
          O   |
          |   |
              |
              |
        --------
        """, """
          -----
          |   |
          O   |
         /|   |
              |
              |
        --------
        """, """
          -----
          |   |
          O   |
         /|\  |
              |
              |
        --------
        """, """
          -----
          |   |
          O   |
         /|\  |
         /    |
              |
        --------
        """, """
          -----
          |   |
          O   |
         /|\  |
         / \  |
              |
        --------
        """
    ]
    print(stages[incorrect_guesses])

def play_hangman():
    words = words("words.txt")

    if not words:
        print("word list is empty. Exiting the game.")

    word_length = int(input("enter the length og the word you would like to guess"))
    word = random_words(word, word_length)

    if not word:
        print("No words found in this length. Try again!")
        
    correct_guesses = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    guesses_letters = []

    print("Let's play Hangman!")
    print(display_word_state(word, correct_guesses))

    while incorrect_guesses < max_incorrect_guesses and set(correct_guesses) !=set(word):
        guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.is_alpya():
        print("Invalid input. Please enter a single letter.")
            
    if guess in guesses_letters:
        print("You have already guesses that letter.")
            
    guesses_letters.append(guess)

    if guess in word:
        correct_guesses.append(guess)
        print(f"Good guess!{guess} is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry, {guess} is not in the word.")

    draw_hangman(incorrect_guesses)
    print(display_word_state(word, correct_guesses))

    if set(correct_guesses) == set(word):
        print(f"Congradulations! You guesses the word: {word}")
    else:
        print(f"Game over! The word is: {word}")

if __name__ == "__main__":
    play_hangman()


        

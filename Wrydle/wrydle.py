import pathlib
import random

wordlist = pathlib.Path("wordlist.txt")

words = [
    word.upper()
    for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
]
word = random.choice(words)

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == word:
        print("Correct")
        break
    if guess == "":
        print("No guess entered")
        continue
    if len(guess) != len(word):
        print(f"Guess must be {len(word)} letters long")
        continue

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

    if guess_num == 6:
        print("Out of guesses. The word was:", word)
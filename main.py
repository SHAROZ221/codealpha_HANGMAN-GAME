"""
Hangman Game
-------------
Goal: A text-based Hangman game where the player guesses a word one letter at a time.

Simplified Scope:
- 5 predefined words
- 6 incorrect guesses allowed
- Basic console input/output

Key Concepts: random, while loop, if-else, strings, lists

Usage:
  Run: python main.py
"""

import random

# ── 5 PREDEFINED WORDS ───────────────────────────────────────────────────────
WORDS = ["python", "network", "security", "firewall", "hacker"]

# ── HANGMAN STAGES ───────────────────────────────────────────────────────────
HANGMAN = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]


def display(word, guessed, wrong, wrong_letters):
    print(HANGMAN[wrong])
    print("  Word: ", " ".join(l if l in guessed else "_" for l in word))
    print(f"\n  Wrong guesses ({wrong}/6): {', '.join(sorted(wrong_letters)) or 'None'}")


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong_letters = set()
    wrong = 0

    print("=" * 40)
    print("        HANGMAN GAME")
    print("=" * 40)
    print("  Guess the word — 6 wrong guesses allowed.")

    while wrong < 6:
        display(word, guessed, wrong, wrong_letters)

        if all(l in guessed for l in word):
            print(f"\n  You guessed it! The word was: {word.upper()}")
            return

        guess = input("\n  Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("  [!] Enter a single letter only.")
            continue

        if guess in guessed or guess in wrong_letters:
            print("  [!] You already guessed that letter.")
            continue

        if guess in word:
            guessed.add(guess)
            print(f"  [+] '{guess}' is in the word!")
        else:
            wrong_letters.add(guess)
            wrong += 1
            print(f"  [-] '{guess}' is not in the word.")

    display(word, guessed, wrong, wrong_letters)
    print(f"\n  Game over! The word was: {word.upper()}")


def main():
    while True:
        play()
        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing!")
            break


if __name__ == "__main__":
    main()
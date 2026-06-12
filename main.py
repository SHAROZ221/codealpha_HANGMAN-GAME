"""
Hangman Game
-------------
Goal: A text-based Hangman game where the player guesses a word one letter at a time.

Simplified Scope:
- 5 predefined words
- 6 incorrect guesses allowed
- Basic console input/output

Extra Features:
- Hint system: reveal a random unguessed letter (costs 1 wrong guess)
- Score tracking: points based on remaining guesses, saved across sessions

Key Concepts: random, while loop, if-else, strings, lists, file handling

Usage:
  Run: python main.py
"""

import random
import os

# ── 5 PREDEFINED WORDS ───────────────────────────────────────────────────────
WORDS = ["python", "network", "security", "firewall", "hacker"]

SCORE_FILE = "hangman_score.txt"

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


def load_total_score():
    if os.path.exists(SCORE_FILE):
        try:
            with open(SCORE_FILE, "r") as f:
                return int(f.read().strip())
        except (ValueError, OSError):
            return 0
    return 0


def save_total_score(total):
    with open(SCORE_FILE, "w") as f:
        f.write(str(total))


def display(word, guessed, wrong, wrong_letters):
    print(HANGMAN[wrong])
    print("  Word: ", " ".join(l if l in guessed else "_" for l in word))
    print(f"\n  Wrong guesses ({wrong}/6): {', '.join(sorted(wrong_letters)) or 'None'}")


def give_hint(word, guessed):
    unguessed = [l for l in set(word) if l not in guessed]
    if not unguessed:
        return None
    return random.choice(unguessed)


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong_letters = set()
    wrong = 0
    hint_used = False

    print("=" * 40)
    print("        HANGMAN GAME")
    print("=" * 40)
    print("  Guess the word — 6 wrong guesses allowed.")
    print("  Type 'hint' to reveal a letter (costs 1 wrong guess).")

    while wrong < 6:
        display(word, guessed, wrong, wrong_letters)

        if all(l in guessed for l in word):
            points = max(0, 6 - wrong) * 10
            print(f"\n  You guessed it! The word was: {word.upper()}")
            print(f"  Points earned: {points}")
            return points

        guess = input("\n  Enter a letter (or 'hint'): ").strip().lower()

        if guess == "hint":
            if hint_used:
                print("  [!] You've already used your hint this round.")
                continue
            hint_letter = give_hint(word, guessed)
            if hint_letter is None:
                print("  [!] No hints available — all letters already guessed!")
                continue
            guessed.add(hint_letter)
            wrong += 1
            hint_used = True
            print(f"  [*] Hint: the word contains '{hint_letter}'. (1 wrong guess added)")
            continue

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
    print("  Points earned: 0")
    return 0


def main():
    total_score = load_total_score()
    print(f"  [i] Total score so far: {total_score}")

    while True:
        points = play()
        total_score += points
        save_total_score(total_score)
        print(f"  Total score: {total_score}")

        again = input("\n  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Thanks for playing!")
            print(f"  Final total score: {total_score}")
            break


if __name__ == "__main__":
    main()
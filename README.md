# Hangman Game
> CodeAlpha Python Programming Internship | Task 1

---

## 📌 Goal
A text-based Hangman game where the player guesses a word one letter at a time, with a maximum of 6 incorrect guesses.

---

## 📁 Project Files

| File | Purpose |
|---|---|
| `main.py` | Main game script |

---

## ▶️ How to Run

No external libraries needed. Uses only built-in Python modules.

```
python main.py
```

---

## 🎮 How to Play

1. A random word is selected from 5 predefined words
2. Guess one letter at a time
3. Correct guess — letter is revealed in the word
4. Wrong guess — hangman drawing progresses
5. You win by guessing all letters before 6 wrong guesses
6. You lose when the hangman is complete (6 wrong guesses)

---

## 🔍 Sample Output

```
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========

  Word:  _ _ _ _ _ _

  Wrong guesses (4/6): a, e, i, o

  Enter a letter:
```

---

## 💡 Key Concepts Used

- `random` — randomly selects a word from the list
- `while loop` — keeps the game running until win or loss
- `if-else` — checks if guessed letter is correct or wrong
- `strings` — word and letter comparison
- `lists` — predefined word list
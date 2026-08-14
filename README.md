# Flashy 🃏

A flashcard-based language learning app built with Python, `tkinter`, and `pandas`. Displays a word, auto-flips after 5 seconds to reveal its translation, and tracks which words you still need to learn, saving your progress between sessions.

## Features
- Displays a random word from a CSV word list on a flashcard
- Auto-flips the card after 5 seconds to reveal the English translation, with matching color and image changes
- Mark a word as "known" to remove it from future rotation
- Progress is saved to `words_to_learn.csv`, so known words stay excluded even after closing and reopening the app
- On first run (no progress file yet), automatically falls back to the full original word list

## How to Run
1. Clone or download this repository to your device.
2. Make sure you have Python installed (3.x recommended) along with `pandas`:

pip install pandas

3. Make sure the `images/` folder (containing `card_front.png`, `card_back.png`, `right.png`, `wrong.png`) and the `data/` folder (containing your word list CSV) are in the same directory as `main.py`.
4. Run `main.py`:

## What I Learned
- Managing scheduled, repeating UI updates with `window.after()` and `window.after_cancel()`, including handling the edge case of cancelling a timer that doesn't exist yet on the very first run
- Updating existing canvas items (image, text, color) in place using `canvas.itemconfig()`, instead of recreating them each time
- Debugging a state-leak bug where a flipped card's white text and back-image styling incorrectly carried over into newly displayed cards, since the "reset to front" logic was missing
- Persisting application state across sessions using `pandas`, reading a "progress" CSV if it exists, falling back to the original source data otherwise
- Debugging a subtle pandas bug where repeated `to_csv()` calls without `index=False` caused unnamed index columns to stack up across multiple runs, corrupting the saved data over time
- Refactoring a `try`/`except` workaround into a simpler, non-duplicated `if variable is not None:` check, after realizing the exception-based approach depended on guessing the correct exception type and duplicated significant logic
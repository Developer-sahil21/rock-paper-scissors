# Day 4 — Rock Paper Scissors

> 30 Days of Python | Difficulty: Easy

## What it does

A terminal Rock Paper Scissors game against the computer. Tracks wins, losses,
and draws across unlimited rounds. Supports single-letter shortcuts (r/p/s) and
shows a full scoreboard after every round. A web UI version is also included.

## Files

| File | Description |
|---|---|
| `day4_rock_paper_scissors.py` | Terminal version — run with Python |
| `day4_ui.html` | Web UI version — open in browser |
| `day4_README.md` | This file |

## Concepts covered

| Concept | Usage |
|---|---|
| `random.choice(list)` | Computer picks from a list randomly |
| Dictionary lookup | `wins_against` dict replaces long if/elif chains |
| `while True` + `break` | Game loop that runs until player quits |
| `.strip().lower()` | Cleaning messy user input |
| Shortcut mapping | `{'r':'rock','p':'paper','s':'scissors'}` |
| Score tracking (dict) | `score = {'player':0, 'computer':0, 'draws':0}` |
| Functions | Separated concerns: logic, display, input |
| f-strings | Clean formatted output |

## How to run

```bash
python day4_rock_paper_scissors.py
```

No external libraries needed. Pure Python 3.

## Sample output

```
╔══════════════════════════════════╗
║   🪨 📄 ✂️   Rock Paper Scissors   ║
╚══════════════════════════════════╝

  Your choice — [r]ock / [p]aper / [s]cissors / [q]uit: r

  Round 1
  You      →  🪨  Rock
  Computer →  ✂️   Scissors

  🎉  You win this round!

  ┌─────────────────────────┐
  │      Scoreboard         │
  ├─────────────────────────┤
  │  You       : 1          │
  │  Computer  : 0          │
  │  Draws     : 0          │
  │  Rounds    : 1          │
  └─────────────────────────┘
```

## Challenge extensions

- **Easy:** Add a "best of 5" mode that ends automatically
- **Medium:** Add Rock Paper Scissors Lizard Spock (5 choices)
- **Hard:** Track win streaks and show the longest streak at the end

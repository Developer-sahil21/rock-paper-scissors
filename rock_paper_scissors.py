"""
Day 4 — Rock Paper Scissors
Play vs computer, track score across rounds.
"""

import random


# ── Constants ──────────────────────────────────────────────────────────────
CHOICES = ['rock', 'paper', 'scissors']

WINS_AGAINST = {
    'rock':     'scissors',   # rock crushes scissors
    'scissors': 'paper',      # scissors cuts paper
    'paper':    'rock',       # paper covers rock
}

EMOJI = {
    'rock':     '🪨',
    'paper':    '📄',
    'scissors': '✂️',
}


# ── Game logic ─────────────────────────────────────────────────────────────

def get_computer_choice() -> str:
    """Return a random choice for the computer."""
    return random.choice(CHOICES)


def get_result(player: str, computer: str) -> str:
    """Return 'win', 'loss', or 'draw' from the player's perspective."""
    if player == computer:
        return 'draw'
    elif WINS_AGAINST[player] == computer:
        return 'win'
    else:
        return 'loss'


def display_round(player: str, computer: str, result: str, round_num: int) -> None:
    """Print the round outcome."""
    p_emoji = EMOJI[player]
    c_emoji = EMOJI[computer]

    print(f"\n  Round {round_num}")
    print(f"  You      →  {p_emoji}  {player.capitalize()}")
    print(f"  Computer →  {c_emoji}  {computer.capitalize()}")
    print()

    if result == 'win':
        print(f"  🎉  You win this round!")
    elif result == 'loss':
        print(f"  💀  Computer wins this round!")
    else:
        print(f"  🤝  It's a draw!")


def display_score(score: dict, rounds: int) -> None:
    """Print the current scoreboard."""
    print(f"\n  ┌─────────────────────────┐")
    print(f"  │      Scoreboard         │")
    print(f"  ├─────────────────────────┤")
    print(f"  │  You       : {score['player']:<11}│")
    print(f"  │  Computer  : {score['computer']:<11}│")
    print(f"  │  Draws     : {score['draws']:<11}│")
    print(f"  │  Rounds    : {rounds:<11}│")
    print(f"  └─────────────────────────┘")


def display_final(score: dict, rounds: int) -> None:
    """Print the final result when the player quits."""
    print("\n" + "═" * 35)
    print("  FINAL RESULTS")
    print("═" * 35)
    display_score(score, rounds)

    if score['player'] > score['computer']:
        print("\n  🏆  You won overall! Great game!")
    elif score['computer'] > score['player']:
        print("\n  🤖  Computer won overall. Better luck next time!")
    else:
        print("\n  🤝  Overall it's a draw!")
    print()


def get_player_choice() -> str | None:
    """
    Prompt the player for their choice.
    Returns the choice string, or None if the player wants to quit.
    """
    shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}

    while True:
        raw = input("  Your choice — [r]ock / [p]aper / [s]cissors / [q]uit: ")
        choice = raw.strip().lower()

        if choice == 'q':
            return None
        if choice in shortcuts:
            return shortcuts[choice]
        if choice in CHOICES:
            return choice

        print("  ⚠️  Type r, p, s (or full word). Try again.\n")


# ── Main ────────────────────────────────────────────────────────────────────

def main():
    print("\n╔══════════════════════════════════╗")
    print("║   🪨 📄 ✂️   Rock Paper Scissors   ║")
    print("╚══════════════════════════════════╝")
    print("  First to ∞  |  Type 'q' to quit\n")

    score  = {'player': 0, 'computer': 0, 'draws': 0}
    rounds = 0

    while True:
        player = get_player_choice()

        if player is None:          # player quit
            break

        computer = get_computer_choice()
        result   = get_result(player, computer)
        rounds  += 1

        # Update score
        if result == 'win':
            score['player'] += 1
        elif result == 'loss':
            score['computer'] += 1
        else:
            score['draws'] += 1

        display_round(player, computer, result, rounds)
        display_score(score, rounds)

    if rounds == 0:
        print("\n  No rounds played. Goodbye! 👋\n")
    else:
        display_final(score, rounds)


if __name__ == "__main__":
    main()

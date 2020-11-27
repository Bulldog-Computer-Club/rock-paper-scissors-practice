from enum import Enum
import sys
import random

Choice = Enum("Choice", "rock paper scissors")

# A dictionary of choice -> choice which this choice beats
# For example, paper beats rock
COUNTERS = {
    Choice.paper: Choice.rock,
    Choice.rock: Choice.scissors,
    Choice.scissors: Choice.paper,
}

# Terminal escape codes for coloring text
GREEN_ANSI = "\033[92m"
END_ANSI = "\033[0m"


def get_choice(val):
    if val == "r" or val == "rock":
        return Choice.rock
    if val == "p" or val == "paper":
        return Choice.paper
    if val == "s" or val == "scissors":
        return Choice.scissors


try:
    user_input = ""
    while True:
        user_input = input(
            f"{GREEN_ANSI}Rock, Paper, Scissors? Type your choice here or .quit to quit: {END_ANSI}"
        ).lower()

        if user_input == ".quit":
            print("Shutting down the magical rock-paper-scissors AI...")
            sys.exit()

        # Map user choice to enum value
        choice = get_choice(user_input)
        if choice is None:
            print("That wasn't a valid input! Please try again.")
            continue

        # Pick a random value
        self_choice = random.choice(list(Choice))

        if self_choice == choice:
            print("🤔 Aw man, it was a tie... Let's play again.\n")
            continue

        # If our choice counters the user pick
        if COUNTERS[self_choice] == choice:
            print(
                f"🚀 You got absolutely destroyed by the bigbrain computer, as I chose {self_choice.name} versus your {choice.name}. Wanna play again?\n"
            )
            continue

        print(
            f"🤯 You beat me, human. I chose {self_choice.name} but you chose {choice.name}. Now let's play again.\n"
        )

except KeyboardInterrupt:
    print("\nGood playing with you, human. I'll be shutting down now.")

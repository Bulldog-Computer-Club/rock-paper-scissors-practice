from enum import Enum
import sys
import random
from typing import Union

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

MESSAGE_TIE = "🤔 Aw man, it was a tie... Let's play again.\n"
MESSAGE_SELF_WIN = "🚀 You got absolutely destroyed by the bigbrain computer, as I chose %s versus your %s. Wanna play again?\n"
MESSAGE_SELF_LOSE = (
    "🤯 You beat me, human. I chose %s but you chose %s. Now let's play again.\n"
)


def get_choice(val: str) -> Union[Choice, None]:
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
            print("That wasn't a valid input! Please try again.\n")
            continue

        # Pick a random value
        bot_choice: Choice = random.choice(list(Choice))

        if bot_choice == choice:
            print("🤔 Aw man, it was a tie... Let's play again.\n")
        elif COUNTERS[bot_choice] == choice:
            print(MESSAGE_SELF_WIN.format(bot_choice.name, choice.name))
        else:
            print(MESSAGE_SELF_LOSE.format(bot_choice.name, choice.name))

except KeyboardInterrupt:
    print("\nGood playing with you, human. I'll be shutting down now.")

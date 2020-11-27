import sys
import random

# A tuple of tuples (computer_choice, user_choice) where the computer wins
WIN_CASES = (("rock", "scissor"), ("scissor", "paper"), ("paper", "rock"))
# Valid choices
CHOICES = ("rock", "paper", "scissors")

# Terminal escape codes for coloring text
GREEN_ANSI = "\033[92m"
END_ANSI = "\033[0m"

QUIT_KEYWORDS = (".quit", "q", "stop", "exit")

MESSAGE_WIN = (
    "🤯 You beat me, human. I chose {0} but you chose {1}. Now let's play again.\n"
)
MESSAGE_LOSE = "🚀 You got absolutely destroyed by the bigbrain computer, as I chose {0} versus your {1}. Wanna play again?\n"
MESSAGE_TIE = "🤔 Aw man, it was a tie... Let's play again.\n"

try:
    user_choice = ""
    while True:
        user_choice = input(
            f"{GREEN_ANSI}Rock, Paper, Scissors? Type your choice here or .quit to quit: {END_ANSI}"
        ).lower()

        if user_choice in QUIT_KEYWORDS:
            print("Shutting down the magical rock-paper-scissors AI...")
            sys.exit()
        if user_choice not in CHOICES:
            print("That wasn't a valid choice, please try again.")
            continue

        # Pick a random value
        bot_choice = random.choice(CHOICES)

        if (bot_choice, user_choice) in WIN_CASES:
            print(MESSAGE_LOSE.format(bot_choice, user_choice))
        elif bot_choice == user_choice:
            print(MESSAGE_TIE)
        else:
            print(MESSAGE_WIN.format(bot_choice, user_choice))

except KeyboardInterrupt:
    print("\nGood playing with you, human. I'll be shutting down now.")

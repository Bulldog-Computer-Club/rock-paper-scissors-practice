import sys
import random

# A tuple of tuples (computer_choice, user_choice) where the computer wins
WIN_CASES = (("rock", "scissor"), ("scissor", "paper"), ("paper", "rock"))
# Valid choices
CHOICES = ("rock", "paper", "scissors")

# Terminal escape codes for coloring text
GREEN_ANSI = "\033[92m"
END_ANSI = "\033[0m"

LOSE_MESSAGES = (
    "🤯 You beat me, human. I chose {0} but you chose {1}. Now let's play again.\n",
    "🤯 How in the world did you do that?! I chose {0} but you chose {1}. You must be using some hax or something...\n",
)
TIE_MESSAGES = (
    "🤔 Aw man, it was a tie... Let's play again.\n",
    "🤔 Quite disappointing, a tie... not to worry, I'll destroy you next time!\n",
)
WIN_MESSAGES = (
    "🚀 You got absolutely destroyed by the bigbrain computer, as I chose {0} versus your {1}. Wanna play again?\n",
    "🚀 git gud --scrub --bot-choice {0} --your-choice {1}\n",
)

try:
    user_choice = ""

    user_input = input(
        f"{GREEN_ANSI}Do you want to play in godmode? Anything other than 'yes' or 'y' will be interpreted as no. {END_ANSI}"
    ).lower()
    # :troll: 10% chance of godmode even if they say no
    godmode = True if user_input in ("yes", "y") else random.random(0, 9) == 0
    print(f"Alright, let's start!\n")

    while True:
        user_choice = input(
            f"{GREEN_ANSI}Rock, Paper, Scissors? Type your choice here or .quit to quit: {END_ANSI}"
        ).lower()

        if user_choice in (".quit", "q", "stop", "exit"):
            print("Shutting down the magical rock-paper-scissors AI...")
            sys.exit()
        if user_choice not in CHOICES:
            print("That wasn't a valid choice, please try again.")
            continue

        # Pick a random value
        bot_choice = (
            # Find winning case if godmode is on
            next(x for x in WIN_CASES if x[1] == user_choice)[0]
            if godmode
            else random.choice(CHOICES)
        )

        messages = None
        if (bot_choice, user_choice) in WIN_CASES:
            messages = WIN_MESSAGES
        elif bot_choice == user_choice:
            messages = TIE_MESSAGES
        else:
            messages = LOSE_MESSAGES

        print(random.choice(messages).format(bot_choice, user_choice))

except KeyboardInterrupt:
    print("\nGood playing with you, human. I'll be shutting down now.")

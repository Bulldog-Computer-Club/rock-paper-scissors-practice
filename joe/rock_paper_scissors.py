import sys
import random

# A tuple of tuples (computer_choice, user_choice) where the computer wins
WIN_CASES = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))
# Valid choices
CHOICES = ("rock", "paper", "scissors")

# Terminal escape codes for coloring text
GREEN_ANSI_START = "\033[92m"
ANSI_END = "\033[0m"

WIN_MESSAGES = (
    "🚀 You got absolutely destroyed by the bigbrain computer, as I chose {0} versus your {1}. Wanna play again?\n",
    "🚀 git gud --scrub --bot-choice {0} --your-choice {1}\n",
)
TIE_MESSAGES = (
    "🤔 Aw man, it was a tie... Let's play again.\n",
    "🤔 Quite disappointing, a tie... not to worry, I'll destroy you next time!\n",
)
LOSE_MESSAGES = (
    "🤯 You beat me, human. I chose {0} but you chose {1}. Now let's play again.\n",
    "🤯 How in the world did you do that?! I chose {0} but you chose {1}. You must be using some hax or something...\n",
)

# question() wraps input() to use ANSI escape codes to make the prompt text green and converts the result to lowercase.
def question(prompt: str):
    """Prompts the user for input and returns the input converted to lowercase.

    Args:
        prompt: The prompt to output in the terminal. It will be wrapped in ANSI escape codes to appear green.

    Returns:
        The inputted value converted to lowercase.
    """

    green_text = f"{GREEN_ANSI_START}{prompt}{ANSI_END}"
    return input(green_text).lower()


try:
    user_input = question(
        "Do you want to play in godmode? Anything other than 'yes' or 'y' will be interpreted as no. "
    )

    # :troll: 10% chance of godmode even if they say no
    godmode_enabled = user_input in ("yes", "y") or random.randint(0, 9) == 0
    print(f"Alright, let's start!\n")

    while True:
        user_choice = question(
            "Rock, Paper, Scissors? Type your choice here or .quit to quit: "
        )

        if user_choice in (".quit", "q", "stop", "exit"):
            print("Shutting down the magical rock-paper-scissors AI...")
            sys.exit()
        elif user_choice not in CHOICES:
            print("That wasn't a valid choice, please try again.")
            continue

        # Pick a random value
        bot_choice = (
            # Find winning case if godmode is on
            next(x for x in WIN_CASES if x[1] == user_choice)[0]
            if godmode_enabled
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

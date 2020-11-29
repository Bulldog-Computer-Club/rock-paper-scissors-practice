import strutils
import strformat
import random

proc ask(prompt: string): string =
    echo &"\x1b[92m{prompt}\x1b[0m"
    return strip(readLine(stdin))

let choices: array[3, string] = ["rock", "paper", "scissors"]

randomize()
let userInput = ask("Do you want to play in godmode? Anything other than 'yes' or 'y' will be interpreted as no. ")
let godmodeEnabled = case userInput
    of "yes", "y": true
    else: false

echo "Alright, let's start!"
while true:
    let userChoice = ask("Rock, paper, scissors? Type your choice here or '.quit' to quit: ")

    if userChoice in @[".quit", "q", "stop", "exit"]:
        echo "Shutting down the magical rock-paper-scissors AI..."
        system.quit(0)
    
    let userIndex = find(choices, userChoice)
    if userIndex == -1:
        echo "That wasn't a valid choice, please try again."
        continue
        
    let botIndex = if godmodeEnabled: (userIndex + 1) mod 3 else: rand(0..2)

    if botIndex == userIndex: echo "Aw man, it was a tie... Let's play again."
    elif (userIndex + 1) mod 3 == botIndex: echo "You got absolutely destroyed by the bigbrain computer, as I chose ", choices[botIndex], " versus your ", choices[userIndex], ". Wanna play again?"
    else: echo "You beat me, human. I chose ", choices[botIndex], " but you chose", choices[userIndex], "... Now let's play again."
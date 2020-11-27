import time

playing = True

while playing:
    playerInput = input("What will you choose (type 'rock' || 'paper' || 'scissors')").lower()
    botInput = ""

    if playerInput == "rock":
        botInput = "My choice: paper"
    elif playerInput == "paper":
        botInput = "My choice: scissors"
    elif playerInput == "scissors":
        botInput = "My choice: rock"
    else:
        print("You didnt type 'rock' 'paper' or 'scissors' :angery:")
        continue

    print(f"Your choice: {playerInput}\n{botInput}\nyou lost")

    if input("Do you still want to play (type 'T' || 'F')") == "F":
        playing = False
    
    time.sleep(1)

# THIS IS A JOKE AND IS NOT ACTUALLY MADE FOR PLAYING HRNGHRGNHRGNHR GNHRGHRNGHN RGNHRGNHRNGH R NG






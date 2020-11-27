package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

const (
	ChoiceRock     = "rock"
	ChoicePaper    = "paper"
	ChoiceScissors = "scissors"

	GreenAnsiStart = "\033[92m"
	AnsiEnd        = "\033[0m"
)

var (
	winCases = map[string]string{ChoiceRock: ChoiceScissors, ChoiceScissors: ChoicePaper, ChoicePaper: ChoiceRock}
	choices  = [3]string{ChoiceRock, ChoicePaper, ChoiceScissors}
)

func main() {
	rand.Seed(time.Now().UnixNano())

	for {
		choice := input("Rock, paper, scissors? ")

		switch choice {
		case ChoiceRock, ChoicePaper, ChoiceScissors:
			// ok
		case ".quit", "q", "stop", "exit":
			fmt.Println("Fun playing with you, shutting down...")
			os.Exit(0)
		default:
			fmt.Println("That wasn't a valid choice, please try again.")
			continue
		}

		botChoice := choices[rand.Intn(3)]

		loseCase := winCases[botChoice]

		switch {
		case choice == loseCase:
			fmt.Printf("You got absolutely destroyed by the bigbrain computer, as I chose %s versus your %s. Wanna play again?\n", botChoice, choice)
		case choice == botChoice:
			fmt.Println("Aw man, it was a tie... Let's play again.")
		default:
			fmt.Printf("You beat me, human. I chose %s but you chose %s... Now let's play again.\n", botChoice, choice)
		}
	}
}

func input(prompt string) string {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(prompt)
	text, _ := reader.ReadString('\n')

	return strings.ToLower(strings.TrimSpace(text))
}

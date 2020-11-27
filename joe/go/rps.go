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
	ChoiceRock    = "rock"
	ChoicePaper   = "paper"
	ChoiceScissor = "scissor"

	GreenAnsiStart = "\033[92m"
	AnsiEnd        = "\033[0m"
)

var (
	winCases = map[string]string{ChoiceRock: ChoiceScissor, ChoiceScissor: ChoicePaper, ChoicePaper: ChoiceRock}
	choices  = [3]string{ChoiceRock, ChoicePaper, ChoiceScissor}
)

func main() {
	rand.Seed(time.Now().UnixNano())

	for {
		choice := input("Rock, paper, scissors? ")

		switch choice {
		case ChoiceRock, ChoicePaper, ChoiceScissor:
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
		if choice == loseCase {
			fmt.Printf("You got absolutely destroyed by the bigbrain computer, as I chose %s versus your %s. Wanna play again?\n", botChoice, choice)
		} else if choice == botChoice {
			fmt.Println("Aw man, it was a tie... Let's play again.")
		} else {
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

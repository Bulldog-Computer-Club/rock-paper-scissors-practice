import { createInterface } from 'readline';
import { once } from 'events';

const enum Choice {
	Rock = 'rock',
	Paper = 'paper',
	Scissors = 'scissors',
}

const GREEN_ANSI_START = '\u001b[92m';
const ANSI_END = '\u001b[0m';

const winCases = {
	[Choice.Rock]: Choice.Scissors,
	[Choice.Scissors]: Choice.Rock,
	[Choice.Paper]: Choice.Rock,
};
const choices = [Choice.Rock, Choice.Paper, Choice.Scissors];

// Small utility to prompt for input. Wrapped in an IIFE to prevent polluting scope with `scanner`.
const ask = (() => {
	const scanner = createInterface({ input: process.stdin, output: process.stdout });
	return async (question: string) => {
		// We don't want a newline
		process.stdout.write(`${GREEN_ANSI_START}${question}${ANSI_END}`);
		const [input]: string[] = await once(scanner, 'line');
		return input.trim().toLowerCase();
	};
})();

async function main() {
	for (;;) {
		const userChoice = await ask('Rock, paper, scissors? ');

		switch (userChoice) {
			case Choice.Rock:
			case Choice.Scissors:
			case Choice.Paper:
				// Okay
				break;

			case '.quit':
			case 'q':
			case 'stop':
			case 'exit':
				console.log('Fun playing with you, shutting down...');
				process.exit(0);

			default:
				console.log("That wasn't a valid choice, please try again.");
				continue;
		}

		const botChoice = choices[Math.floor(Math.random() * choices.length)];
		const losingChoice = winCases[botChoice];
		if (userChoice === losingChoice) {
			console.log(
				`You got absolutely destroyed by the bigbrain computer, as I chose ${botChoice} versus your ${userChoice}. Wanna play again?`,
			);
		} else if (userChoice === botChoice) {
			console.log("Aw man, it was a tie... Let's play again.");
		} else {
			console.log(`You beat me, human. I chose ${botChoice} but you chose ${userChoice}... Now let's play again.`);
		}
	}
}

main();

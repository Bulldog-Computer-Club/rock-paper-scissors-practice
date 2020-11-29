import java.util.Scanner;
import java.util.Random;
import java.util.HashMap;
import java.util.Map;

public class RockPaperScissors {
	private static final Scanner scanner = new Scanner(System.in);
	private static final Random rand = new Random();
	private static final Choice[] choices = Choice.values();
	private static final char ansiSeparator = (char) Integer.parseInt("0001b", 16);

	private static Map<Choice, Choice> losingChoices = new HashMap<>();

	static {
		losingChoices.put(Choice.ROCK, Choice.SCISSORS);
		losingChoices.put(Choice.SCISSORS, Choice.ROCK);
		losingChoices.put(Choice.PAPER, Choice.ROCK);
	}

	public static void main(String[] args) {
		while (true) {
			var userInput = input("Rock, paper, scissors? ");

			var userChoice = Choice.fromStr(userInput);
			if (userChoice == null) {
				switch (userInput) {
					case ".quit":
					case "q":
					case "stop":
					case "exit":
						System.out.println("Fun playing with you, shutting down...");
						System.exit(0);

					default:
						System.out.println("That wasn't a valid choice, please try again.");
						continue;
				}
			}

			var botChoice = choices[rand.nextInt(choices.length)];
			var losingChoice = losingChoices.get(botChoice);
			if (userChoice.equals(losingChoice)) {
				System.out.printf(
						"You got absolutely destroyed by the bigbrain computer, as I chose %s versus your %s. Wanna play again?\n",
						botChoice.getStr(), userChoice.getStr());
			} else if (userChoice.equals(botChoice)) {
				System.out.println("Aw man, it was a tie... Let's play again.");
			} else {
				System.out.printf("You beat me, human. I chose %s but you chose %s... Now let's play again.\n",
						botChoice.getStr(), userChoice.getStr());
			}
		}
	}

	private static String input(String prompt) {
		System.out.printf("%c[92m%s%c[0m", ansiSeparator, prompt, ansiSeparator);
		return scanner.nextLine().trim().toLowerCase();
	}

	private enum Choice {
		ROCK("rock"), PAPER("paper"), SCISSORS("scissors");

		private final String choiceStr;

		Choice(String choiceStr) {
			this.choiceStr = choiceStr;
		}

		public String getStr() {
			return choiceStr;
		}

		private final static Map<String, Choice> lookup = new HashMap<>();

		static {
			for (var choice : Choice.values()) {
				lookup.put(choice.getStr(), choice);
			}
		}

		public static Choice fromStr(String str) {
			return lookup.get(str);
		}
	}
}
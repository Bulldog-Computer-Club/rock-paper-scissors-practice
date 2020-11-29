using System;
using System.Collections.Generic;

namespace csharp
{
	class RockPaperScissors
	{
		private static Random random = new Random();
		private static string[] choices = { Choice.Rock, Choice.Paper, Choice.Scissors };
		private static IDictionary<string, string> losingChoices
		{
			get
			{
				var choices = new Dictionary<string, string>();
				choices.Add(Choice.Rock, Choice.Scissors);
				choices.Add(Choice.Scissors, Choice.Paper);
				choices.Add(Choice.Paper, Choice.Rock);
				return choices;
			}
		}

		public static void Main()
		{
			while (true)
			{
				var input = GetInput("Rock, paper, scissors? ");

				switch (input)
				{
					case Choice.Rock:
					case Choice.Scissors:
					case Choice.Paper:
						// Okay
						break;

					case ".quit":
					case "q":
					case "stop":
					case "exit":
						Console.WriteLine("Fun playing with you, shutting down...");
						Environment.Exit(0);
						break;

					default:
						Console.WriteLine("That wasn't a valid choice, please try again.");
						continue;
				}

				var botChoice = choices[random.Next(choices.Length)];
				var losingChoice = losingChoices[input];

				if (input.Equals(losingChoice)) Console.WriteLine($"You got absolutely destroyed by the bigbrain computer, as I chose {botChoice} versus your {input}. Wanna play again?");
				else if (input.Equals(botChoice)) Console.WriteLine("Aw man, it was a tie... Let's play again.");
				else Console.WriteLine($"You beat me, human. I chose {botChoice} but you chose {input}. Now let's play again.");
			}
		}

		private static string GetInput(string prompt)
		{
			Console.Write($"\u001b[92m{prompt}\u001b[0m");
			return Console.ReadLine().Trim().ToLower();
		}
	}

	public class Choice
	{
		public const string Rock = "rock";
		public const string Paper = "paper";
		public const string Scissors = "scissors";
	}
}

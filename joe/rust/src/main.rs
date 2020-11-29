use rand::distributions::{Distribution, Uniform};
use std::io::*;

const CHOICES: &[&str] = &["rock", "paper", "scissors"];

fn main() {
	let mut rng = rand::thread_rng();
	let rand_indices = Uniform::from(0..3);

	loop {
		print!("\x1b[92mRock, paper, scissors? \x1b[0m");
		stdout().flush().unwrap();

		let mut input = String::new();
		match stdin().read_line(&mut input) {
			Ok(_) => {}
			Err(_) => {
				println!("Failed to read input, try again?");
				continue;
			}
		};

		let lowered_input_str = input.trim().to_ascii_lowercase();
		let lowered_input = lowered_input_str.as_str();

		let user_index = match lowered_input {
			"rock" | "paper" | "scissors" => {
				CHOICES.iter().position(|&v| v == lowered_input).unwrap()
			}
			".quit" | "q" | "stop" | "exit" => {
				println!("Fun playing with you, shutting down...");
				std::process::exit(1);
			}
			_ => {
				println!("That wasn't a valid choice, please try again.");
				continue;
			}
		};

		let ai_index = rand_indices.sample(&mut rng);

		if (user_index + 1) % 3 == ai_index {
			println!("You got absolutely destroyed by the bigbrain computer, as I chose {} versus your {}. Wanna play again?", CHOICES[ai_index], CHOICES[user_index]);
		} else if user_index == ai_index {
			println!("Aw man, it was a tie... Let's play again.");
		} else {
			println!(
				"You beat me, human. I chose {} but you chose {}... Now let's play again.",
				CHOICES[ai_index], CHOICES[user_index]
			);
		}
	}
}

extern crate rand;

use std::io;
use rand::Rng;

const CHOICES : [&str; 3] = ["rock", "paper", "scissors"];

fn main() {
    println!("Options: Rock, Paper, Scissors");
    print!("What do you choose: \n"); 

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("error, something went wrong");

    let user_choice = CHOICES.iter().position(|&s| s == &input.to_lowercase()[0..input.len() - 1]);
    let cpu_choice = rand::thread_rng().gen_range(0..3);

    println!("\n\nYou chose {}", &String::from(&input[0..input.len() - 1]));
    println!("The computer chose {}", CHOICES[cpu_choice]);

    if (user_choice.unwrap() + 1) % 3 == cpu_choice {
        println!("You lose");
    } else if user_choice.unwrap() == cpu_choice {
        println!("Its a draw!")
    } else {
        println!("You WIN!!!"); 
    }  
}
/*
A really fast rock paper scissor game

SHOULD be cross platform
*/


#include <iostream>
#include <string>
#include <random>

int main() {
	std::string choices[3] = {"Rock", "Paper", "Scissors"};

	std::cout << "Please input your choice. Rock, Paper, or Scissors: ";
	std::string user_input;
	std::cin >> user_input;	
	
	bool passing = false;
	int user_choice_int;
	int i = 0;
	for (std::string choice : choices) {
		if (choice == user_input) {
			passing = true;
			user_choice_int = i;
		}
		i++;
	}

	if (!passing) {
		std::cout << "invalid selection" << std::endl;
		return 0;
	}

	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> distr(0, 2);
	
	int computer_int = distr(gen);
	std::string* computer = &choices[computer_int];


	std::cout << "You chose: " << user_input << std::endl;
	std::cout << "The computer chose: " << *computer << std::endl;
	
	if ((user_choice_int + 1) % 3 == computer_int) {
		std::cout << "You Lose, Computer Won" << std::endl
			<< computer << " beats " << user_input << std::endl;
	} else if (user_choice_int == computer_int) {
		std::cout << "Its a Draw" << std::endl;
	} else {
		std::cout << "You Win, Computer Lost" << std::endl
			<< user_input << " beats " << computer;
	}

	return 0;
}

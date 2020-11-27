/*
an absolutely ridiculously fast rock paper scissor game

Tested on a linux environment, might not work as expected on other platforms
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int random_range(int start, int end) { 
         return (rand() % (end - start + 1)) + start; 
} 

int main() {
	srand(time(NULL));
	const char* choices[] = {"Rock","Paper","Scissors"};
	
	// using numbers instead of whole strings for simplicity
	printf("Please input your choice. Rock (1), Paper (2), or` Scissors (3): ");
	int user_choice;
       	scanf("%d", &user_choice);
	
	if (user_choice > 3) {
		puts("Please enter a number between 1 and 3");
		return 0;
	}	
	user_choice--;
	
	
	int computer = random_range(0, 2);

	printf("You chose: %s\n", choices[user_choice]);
	printf("The computer chose: %s\n", choices[computer]);

	if ((user_choice + 1) % 3 == computer) {
		printf("You Lose, Computer Won\n%s beats %s\n", choices[computer], choices[user_choice]);
	} else if (user_choice == computer) {
		printf("Its a Draw\n");
	} else {
		printf("You Win, Computer Lost\n%s beats %s\n", choices[user_choice], choices[computer]);
	}

	return 0;
}	

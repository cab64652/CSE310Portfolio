package hangman;

import java.util.Scanner;

// This class handles the overall game play and initializes the game.
public class GameController {
	
	// Scanner declared as a class variable so it can be used in multiple functions
	private static Scanner scanner = new Scanner(System.in);
	
	public static void main(String[] args) {
		
		// Get user input to select the difficulty for the game.
		Integer choice;
		
		// This while loop will play the game until quit is selected.
		do {
			
			// This will catch any input that is not a number.
			try {
				displayMenu();
				choice = scanner.nextInt();
			}
			catch (Exception e) {
				choice = -1;
				scanner.nextLine(); 
			}
			
			// Starts the game with the corresponding difficulty or quit the game.
			switch (choice) {
			case 0:
				break;
				
			case 1:
				playGame("easy");
				break;
				
			case 2:
				playGame("med");
				break;
				
			case 3:
				playGame("hard");
				break;
				
			default:
				System.out.println("Invalid Input!");
				break;
			}	
			
		} while (choice != 0);
		scanner.close();
		
	}
	
	
	// Displays the game menu.
	private static void displayMenu() {
		System.out.println("Hangman:\n"
				+ "0. Quit\n"
				+ "1. Easy\n"
				+ "2. Medium\n"
				+ "3. Hard");
	}
	
	
	// Initializes the game and handles the game play. 
	private static void playGame(String difficulty) {
		
		// Creates a new game and sets the difficulty level
		Game game = new Game();
		game.initializeGame(difficulty);
		
		// Runs the game until the word is guessed or
		// until the hang man is completed.
		do {
			
			// Displays the hang man and gets the users guess.
			game.displayGame();
			System.out.println("Enter a letter: ");
			
			// This will catch any input that is not a letter.
			try {
				char letter = scanner.next().charAt(0);
				
				// Checks the hidden word to see if it contains the letter guess.
				if (game.word.hiddenWord.contains(String.valueOf(letter))){
					
					// Updates the hint if there is a letter match.
					game.updateHint(letter);
				}
				else {
					
					// Updates the hang man if there is no a letter match. 
					game.updateGameBoard(letter);
				}
				
				// Checks to see if the hidden word has be solved.
				game.gameWon();
			}
			catch (Exception e) {
				
					System.out.println("Invalid Input!");
			}
			
		// Returns false while the hidden word is not 
		// guessed and the hang man is not completed.
		} while (!game.gameOver());
	}
}
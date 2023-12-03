package hangman;

import java.util.Scanner;


public class GameController {

	private static Scanner scanner = new Scanner(System.in);

	public static void main(String[] args) {
		Integer choice;
		
		do {

			try {
				displayMenu();
				choice = scanner.nextInt();
			}
			catch (Exception e) {
				choice = -1;
				scanner.nextLine(); 
			}
		
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
	
	
	private static void displayMenu() {
		System.out.println("Hangman:\n"
				+ "0. Quit\n"
				+ "1. Easy\n"
				+ "2. Medium\n"
				+ "3. Hard");
	}
	
	
	private static void playGame(String difficulty) {
		Game game = new Game();
		game.initializeGame(difficulty);
		
		do
		{
			game.displayGame();
			System.out.println("Enter a letter: ");

			try{
				char letter = scanner.next().charAt(0);

				if (game.checkLetter(letter))
				{
					game.updateHint(letter);
				}
				else
				{
					game.updateGameBoard(letter);
				}
				
				game.gameWon();
			}
			catch (Exception e) {
					System.out.println("Invalid Input!");
			}
		} while (!game.gameOver());
	}
}
package hangman;

import java.util.Scanner;


public class GameController {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		Integer choice;
		
		do {
			
			do {
				displayMenu();
				String input = scanner.nextLine();
				choice = isInt(input);
			} while (choice == null);
		
			switch (choice) {
			case 0:
				break;
				
			case 1:
				playGame("Easy");
				break;
				
			case 2:
				playGame("Medium");
				break;
				
			case 3:
				playGame("Hard");
				break;
				
//			case null:
//				System.out.println("Invalid Input");
//				break;
				
			default:
				System.out.println("Invalid Input");
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
		game.initialize_game();
		game.display();
		Scanner scanner = new Scanner(System.in);

		while (!game.game_over())
		{
			System.out.println("Enter a letter: ");

			try{
				char letter = scanner.next().charAt(0);

				if (game.check_letter(letter))
				{
					game.update_hint(letter);
				}
				else
				{
					game.update_game_board(letter);
				}
				game.display();
				game.game_won();
			}
			catch (Exception e) {
					System.out.println("Invalid Input!");
			}
		}
		
		scanner.close();
	}
	
	
	private static Integer isInt(String str) {
		
		try {
			
			return Integer.parseInt(str);
			
		} catch (Exception e){
			
			System.out.println("Invalid Input");
			return null;
		}
	}

}

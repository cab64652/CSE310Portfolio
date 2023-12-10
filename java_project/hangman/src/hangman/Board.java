package hangman;

// This class creates the hang man and handles all updates 
// for it as well as keeping track of the strikes.
public class Board {
	
	public String gameBoard; // Stores the hang man.
	public int strikes;      // Number of incorrect guesses.
	
	// Creates the starting hang man.
	void initializeBoard() {
		gameBoard = ("     ____\n"
				+ "    |    |\n"
				+ "    |    |\n"
				+ "         |\n"
				+ "         |\n"
				+ "         |\n"
				+ "         |\n"
				+ "   ______|__\n"
				+ "  |         |\n"
				+ "  |         |");
	}
	
	
	void displayBoard() {
		
		System.out.println(gameBoard);
	}
	
	// Adds a strike when called.
	void updateStrikes() {
		
		strikes++;
	}
	
	
	// Updates the hang man and adds incorrect letters to the hang man.
	void updateBoard(char letter) {
		
		// Adds a strike.
		updateStrikes();
		// Temporary array to update individual characters. 
		char[] tempGameBoard = gameBoard.toCharArray();
		
		// Updates the hang man based on how many strikes there are. 
		switch (strikes) {
		
		// Updates the strikes by index according to the number of strikes.
		case 0:
			break;

		case 1:
			tempGameBoard[25] = '0';     // Updates hang man.
			tempGameBoard[93] = letter;  // Updates incorrect letters.
			break;

		case 2:
			tempGameBoard[36] = '|';     // Updates hang man.
			tempGameBoard[94] = letter;  // Updates incorrect letters.
			break;

		case 3:
			tempGameBoard[35] = '\\';     // Updates hang man.
			tempGameBoard[95] = letter;  // Updates incorrect letters.
			break;

		case 4:
			tempGameBoard[37] = '/';     // Updates hang man.
			tempGameBoard[96] = letter;  // Updates incorrect letters.
			break;

		case 5:
			tempGameBoard[47] = '|';     // Updates hang man.
			tempGameBoard[97] = letter;  // Updates incorrect letters.
			break;

		case 6:
			tempGameBoard[57] = '/';     // Updates hang man.
			tempGameBoard[98] = letter;  // Updates incorrect letters.
			break;

		case 7:
			tempGameBoard[59] = '\\';    // Updates hang man.
			tempGameBoard[99] = letter;  // Updates incorrect letters.
			break;

		case 8:
			break;

		default:
			System.out.println("Error updating board.");
		}
		
		// Converts the the temporary hang man array 
		// into a string and sets it to the hang man.
		gameBoard = new String(tempGameBoard);
	}
}

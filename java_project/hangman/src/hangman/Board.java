package hangman;

public class Board {
	
	public String gameBoard;
	public int strikes;
	
	
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
	
	
	void updateStrikes() {
		strikes ++;
	}
	
	
	void updateBoard(char letter) {
		updateStrikes();
		char[] tempGameBoard;

		switch (strikes)
		{
		case 0:
			break;

		case 1:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[25] = '0';
			tempGameBoard[93] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 2:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[36] = '|';
			tempGameBoard[94] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 3:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[35] = '\\';
			tempGameBoard[95] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 4:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[37] = '/';
			tempGameBoard[96] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 5:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[47] = '|';
			tempGameBoard[97] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 6:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[57] = '/';
			tempGameBoard[98] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 7:
			tempGameBoard = gameBoard.toCharArray();
			tempGameBoard[59] = '\\';
			tempGameBoard[99] = letter;
			gameBoard = new String(tempGameBoard);
			break;

		case 8:
			break;

		default:
			System.out.println("Error updating board.");
		}
	}
	
	
	int getStrikes() {
		return strikes;
	}
}

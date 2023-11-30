package hangman;

public class Board {
	
	public String gameBoard;
	public int strikes;
	
	
	void initialize_board() {
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
	
	
	void display_board() {
		System.out.println(gameBoard);
	}
	
	
	void update_strikes() {
		strikes ++;
	}
	
	
	void update_board(char letter) {
		update_strikes();

		switch (strikes)
		{
		case 0:
			break;

		case 1:
			gameBoard = gameBoard.substring(0, 25) + '0' + gameBoard.substring(26, 93) + letter + gameBoard.substring(94);
//			gameBoard[93] = letter;
			break;

		case 2:
			gameBoard = gameBoard.substring(0, 36) + '|' + gameBoard.substring(37, 94) + letter + gameBoard.substring(95);
//			gameBoard[36] = '|';
//			gameBoard[94] = letter;
			break;

		case 3:
			gameBoard = gameBoard.substring(0, 35) + '\\' + gameBoard.substring(36, 95) + letter + gameBoard.substring(96);
//			gameBoard[35] = char(92);
//			gameBoard[95] = letter;
			break;

		case 4:
			gameBoard = gameBoard.substring(0, 37) + '/' + gameBoard.substring(38, 96) + letter + gameBoard.substring(97);
//			gameBoard[37] = '/';
//			gameBoard[96] = letter;
			break;

		case 5:
			gameBoard = gameBoard.substring(0, 47) + '|' + gameBoard.substring(48, 97) + letter + gameBoard.substring(98);
//			gameBoard[47] = '|';
//			gameBoard[97] = letter;
			break;

		case 6:
			gameBoard = gameBoard.substring(0, 57) + '/' + gameBoard.substring(58, 98) + letter + gameBoard.substring(99);
//			gameBoard[57] = '/';
//			gameBoard[98] = letter;
			break;

		case 7:
			gameBoard = gameBoard.substring(0, 59) + '/' + gameBoard.substring(60, 99) + letter + gameBoard.substring(100);
//			gameBoard[59] = char(92);
//			gameBoard[99] = letter;
			break;

		case 8:
			break;

		default:
			System.out.println("Error updating board.");
		}
	}
	
	
	int get_strikes() {
		return strikes;
	}
}

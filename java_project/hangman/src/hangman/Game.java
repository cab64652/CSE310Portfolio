package hangman;

public class Game {
	
	public Word word = new Word();
	String hiddenWord;
	public String hint = "-";
	Board board = new Board();
	
	void getHiddenWord(String difficulty) {
		word.getHiddenWord(difficulty);
		hiddenWord = word.hiddenWord;
	}
	
	void getHint() {
		int hintLen = hiddenWord.length();


		for (int i = 0; i < hintLen - 1; i++)
		{
			hint += "-";
		}
	}
	
	
	void updateHint(char letter) {
		
		int i = 0;
		for (char hiddenLetter : hiddenWord.toCharArray())
		{
			if (hiddenLetter == letter)
			{
				char[] hintChars = hint.toCharArray();
				hintChars[i] = letter;
				hint = new String(hintChars);
			}
			i++;
		}
	}
	
	
	void initializeGame(String difficulty) {
		
		getHiddenWord(difficulty);
		getHint();
		board.initializeBoard();
		
	}
	
	
	void displayGame() {
		
		board.displayBoard();
		System.out.println(hint);
	}
	
	
	void addStrike(char letter) {
		
		board.updateBoard(letter);
	}
	
	
	boolean gameOver() {
		
		if (board.getStrikes() == 8 || hiddenWord.equals(hint))
		{
			return true;
		}

		return false;
	}
	
	
	void updateGameBoard(char letter) {
		board.updateBoard(letter);
	}
	
	
	boolean checkLetter(char letter) {
		
		for (char hiddenLetter : hiddenWord.toCharArray())
		{
			if(hiddenLetter == letter)
			{
				return true;
			}
		}
		
		return false;
	}
	
	
	void gameWon() {
		
		if (gameOver())
		{
			System.out.println(hiddenWord);
			
			if (hiddenWord.equals(hint))
			{
				System.out.println("You won!");
			}
			else
			{
				System.out.println("Game Over!");
			}
		}
	}
	
}

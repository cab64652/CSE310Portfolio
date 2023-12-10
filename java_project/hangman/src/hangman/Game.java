package hangman;


// This class handles all the details of game play including setting
// up the hang man, getting the hidden word and creating the hint.
public class Game {
	
	public Word word = new Word();
	public Board board = new Board();
	public String hint = "-";
	
	// Sets the hidden word in the word object.
	void getHiddenWord(String difficulty) {
		
		word.getHiddenWord(difficulty);
	}
	
	// Sets the hint equal to a number dashes 
	// equal to the length of the hidden word.
	void getHint() {
		
		int hintLen = word.hiddenWord.length();

		for (int i = 0; i < hintLen - 1; i++) {
			
			hint += "-";
		}
	}
	
	// Replaces dashes in the hint with letter corresponding
	// to the letters position in the hidden word.
	void updateHint(char letter) {
		
		// Converts the hint and the hidden word into char arrays 
		// so that each char can be compared and replace as needed.
		char[] hintChars = hint.toCharArray();
		char[] hiddenWordChars = word.hiddenWord.toCharArray();
		
		// Cycles through each letter in hidden word by index.
		for (int i = 0; i < hiddenWordChars.length; i++) {
			
			// Replaces the corresponding dash in hint if the 
			// letter matches the letter in the hidden word.
			if (hiddenWordChars[i] == letter) {
				
				hintChars[i] = letter;
			}
		}
		
		// Sets hint to the new hint as a string. 
		hint = new String(hintChars);
	}
	
	// Gets all the game components.
	void initializeGame(String difficulty) {
		
		getHiddenWord(difficulty); // Gets the hidden word.
		getHint();				   // Creates the hint.
		board.initializeBoard();   // Creates the hang man.
		
	}
	
	// Displays the hint and the hang man to the console.
	void displayGame() {
		
		board.displayBoard();
		System.out.println(hint);
	}
	
	
	// Sets game over to true when the max number of 
	// strikes is reached or if the hidden word is guessed.
	boolean gameOver() {
		
		if (board.strikes == 8 || word.hiddenWord.equals(hint)) {
			
			return true;
		}

		return false;
	}
	
	
	// Updates the hang man graphic and updates incorrect guesses. 
	void updateGameBoard(char letter) {
		
		board.updateBoard(letter);
	}
	
	
	// Returns true if the hidden word was guessed.
	void gameWon() {
		
		// When the game over condition is met it displays the 
		// appropriate message depending if the game was won or lost. 
		if (gameOver()) {
			
			System.out.println(word.hiddenWord);
			
			if (word.hiddenWord.equals(hint)) {
				
				System.out.println("You won!");
			}
			else {
				
				System.out.println("Game Over!");
			}
		}
	}
	
}

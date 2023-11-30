package hangman;

public class Game {
	
	public String hiddenWord;
	public String hint;
	Board board = new Board();
	
	void get_hidden_word() {
		hiddenWord = "bananas";
	}
	
	void get_hint() {
		int hint_len = hiddenWord.length();


		for (int i = 0; i < hint_len; i++)
		{
			hint += "-";
		}
	}
	
	
	void update_hint(char letter) {
		
		int i = 0;
		for (char hidden_letter : hiddenWord.toCharArray())
		{
			if (hidden_letter == letter)
			{
				char[] hintChars = hint.toCharArray();
				hintChars[i] = letter;
				hint = new String(hintChars);
			}
			i++;
		}
	}
	
	
	void initialize_game() {
		
		get_hidden_word();
		get_hint();
		board.initialize_board();
		
	}
	
	
	void display() {
		
		board.display_board();
		System.out.println("\n" + hint);
	}
	
	
	void add_strike(char letter) {
		
		board.update_board(letter);
	}
	
	
	boolean game_over() {
		
		if (board.get_strikes() == 8 || hiddenWord == hint)
		{
			return true;
		}

		return false;
	}
	
	
	void update_game_board(char letter) {
		board.update_board(letter);
	}
	
	
	boolean check_letter(char letter) {
		
		for (char hidden_letter : hiddenWord.toCharArray())
		{
			if(hidden_letter == letter)
			{
				return true;
			}
		}
		
		return false;
	}
	
	
	void game_won() {
		
		if (game_over())
		{
			if (hiddenWord == hint){
				System.out.println("You won!");
			}
			else
			{
				System.out.println(hiddenWord);
				System.out.println("Game Over!");
			}
		}
	}
	
}

package hangman;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Random;

public class Word {
	
	public String hiddenWord;
	private String[] words;
	
	void getHiddenWord(String difficulty){
		
		importWords(difficulty);
		Random rand = new Random();
		int index = rand.nextInt(words.length) + 1;
		hiddenWord = words[index];
	}
	
	private void importWords(String difficulty) {
		
		try {
			words = Files.readAllLines(Paths.get("src/hangman/" + difficulty + ".txt")).toArray(new String[0]);;
		}
		catch (Exception e) {
			System.out.println("Error opening file.");
		}
	}
}

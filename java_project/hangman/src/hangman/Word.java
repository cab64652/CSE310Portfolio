package hangman;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Random;


// This class gets a random word from a text document.
public class Word {
	
	private String[] words;
	public String hiddenWord;
	
	// Reads in a list of words from text file into an array. 
	void getHiddenWord(String difficulty) {
		
		// Imports a list of words from the text file 
		// with the name stored in the difficulty variable.
		importWords(difficulty);
		// Gets a random number to use as a index for a random word. 
		Random rand = new Random();
		int index = rand.nextInt(words.length) + 1;
		hiddenWord = words[index];
	}
	
	
	// Imports a text file into an array. 
	private void importWords(String difficulty) {
		
		try {
			words = Files.readAllLines(Paths.get("src/hangman/" + difficulty + ".txt")).toArray(new String[0]);;
		}
		catch (Exception e) {
			System.out.println("Error opening file.");
		}
	}
}

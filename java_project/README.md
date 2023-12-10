# Overview

{Important! Do not say in this section that this is college assignment. Talk about what you are trying to accomplish as a software engineer to further your learning.}

This program is a hang man game that is played from the terminal. It takes a letter as user input and compares that letter to each letter in a hidden word and reveals correct guesses and records incorrect guess and draws a hang man graphic using symbols on a key board. It reads in words from a text document into an array and uses a randomly generated number to get a random word from the array by index to use as the hidden word. The program will play multiple games until the user quits the program.

The purpose for me writing this program was to get an introduction to the Java programming language and learn the basic syntax of Java.

[Software Demo Video](https://youtu.be/djEm8smfY38)

# Development Environment

This program was written using the Eclipse IDE for Java developers.

This program was written using the Java programming language. The java.util.Scanner library was imported to get user input from the terminal. The java.nio.file.Files and java.nio.file.Paths libraries were imported to get information from a text file. The Paths library handled getting the path to the text file and the File library handled reading in the text from the text file. The java.util.Random library was also used to generate a random number.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [W3 Schools](https://www.w3schools.com/java)
- [Geeks for Geeks](https://www.geeksforgeeks.org/java/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Add error handling so that when a word is put in rather than a letter it will ask for another input rather than taking the first of the word inputted.
- Refine the words in each difficulty category so that they better reflect the difficulty selection.
- Add functionality to stop duplicate letters from being guessed.
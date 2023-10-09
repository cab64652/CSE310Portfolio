# Overview

This is a simple encryption and decryption program. It asks the user for a message and a key and uses the key to either encrypt or decrypt the message depending of the user's selection. The program takes the message and converts it to a number. It then xor's the key and the number to either encrypt or decrypt the message. For encryption it returns the encrypted message as a long number. In the decryption it then separates the numbers into groups of two and converts them back into letter and returns the decrypted message.

I wrote this program to give me an introduction to the Rust Language. It allowed me to practice using variables both mutable and immutable, the different kind of loops, conditionals, and functions.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running and a walkthrough of the code. Focus should be on sharing what you learned about the language syntax.}

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

This program was created using VS code and Cargo, a build system and package manager for Rust.

This program was created using the Rust programming language and the standard input/output library.

# Useful Websites

- [Stack Over Flow](https://stackoverflow.com/)
- [Rust Language](https://doc.rust-lang.org/stable/book/)
- [YouTube - Lets Get Rusty](https://www.youtube.com/watch?v=OX9HJsJUDxA&list=PLai5B987bZ9CoVR-QEIN9foz4QCJ0H2Y8&index=1)

# Future Work

- Fix the overflow error so that this program can handle large messages.
- Using a better encryption algorithm that wold be more secure.
- Make it so all the characters on the keyboard are usable. 
- Make it so it could encrypt more than just inputted messages.
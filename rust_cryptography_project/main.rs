use std::io;


fn main() {
    /* Prompts the user for a message and to encrypt or decrypt 
       and a key used for the encryption or decryption.  */
    println!("Enter your message: ");
    let mut message= String::new(); 

    io::stdin()     // Stores input into a variable.
        .read_line(&mut message)
        .expect("Failed to read line.");

    println!("Enter the key: ");
    let mut key = String::new();

    io::stdin()     // Stores input into a variable.
        .read_line(&mut key)
        .expect("Failed to read line.");

    // Convert key from a string to an unsigned integer.
    let int_key: u128 = key.trim().parse()
        .expect("Invalid Input");
    
    // Will loop until a valid input is given.
    // Allows the user to select to either encrypt or decrypt a message.
    loop {
        let mut choice = String::new();
        println!("Encryption (e) or Decryption (d): ");
        
        io::stdin()
            .read_line(&mut choice)
            .expect("Failed to read line.");

        /* Using the encrypt() and decrypt() the corresponding version
         of the message will be displayed in the terminal. */
        if choice.trim() == "e" {
            encrypt(message, int_key);
            break;    
        } 
        else if choice.trim() == "d" {
            decrypt(message, int_key);
            break;
        }
        else {
            println!("Invalid input. Please type 'e' or 'n'.")
        }
    };

}


/* Takes a message as a string and a key as an unsigned integer
 to encrypt a message and display it to the terminal. */
 
fn encrypt(message: String, key: u128) {

    // Gets rid of extra characters not part of the message.
    let message = message.trim();

    print!("Your message is: ");

    let mut code = String::new();

    /* Takes each letter in the message and converts it to uppercase gets the
    integer form of the letter. The integer is then converted back to a string
    so that the numbers can be concatenated back together to ge the encrypted message. */ 
    for letter in message.chars(){
        let int = letter.to_ascii_uppercase() as u8;
        let str = int.to_string();
        code.push_str(&str);
    }

    /* Converts the string of numbers to an integer so that it can be 
    passed to the encode function to finish the encryption. */
    let code_int = code.trim().parse()
    .expect("Error, number not found");
    
    // Uses encode() to finish encryption and displays the encrypted message.
    let coded_message = encode(code_int, key);
    println!("{}", coded_message);
}


/* Takes a string of numbers and an encryption key to
 decrypt the number string into plain text. */

fn decrypt(message: String, key: u128) {
    
    
    /* Converts the message into an integer so it can be passed
    to encode() so the messaged can be decrypted. */
    let int: u128 = message.trim().parse()
    .expect("Error, number not found");

    // Uses encode to get the decrypted message as an integer.
    let code = encode(int, key);

    // Converts the integer from encode to a string so it can be iterated through.
    let code_str = code.to_string();
    print!("Your message is: ");

    /* Iterates through the string of numbers so they 
    can be converted back into letters. */
    let mut ascii = String::new();
    let mut counter = 0;
    for number in code_str.chars() {

        /* Uses counter and % to group numbers in groups of 
        two for the integer to letter conversion. */
        ascii.push(number);
        counter += 1;

        if counter % 2 == 0 {
            
            /* Once a group of two numbers is found it is converted to 
            an integer and so it can be converted back into a letter. */
            let int : u8 = ascii.trim().parse()
                .expect("Error, number not found");

            /* Displays the letter to the terminal and clears the ascii 
            string so a new group of numbers can be converted */
            print!("{}", int as char);
            ascii.clear();
        }
    }
}


/* Uses a basic symmetric encryption algorithm to both encrypt and decrypt a 
message by xor the message and the key to get a the encrypted or decrypted message. */

fn encode(code: u128, key: u128) -> u128 {
    return code ^ key;
}
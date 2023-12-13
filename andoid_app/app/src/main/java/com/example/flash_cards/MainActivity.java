package com.example.flash_cards;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.ToggleButton;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {


    ToggleButton toggleQA = new ToggleButton(this);
    Button buttonNext = new Button(this);
    String[] questionCards;
    String[] answerCards;
    String question;
    String answer;
    int index = 0;
    TextView flashCard;

//    Sets up the android screen.
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Sets up the toggle button to with the question and answer.
        toggleQA = findViewById(R.id.toggle_QA);
        toggleQA.setTextOn(answerCards[index]);
        toggleQA.setTextOff(questionCards[index]);
        toggleQA.setChecked(true);

        // Sets up the next button to cycle to the next flashcard.
        buttonNext = findViewById(R.id.nextButton);
        flashCard = findViewById(R.id.text);

        // Toggles between the question and answer for the flashcard when the button was touched.
        toggleQA.setOnClickListener(v -> {
            // Makes sure the question is shown first.
            if(toggleQA.isChecked()){

                flashCard.setText(answerCards[index]);
            }
            else{
                flashCard.setText(questionCards[index]);
            }

        });

        // Goes to the next flash card when the next button in touched.
        buttonNext.setOnClickListener(v -> {
            // Adds 1 to the index or sets index to 0 if index out of range exception is thrown.
            try {
                index++;
            } catch (Exception e) {
                index = 0;
            }

        });
    }
}
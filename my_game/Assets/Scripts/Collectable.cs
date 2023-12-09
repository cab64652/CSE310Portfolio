using UnityEngine;
using TMPro;

public class Collectable : MonoBehaviour
{   
    public GameObject player;
    public GameObject bot;
    public GameObject startPosition;
    public LayerMask homeBase;
    private Vector2 target;
    public TMP_Text scoreText;
    public float followDistance = 0.75f;
    public float speed = 5;
    private float timer;
    private bool collected = false;
    public int score;
    private int timeDelay;


    void Start()
    {
        target = transform.position; // Keeps the collectable stationary at the start of the game.
        timeDelay = 1;
        score = 0;
        scoreText.text = "Score: ";
    }


    void Update()
    {
        // Checks if the player overlaps the collectable and sets collected to true.
        if (Vector2.Distance(this.transform.position, player.transform.position) < 0.5f)
        {
            collected = true;
        }

        // Makes the collectable follow the player when collected is true.
        if (collected)
        {
            // Sets the target location of the collectable to the players 
            // position minus the following distance.
            target = player.transform.position - (player.transform.position.normalized * followDistance);
            // Moves the collectable to the target location at a constant speed.
            transform.position = Vector3.MoveTowards(transform.position, target, speed * Time.deltaTime);
        }

        // Moves the collectable back to the start
        // position if the player enters the home base.
        if (Physics2D.OverlapCircle(player.transform.position, 0.1f, homeBase))
        {
            // Sets the position of the collectable to the start position. 
            transform.position = startPosition.transform.position;
            // Sets the target position back to the player position so the
            // collectable wont keep following the player.
            target = transform.position;
            collected = false;
        }
        
        // Cycles the timer.
        timer += Time.deltaTime; 

        // Adds 1 to the score every second the collectable is collected. 
        // Checks that the collectable is not in the start location and
        // the appropriate time has passed before updating the score.
        if (transform.position != startPosition.transform.position && timer >= timeDelay)
        {
            timer = 0f;
            score++;
        }

        // Subtracts 5 from the score when the bot touches the player.
        // Checks to see if the bot touches the player and uses the
        // timer to make sure that score is only updated once. 
        if (Vector2.Distance(player.transform.position, bot.transform.position) < 0.85f && timer >= timeDelay)
        {
            timer = 0f;
            score -= 5;
        }
    }
}
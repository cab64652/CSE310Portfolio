using UnityEngine;

public class Player : MonoBehaviour
{   
    public GameObject startPosition;
    public GameObject bot;
    private Vector3 target;
    private Vector2 direction;
    private float angle;
    public float speed;
   

    void Start() 
    {
        target = transform.position; // Keeps the players stationary at the start of the game.
    }

    void Update()
    {
        // Gets the mouse position when the button is released. 
        if(Input.GetMouseButtonUp(0))
        {
            // Sets the target position using the camera fixes the z axis.
            target = Camera.main.ScreenToWorldPoint(Input.mousePosition);
            target.z = transform.position.z;

            // Changes the direction the player is facing.
            direction = target - transform.position;
            direction.Normalize();
            angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;
        }

        // Moves the player back to the start position if the bot touches the player.
        if (Vector2.Distance(this.transform.position, bot.transform.position) < 0.75f)
        {
            transform.position = startPosition.transform.position;
            target = transform.position;
        }
        
        // Uses the target position to move the player at a constant speed. 
        transform.position = Vector3.MoveTowards(transform.position, target, speed * Time.deltaTime);
        transform.rotation = Quaternion.Euler(Vector3.forward * angle);
        
    }
}
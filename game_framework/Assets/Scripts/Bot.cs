using UnityEngine;

public class Bot : MonoBehaviour
{
    public GameObject player;
    public GameObject startPosition;
    public float speed;
    public LayerMask homeBase;
    private float angle;
    private Vector2 direction;
    private Vector3 target;
    
    void Update()
    {
        // Sets the target position to the players position.
        target = player.transform.position;

        // Returns the bot to the start position if the player enters home base.
        if (Physics2D.OverlapCircle(target, 0.1f, homeBase))
        {
            target = startPosition.transform.position;
        }

        // Sets the direction of the bot to face the player. 
        direction = target - transform.position;
        direction.Normalize();
        angle = Mathf.Atan2(direction.y, direction.x) * Mathf.Rad2Deg;

        // Move the bot and adjusts the direction it is facing at a constant speed. 
        transform.position = Vector2.MoveTowards(this.transform.position, target, speed * Time.deltaTime);
        transform.rotation = Quaternion.Euler(Vector3.forward * angle);
    }
}

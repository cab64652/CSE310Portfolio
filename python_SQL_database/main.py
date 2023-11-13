import sqlite3

def main():
    
    connection = sqlite3.connect("python_SQL_database/data.db")
    cursor = connection.cursor()

    create_lure_table = """CREATE TABLE IF NOT EXISTS
        lures(lure_id INTEGER PRIMARY KEY, name TEXT, color TEXT, lost TEXT)"""
    
    cursor.execute(create_lure_table)

    # create_lure_stats_table = """CREATE TABLE IF NOT EXISTS
    #     stats(lure_id INTEGER, fish_num INTEGER, fish_type TEXT, 
    #     location TEXT, weather TEXT, water_cond TEXT, 
    #     FOREIGN KEY(lure_id) REFERENCES lures(lure_id))"""
    
    # cursor.execute(create_lure_stats_table)

    create_fish_table = """CREATE TABLE IF NOT EXISTS
        fish(lure_id INTEGER, trout INTEGER, bass INTEGER, catfish INTEGER, muskie INTEGER,
        FOREIGN KEY(lure_id) REFERENCES lures(lure_id))"""
    
    cursor.execute(create_fish_table)

    choice = None
    while not choice == 0:
        display_menu_1()
        choice = is_int(input("Selection: "))

        match choice:
            case 0:
                break

            case 1:
                add_lure(cursor)
                print_lures(cursor)

            case 2:
                find_lure(cursor)

            case 3:
                update_lure(cursor)
                print_lures(cursor)

            case 4:
                delete_lure(cursor)
                print_lures(cursor)

            case 9:
                print_lures(cursor)

            case _:
                print("Invalid input\n")
        
    connection.commit()
    connection.close()



def display_menu_1():
    print("0. Quit\n"
          "1. Add Lure\n"
          "2. Find Lure\n"
          "3. Update Lure\n"
          "4. Remove Lure\n"
          "5. Suggest Lure")


def print_lures(cursor):

    for row in cursor.execute("SELECT * FROM lures"):
        print(f"ID: {row[0]}, Name: {row[1]}, Color: {row[2]}, Lost: {row[3]}")

        query = """SELECT * from fish WHERE lure_id = ?"""
        cursor.execute(query, (row[0],))

        fish_row = cursor.fetchone()
        print(f"Name: {row[1]}, ID: {fish_row[0]} Trout: {fish_row[1]}, Bass: {fish_row[2]}, Catfish: {fish_row[3]}, Muskie: {fish_row[4]}")
    

def is_int(num):
    try:
        return int(num)
    except:
        print("Invalid Input\n")
        return False


def add_lure(cursor):

    name = input("Enter lure name: ").lower()
    color = input("Enter lure color: ").lower()
    lost = "no"
    id = is_int(input("enter id: "))
    if id == False:
        return

    new_row_lures = (id, name, color, lost)
    new_row_fish = (id, 0, 0, 0, 0)

    
    cursor.execute("INSERT INTO lures VALUES (?, ?, ?, ?)", new_row_lures)
    cursor.execute("INSERT INTO fish VALUES (?, ?, ?, ?, ?)", new_row_fish)


def delete_lure(cursor):

    id = is_int(input("Enter the ID of the lure to be deleted: "))
    if id == False:
        return
    
    cursor.execute("DELETE FROM lures WHERE lure_id=?", id)
    cursor.execute("DELETE FROM fish WHERE lure_id=?", id)


def find_lure(cursor):

    search_id = is_int(input("Enter the lure ID to search for: "))
    if search_id == False:
        return
    
    query = """SELECT * from lures WHERE lure_id = ?"""
    cursor.execute(query, (search_id,))

    row = cursor.fetchone()
    print(f"Name: {row[1]}, Color: {row[2]}, Lost: {row[3]}")    


def update_lure(cursor):

    id = is_int(input("Enter the ID of the lure to update: "))
    if id == False:
        return
    
    field = input("Enter the field of the lure to update: ")

    match field:
        case "lost":
            update_lost(cursor, id)
        
        case "fish":
            update_fish(cursor, id)
        
        case _:
                print("Invalid input\n")


def update_lost(cursor, id):

    lost_value = input("Enter the new value: ").lower()

    update_values = (lost_value, id)
    cursor.execute("UPDATE lures SET lost = ? WHERE lure_id = ?", update_values)


def display_menu_2():

    print("0. Back\n"
          "1. Trout\n"
          "2. Bass\n"
          "3. Catfish\n"
          "4. Muskie")
    

def update_fish(cursor, id):

    num_fish = is_int(input("Number of fish caught: "))
    if num_fish == False:
        return
    
    display_menu_2()
    fish = is_int(input("Enter the type of fish to update: "))
    if fish == False:
        return

    cursor.execute("""SELECT * from fish WHERE lure_id = ?""", (id,))
    row = cursor.fetchone()    

    cur_num_fish = int(row[fish])
    new_num_fish = cur_num_fish + num_fish
    update_values = (new_num_fish, id)

    match fish:
        case 0:
            return
        
        case 1:
            cursor.execute("UPDATE fish SET trout = ? WHERE lure_id = ?", update_values)

        case 2:
            cursor.execute("UPDATE fish SET bass = ? WHERE lure_id = ?", update_values)

        case 3:
            cursor.execute("UPDATE fish SET catfish = ? WHERE lure_id = ?", update_values)
        
        case 4:
            cursor.execute("UPDATE fish SET muskie = ? WHERE lure_id = ?", update_values)
        
        case _:
                print("Invalid Selection\n")




if __name__ == "__main__":
    main()
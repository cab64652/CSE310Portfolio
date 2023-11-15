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
    while choice != 7:

        display_menu_1()
        choice = is_int(input("Selection: "))

        match choice:

            case 1:
                add_lure(cursor)

            case 2:
                print_lures(cursor)

            case 3:
                find_lure(cursor)

            case 4:
                update_lure(cursor)

            case 5:
                delete_lure(cursor)

            case 6:
                suggest_lure(connection)

            case 7:
                break
            
            case _:
                print("Invalid Selection\n")
        
    connection.commit()
    connection.close()



def display_menu_1():
    print("\n1. Add Lure\n"
          "2. Display All Lures\n"
          "3. Find Lure\n"
          "4. Update Lure\n"
          "5. Remove Lure\n"
          "6. Suggest Lure\n"
          "7. Quit")


def print_lures(cursor):

    for row in cursor.execute("\nSELECT * FROM lures"):
        print(f"ID: {row[0]}, Name: {row[1]}, Color: {row[2]}, Lost: {row[3]}")


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
    
    cursor.execute("DELETE FROM lures WHERE lure_id = ?", (id,))
    cursor.execute("DELETE FROM fish WHERE lure_id = ?", (id,))


def find_lure(cursor):

    search_id = is_int(input("Enter the lure ID to search for: "))
    if search_id == False:
        return
    
    try:
        cursor.execute("""SELECT * from lures WHERE lure_id = ?""", (search_id,))
        row = cursor.fetchone()

        print(f"\nName: {row[1]}, Color: {row[2]}, Lost: {row[3]}")    

        cursor.execute("""SELECT * from fish WHERE lure_id = ?""", (row[0],))
        fish_row = cursor.fetchone()

        print("Fish Caught:")
        print(f"Trout: {fish_row[1]}, \nBass: {fish_row[2]}, \nCatfish: {fish_row[3]}, \nMuskie: {fish_row[4]}")

    except:
        print("ID Not Found")


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

    print("\n0. Back\n"
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


def suggest_lure(connection):

    display_menu_2()

    fish = is_int(input("Enter the target fish: "))
    if fish == False:
        return

    max = -1
    # max_id = -1
    suggested_lure = None
    # for row in cursor.execute("SELECT * FROM fish"):
    #     if int(row[fish]) > max:
    #         max = int(row[fish])
    #         max_id = int(row[0])

    cursor1 = connection.cursor()
    cursor2 = connection.cursor()

    cursor1.execute('SELECT * FROM lures')
    cursor2.execute('SELECT * FROM fish')

    for row1, row2 in zip(cursor1, cursor2):
        if int(row2[fish]) > max and row1[3] == "no":
            max = int(row2[fish])
            # max_id = int(row2[0])
            suggested_lure = row1 + tuple([max])

    # print(suggested_lure)


    # cursor.execute("""SELECT * from lures WHERE lure_id = ?""", (max_id,))
    # suggested_lure = cursor.fetchone() 

    print("\nSuggested Lure") 
    print(f"Name: {suggested_lure[1]} \nColor: {suggested_lure[2]} \nNumber of target fish caught: {suggested_lure[4]}")   



if __name__ == "__main__":
    main()
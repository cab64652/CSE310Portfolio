import sqlite3

fish_list = ["place holder", "trout", "bass", "catfish", "muskie"]
water_list = ["place holder", "clear", "stained", "muddy"]


def main():
    
    connection = sqlite3.connect("python_SQL_database/data.db")
    cursor = connection.cursor()

    create_lure_table = """CREATE TABLE IF NOT EXISTS
        lures(lure_id INTEGER PRIMARY KEY, name TEXT, color TEXT, lost TEXT)"""
    
    cursor.execute(create_lure_table)

    create_fish_table = """CREATE TABLE IF NOT EXISTS
        fish(lure_id INTEGER, trout INTEGER, bass INTEGER, catfish INTEGER, 
        muskie INTEGER, FOREIGN KEY(lure_id) REFERENCES lures(lure_id))"""
    
    cursor.execute(create_fish_table)

    create_water_table = """CREATE TABLE IF NOT EXISTS
    water(lure_id INTEGER, clear INTEGER, stained INTEGER, muddy INTEGER,
    FOREIGN KEY(lure_id) REFERENCES lures(lure_id))"""
    
    cursor.execute(create_water_table)

    choice = -1
    while choice:
        
        choice = get_int(get_menu_1())

        match choice:
            case 0:
                break
            
            case 1:
                add_lure(cursor)
                connection.commit()

            case 2:
                # print_lures(cursor)
                print_lures(connection)

            case 3:
                search_id = get_int("Enter the lure ID to search for: ")
                row = find_lure(cursor, search_id)
                print_lure_info(row, cursor)

            case 4:
                update_lure(cursor)
                connection.commit()

            case 5:
                delete_lure(cursor)
                connection.commit()

            case 6:
                suggest_lure(connection)

            case _:
                print("Invalid Selection\n")
        
    connection.commit()
    connection.close()


def get_menu_1():
    return ("\n0. Quit/Back\n"
            "1. Add Lure\n"
            "2. Display All Lures\n"
            "3. Find Lure\n"
            "4. Update Lure\n"
            "5. Remove Lure\n"
            "6. Suggest Lure\n"
            "Selection: ")


# def print_lures(cursor):

#     for row in cursor.execute("\nSELECT * FROM lures"):
#         print(f"ID: {row[0]}, Name: {row[1]}, Color: {row[2]}, Lost: {row[3]}")

def print_lures(connection):

    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()

    cursor1.execute('SELECT * FROM lures')
    cursor2.execute('SELECT * FROM fish')
    cursor3.execute('SELECT * FROM water')

    for row1, row2, row3 in zip(cursor1, cursor2, cursor3):
        print(f"ID: {row1[0]}, Name: {row1[1]}, Color: {row1[2]}, Lost: {row1[3]}")
        print(row2)
        print(f"{row3}\n")


def print_lure_info(lure_row, cursor):
    
    if lure_row:
        print(f"\nName: {lure_row[1]}, Color: {lure_row[2]}, Lost: {lure_row[3]}")    

        cursor.execute("""SELECT * from fish WHERE lure_id = ?""", (lure_row[0],))
        fish_row = cursor.fetchone()

        cursor.execute("""SELECT * from water WHERE lure_id = ?""", (lure_row[0],))
        water_row = cursor.fetchone()

        print("Fish Caught:")
        for i in range(1, len(fish_list)):
            print(f"{fish_list[i].capitalize()}: {fish_row[i]}")
        
        for i in range(1, len(water_list)):
            print(f"{water_row[i]} caught in {water_list[i]} water.")  


    else:
        print("ID Not Found")


def get_int(message):

    num = None

    while type(num) != int:
        num = input(message)
        try:
            return int(num)
        except:
            print("Invalid Input")
        

def add_lure(cursor):

    name = input("Enter lure name: ").lower()
    if name == '0':
        return
    color = input("Enter lure color: ").lower()
    if color == '0':
        return
    lost = "no"

    cursor.execute('SELECT * FROM lures ORDER BY ROWID DESC LIMIT 1')    
    last = cursor.fetchone()

    if last:
        id = int(last[0]) + 1
    else:
        id = 1

    new_row_lures = (id, name, color, lost)
    new_row_fish = (id, 0, 0, 0, 0)
    new_row_water = (id, 0, 0, 0)

    cursor.execute("INSERT INTO lures VALUES (?, ?, ?, ?)", new_row_lures)
    cursor.execute("INSERT INTO fish VALUES (?, ?, ?, ?, ?)", new_row_fish)
    cursor.execute("INSERT INTO water VALUES (?, ?, ?, ?)", new_row_water)


def delete_lure(cursor):

    id = get_int("Enter the ID of the lure to be deleted: ")
    
    cursor.execute("DELETE FROM lures WHERE lure_id = ?", (id,))
    cursor.execute("DELETE FROM fish WHERE lure_id = ?", (id,))
    cursor.execute("DELETE FROM water WHERE lure_id = ?", (id,))


def find_lure(cursor, search_id):
    
    cursor.execute("""SELECT * from lures WHERE lure_id = ?""", (search_id,))
    row = cursor.fetchone()

    return row
    

def update_lure(cursor):

    id = get_int("Enter the ID of the lure to update: ")
    if not id:
        return

    found = find_lure(cursor, id)

    if found:

        print(f"ID: {found[0]}, Name: {found[1]}, Color: {found[2]}, Lost: {found[3]}")
        field = input("Enter the field of the lure to update (fish/lost): ")
        if field == '0':
            return

        if field == "lost":
            update_lost(cursor, id)
            
        elif field == "fish":
            update_fish(cursor, id)
            
        else:
            print("Invalid input\n")

    else:
        print("ID Not Found")


def update_lost(cursor, id):

    lost_value = input("Enter the new value: ").lower()
    if lost_value == '0':
        return

    update_values = (lost_value, id)
    cursor.execute("UPDATE lures SET lost = ? WHERE lure_id = ?", 
                   update_values)


def display_menu_2():

    return ("\n0. Back\n"
          "1. Trout\n"
          "2. Bass\n"
          "3. Catfish\n"
          "4. Muskie")


def display_menu_3():

    return("\n0. Back\n"
          "1. Clear\n"
          "2. Stained\n"
          "3. Muddy")
    

def update_fish(cursor, id):

    num_fish = get_int("Number of fish caught: ")
    if not num_fish:
        return
    
    print(display_menu_2())
    fish = get_int("Enter the type of fish to update: ")
    if not fish:
        return

    print(display_menu_3())
    water = get_int("Enter the the water clarity: ")
    if not water:
        return

    cursor.execute("""SELECT * from fish WHERE lure_id = ?""", (id,))
    row_fish = cursor.fetchone()    

    cur_num_fish = int(row_fish[fish])
    new_num_fish = cur_num_fish + num_fish
    update_fish = (new_num_fish, id)

    cursor.execute("""SELECT * from water WHERE lure_id = ?""", (id,))
    row_water = cursor.fetchone() 

    cur_num_water = int(row_water[water])
    new_num_water = cur_num_water + num_fish
    update_water = (new_num_water, id)

    cursor.execute(f"UPDATE fish SET {fish_list[fish]} = ? WHERE lure_id = ?", update_fish)
    cursor.execute(f"UPDATE water SET {water_list[water]} = ? WHERE lure_id = ?", update_water)


def suggest_lure(connection):

    fish = get_int(display_menu_2() + "\nEnter the target fish: ")
    if not fish:
        return
    water = get_int(display_menu_3() + "\nEnter the water conditions: ")
    if not water:
        return

    max = -1
    suggested_lure = None

    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()

    cursor1.execute('SELECT * FROM lures')
    cursor2.execute('SELECT * FROM fish')
    cursor3.execute('SELECT * FROM water')

    for row1, row2, row3 in zip(cursor1, cursor2, cursor3):
        if int(row2[fish]) + int(row3[water]) > max and row1[3] == "no":
            max = int(row2[fish])
            suggested_lure = row1 + tuple([max])

    print(f"\nSuggested lure for {fish_list[fish]} in {water_list[water]} water:") 
    print(f"Name: {suggested_lure[1]} \nColor: {suggested_lure[2]} "
          f"\nNumber of target fish caught: {suggested_lure[4]}")   



if __name__ == "__main__":
    main()
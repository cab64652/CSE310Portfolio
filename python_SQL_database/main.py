import sqlite3

fish_list = ["place holder", "trout", "bass", "catfish", "muskie"]
water_list = ["place holder", "clear", "stained", "muddy"]


def main():
    
    # Sets up the connection to the database and the 
    # cursor to access the information in the database.
    connection = sqlite3.connect("python_SQL_database/data.db")
    cursor = connection.cursor()

    # Creates a table if one doesn't already exist to 
    # hold identifying information for the lures.
    create_lure_table = """CREATE TABLE IF NOT EXISTS
        lures(lure_id INTEGER PRIMARY KEY, name TEXT, color TEXT, lost TEXT)"""
    
    cursor.execute(create_lure_table)

    # Creates a table if one doesn't already exist to hold 
    # information about the different fish caught by the lure.
    create_fish_table = """CREATE TABLE IF NOT EXISTS
        fish(lure_id INTEGER, trout INTEGER, bass INTEGER, catfish INTEGER, 
        muskie INTEGER, FOREIGN KEY(lure_id) REFERENCES lures(lure_id))"""
    
    cursor.execute(create_fish_table)

    # Creates a table if one doesn't already exist to hold  information about
    # the different water condition  when the fish was caught by the lure.
    create_water_table = """CREATE TABLE IF NOT EXISTS
    water(lure_id INTEGER, clear INTEGER, stained INTEGER, muddy INTEGER,
    FOREIGN KEY(lure_id) REFERENCES lures(lure_id))"""
    
    cursor.execute(create_water_table)

    choice = -1
    while choice:
        
        # Gets an integer input.  
        choice = get_int(get_main_menu())

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


# Gets a menu that can be displayed or passed to a function.
def get_main_menu():
    return ("\n0. Quit/Back\n"
            "1. Add Lure\n"
            "2. Display All Lures\n"
            "3. Find Lure\n"
            "4. Update Lure\n"
            "5. Remove Lure\n"
            "6. Suggest Lure\n"
            "Selection: ")


# # Displays each lure in the database. 
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


# Displays all the information of a single lure including the number 
# of each fish caught and the water conditions they were caught in.
def print_lure_info(lure_row, cursor):
    
    # If the info about the lure is not null.
    if lure_row:

        # Displays lure description.
        print(f"\nName: {lure_row[1]}, Color: {lure_row[2]}, Lost: {lure_row[3]}")    

        # Gets the information about the number of each fish caught.
        cursor.execute("""SELECT * from fish WHERE lure_id = ?""", (lure_row[0],))
        fish_row = cursor.fetchone()

        # Gets the information about the number of fish caught in each water condition.
        cursor.execute("""SELECT * from water WHERE lure_id = ?""", (lure_row[0],))
        water_row = cursor.fetchone()

        # Uses the global fish list to access the name of each fish and uses 
        # the index to get the corresponding information from the database.
        print("Fish Caught:")
        for i in range(1, len(fish_list)):
            print(f"{fish_list[i].capitalize()}: {fish_row[i]}")
        
        # Uses the global water list to access the name of each type of water and 
        # uses the index to get the corresponding information from the database.
        for i in range(1, len(water_list)):
            print(f"{water_row[i]} caught in {water_list[i]} water.")  


    else:
        print("ID Not Found")


# Takes a message as input and returns an integer.
def get_int(message):

    num = None

    # Continues to receive and try and convert the user input 
    # into an integer until it passes the try except statement.
    while type(num) != int:
        num = input(message)
        try:
            return int(num)
        except:
            print("Invalid Input")
        

def add_lure(cursor):

    # Gets the name and color of the lure or goes back if 0 is entered.
    name = input("Enter lure name: ").lower()
    if name == '0':
        return
    
    color = input("Enter lure color: ").lower()
    if color == '0':
        return
    
    # Sets all the default information for the other tables in the database. 
    lost = "no"
    new_row_lures = (id, name, color, lost)
    new_row_fish = (id, 0, 0, 0, 0)
    new_row_water = (id, 0, 0, 0)

    # Gets the last lure ID from the database.
    cursor.execute('SELECT * FROM lures ORDER BY ROWID DESC LIMIT 1')    
    last = cursor.fetchone()

    # Sets the ID to 1 if there is no information in 
    # the table or sets the ID to the last ID plus one.
    if last:
        id = int(last[0]) + 1
    else:
        id = 1

    # Adds the new lure and the default information to the corresponding tables.
    cursor.execute("INSERT INTO lures VALUES (?, ?, ?, ?)", new_row_lures)
    cursor.execute("INSERT INTO fish VALUES (?, ?, ?, ?, ?)", new_row_fish)
    cursor.execute("INSERT INTO water VALUES (?, ?, ?, ?)", new_row_water)


def delete_lure(cursor):
    # Gets the ID of the lure to be deleted.
    id = get_int("Enter the ID of the lure to be deleted: ")
    
    # Removes the data from each table in the database. 
    cursor.execute("DELETE FROM lures WHERE lure_id = ?", (id,))
    cursor.execute("DELETE FROM fish WHERE lure_id = ?", (id,))
    cursor.execute("DELETE FROM water WHERE lure_id = ?", (id,))


def find_lure(cursor, search_id):
    
    # Returns a single row at the search ID.
    cursor.execute("""SELECT * from lures WHERE lure_id = ?""", (search_id,))
    row = cursor.fetchone()

    return row
    

def update_lure(cursor):

    # Gets the lure ID to update or returns if the ID does not exist. 
    id = get_int("Enter the ID of the lure to update: ")

    found = find_lure(cursor, id)

    if found:

        # Prints lure information for reference.
        print(f"ID: {found[0]}, Name: {found[1]}, Color: {found[2]}, Lost: {found[3]}")

        field = input("Enter the field of the lure to update (fish/lost): ")

        # Calls the corresponding function to update the information.
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

    # Updates the if the lure has been lost to 
    # help filter data for the suggest lure function.
    lost_value = input("Enter the new value: ").lower()
    if lost_value == '0':
        return

    update_values = (lost_value, id)
    cursor.execute("UPDATE lures SET lost = ? WHERE lure_id = ?", 
                   update_values)


# Gets a menu that can be displayed or passed to a function.
def get_fish_menu():

    return ("\n0. Back\n"
          "1. Trout\n"
          "2. Bass\n"
          "3. Catfish\n"
          "4. Muskie")

# Gets a menu that can be displayed or passed to a function.
def get_water_menu():

    return("\n0. Back\n"
          "1. Clear\n"
          "2. Stained\n"
          "3. Muddy")
    

def update_fish(cursor, id):

    # Gets the data for each corresponding field and returns if 0 was entered. 
    num_fish = get_int("Number of fish caught: ")
    if not num_fish:
        return
    
    print(get_fish_menu())
    fish = get_int("Enter the type of fish to update: ")
    if not fish:
        return

    print(get_water_menu())
    water = get_int("Enter the the water clarity: ")
    if not water:
        return

    # Gets the current data on the type and number of fish 
    # caught so that new data can be added to the old data.
    cursor.execute("""SELECT * from fish WHERE lure_id = ?""", (id,))
    row_fish = cursor.fetchone()    

    # Gets the current data on the type and number of fish 
    # caught so that new data can be added to the old data.
    cur_num_fish = int(row_fish[fish])
    new_num_fish = cur_num_fish + num_fish
    update_fish = (new_num_fish, id)

    # Gets the current data on the type water the fish were caught in and 
    # number of fish caught so that new data can be added to the old data.
    cursor.execute("""SELECT * from water WHERE lure_id = ?""", (id,))
    row_water = cursor.fetchone() 

    # Gets the current number of fish from the 
    # database and adds the new data to it.
    cur_num_water = int(row_water[water])
    new_num_water = cur_num_water + num_fish
    update_water = (new_num_water, id)

    # Updates the corresponding table with the new data.
    cursor.execute(f"UPDATE fish SET {fish_list[fish]} = ? WHERE lure_id = ?", update_fish)
    cursor.execute(f"UPDATE water SET {water_list[water]} = ? WHERE lure_id = ?", update_water)


# Gives a lure suggestion based on the target 
# fish to be caught and the water clarity.
def suggest_lure(connection):

    fish = get_int(get_fish_menu() + "\nEnter the target fish: ")
    if not fish:
        return
    water = get_int(get_water_menu() + "\nEnter the water conditions: ")
    if not water:
        return

    # Sets up 3 cursor so that data from each 
    # table can be evaluated at the same time.
    cursor1 = connection.cursor()
    cursor2 = connection.cursor()
    cursor3 = connection.cursor()

    cursor1.execute('SELECT * FROM lures')
    cursor2.execute('SELECT * FROM fish')
    cursor3.execute('SELECT * FROM water')
    
    # Max keeps track of the largest total of the target fish caught and 
    # the total number of fish caught in the specified water clarity.
    max = -1
    suggested_lure = None

    # For each row in the table the it determines if max 
    # will be updated and sets the suggested lure as needed.
    for row1, row2, row3 in zip(cursor1, cursor2, cursor3):
        if int(row2[fish]) + int(row3[water]) > max and row1[3] == "no":
            max = int(row2[fish])
            suggested_lure = row1 + tuple([max])

    # Displays the information on the suggested lure.
    print(f"\nSuggested lure for {fish_list[fish]} in {water_list[water]} water:") 
    print(f"Name: {suggested_lure[1]} \nColor: {suggested_lure[2]} "
          f"\nNumber of target fish caught: {suggested_lure[4]}")   



if __name__ == "__main__":
    main()
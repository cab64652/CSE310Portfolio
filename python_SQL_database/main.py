import sqlite3

def main():
    
    connection = sqlite3.connect("data.db")
    cursor = connection.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS
        lures(name TEXT, color TEXT, fish_num INTEGER, fish_type TEXT, location TEXT, weather TEXT, water_cond TEXT)"""
    
    cursor.execute(create_table)

    choice = None

    while choice is not 0:
        display_menu_1()
        choice = is_int(input("Selection: "))

        match choice:
            case 0:

            case 1:

            case 2:

            case _:
                print("Invalid input\n")
        

    connection.close()


def display_menu_1():
    print("0. Quit\n"
          "1. Add Lure\n"
          "2. Find Lure\n"
          "3. Update Lure")
    

def is_int(num):
    try:
        return int(num)
    except:
        print("Invalid Input\n")




if __name__ == "__main__":
    main()
# Overview

This program stores information about different fishing lures. It stores the name, color, number of fish caught, and the water conditions they were caught in. It adds, deletes and modifies data across different and tables and uses the data from multiple tables to give lure suggestions based the fish you are trying to catch and the water conditions. 

The purpose of writing this program was for me to learn how to use SQL databases in python. 


[Software Demo Video](https://youtu.be/XGwyf5e47Ek)

# Relational Database

The data for this database is separated into three tables that are all connect through a common ID. The first table gets descriptive data about the lure such as the name and the color. It also has a column to indicate weather a lure has be lost or not. Losing lures happens a lot when fishing and good lures are often replaced. The lost indicator is there to be able to keep all of the data about a lure that has been lost while still being able to exclude it from suggestions until a new lure can be purchased. The second table holds the totals of different types of fish caught by an individual lure and the last table records the total number of fish caught in different water conditions. This data is used to give lure suggestions based on the fish you are targeting and the clarity of the water you are fishing in.

# Development Environment

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

This program was written in Visual Studio Code using the Python programming language.
Data for this program was stored in an SQL database and the SQLite3 library was used access and modify data in the database.

# Useful Websites

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python sqlite3](https://docs.python.org/3.8/library/sqlite3.html)

# Future Work

- Add functionality to be able other types of fish to the database.
- Add functionality to be able to ask for another lure suggestion if the first one was not satisfactory.
- Add the ability for store pictures of the lures in the database.

import sqlite3

connection = sqlite3.connect("data.db")                                     # creating a connection
cursor = connection.cursor()                                                # cursor enables running of sql queries
create_table = "CREATE TABLE users(id int, username text, password text)"   # creating a table
cursor.execute(create_table)                                                # running the query to create the table
user = (1, "jose", 'abcd')                                          # storing a single user data into the users' table
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)
                                                                    # inserting many users
users = [
    (2, "rolf", '1234'),
    (3, "angel", 'kyeah')
]
cursor.executemany(insert_query, users)
select_query = "SELECT * FROM users"                                        # selecting data from the users' table
for row in cursor.execute(select_query):                                    # print the data in the users' table
    print(row)

connection.commit()
connection.close()

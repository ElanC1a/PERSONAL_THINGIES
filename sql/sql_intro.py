import sqlite3 as sql

data_base=sql.connect('info_user.db')

pointer=data_base.cursor()
# pointer.execute('''CREATE TABLE users(          
#     id integer,
#     name text,
#     surname text,
#     login text,
#     password text,
#     email text)
# ''')

#pointer.execute("INSERT INTO users VALUES (0, 'Peter', 'Jonshon', 'peter', 'banana', 'pet@gmail.com') ")                  #ddl -definition , dml -manupulation , dcl - control 

pointer.execute('SELECT * FROM users')
#print(pointer.fetchall)
# pointer.execute('DROP TABLE users')

data_base.commit()

data_base.close()
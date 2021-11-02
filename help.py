#!/usr/bin/python3
print('syntax database mysql')
while True:
    print('''
          1. DDL
          2. DML
          0. exit''')
    choice = input('enter your choice: ')
    if choice == '1':
        print('''
            CREATE              -CREATE DATABASE database_name;
                                -CREATE TABLE table_name (col1 type, col2 type, ...);
            DROP                -DROP DATABASE database_name;
                                -DROP TABLE table_name;
            ALTER               -(ADD COLUMN) ALTER TABLE table_name ADD COLUMN column_name datatype;
                                -(DROP COLUMN) ALTER TABLE table_name DROP COLUMN column_name;
                                -(MODIFY COLUMN) ALTER TABLE table_name MODIFY COLUMN column_name datatype;
                                ''')
        input()
    elif choice == '2':
        print('''
            SELECT              -SELECT*FROM table_name;
                                -SELECT column_name FROM table_name;
            DELETE              -DELETE table_name (all)
                                -DELETE FROM table_name WHERE condition;
            INSERT              -INSERT INTO table_name VALUES (value);
                                -INSERT INTO table_name (column_name) VALUES (value);
                                -INSERT INTO table2 SELECT*FROM table1 WHERE condition;
            UPDATE              -UPDATE table_name SET column1=value1, column2=value2 WHERE condition;
                                ''')
    elif choice == '0':
        exit() 
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
            CREATE              -create database nama_database;
                                -create table nama_table (col1 type, col2 type, ...);
            DROP                -drop database nama_table;
                                -drop table nama_database;
            ALTER               -alter table nama_table add column nama_colun datatype;
                                -alter nama_table drop column nama_colun;
                                ''')
        input()
    elif choice == '2':
        print('''
            SELECT              -select * from nama_table;
                                -select nama_column from nama_table;
            DELETE              -delete name_table (all)
                                -delete from nama_table where condition;
            INSERT              -insert into nama_table values (value);
                                -insert into nama_table (nama_colun) values (value);
                                -insert into table2 selet*from table1 where condition;
                                -   
                                ''')
    elif choice == '0':
        exit() 
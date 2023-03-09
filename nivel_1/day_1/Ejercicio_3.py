'''Ejercicio 3.
Find Customer Referee
id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.

The query result format is in the following example.
'''
from db import get_db
from schema import e_3

def create_table():
    db, c = get_db()
    c.execute('DROP TABLE IF EXISTS Customer')
    for instruction in e_3: 
        c.execute(instruction)
        db.commit()
    print('base de datos inicializada')
    
def view(row):
    print('name')
    for table in row:
        print(table)
        
def resolucion():
    db, c = get_db()
    c.execute('''SELECT name
              FROM Customer
              WHERE referee_id IS NULL OR referee_id != 2''')
    view(c.fetchall())

if __name__ == '__main__':
    create_table()
    resolucion()
'''Ejercicio 2.
 Recyclable and Low Fat Products
 product_id is the primary key for this table.
low_fats is an ENUM of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

Write an SQL query to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The query result format is in the following example.
'''

from db import get_db
from schema import e_2

def create_table():
    db, c = get_db()
    c.execute('DROP TABLE IF EXISTS products')
    for instruction in e_2: 
        c.execute(instruction)
        db.commit()
    print('base de datos inicializada')
    
def view(row):
    print('product_id')
    for table in row:
        print(table)
        
def resolucion():
    db, c = get_db()
    c.execute('''SELECT product_id
              FROM products
              WHERE low_fats ="Y" AND recyclable = "Y"''')
    view(c.fetchall())

if __name__ == '__main__':
    create_table()
    resolucion()
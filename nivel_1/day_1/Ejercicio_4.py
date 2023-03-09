'''Ejercicio 4.'''

from db import get_db 
from schema import e_4

def create_table(): 
    db, c = get_db()
    c.execute('DROP TABLE IF EXISTS Orders')
    c.execute('DROP TABLE IF EXISTS Customers')
    for instruction in e_4: 
        c.execute(instruction) 
        db.commit() 
    print('base de datos inicializada') 

def view(row): 
    print('name') 
    for table in row: 
        print(table) 

def resolucion(): 
    db, c = get_db() 
    c.execute('''SELECT  name AS Customers
            FROM  Customers AS c
            LEFT JOIN Orders AS o ON c.id = o.customerId
            WHERE o.customerId IS NULL''')
    view(c.fetchall()) 
if __name__ == '__main__': 
    create_table() 
    resolucion() 

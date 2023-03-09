'''Ejercicio 3.'''

from db import get_db 
from schema import e_ 

def create_table(): 
    db, c = get_db() 
    c.execute('DROP TABLE IF EXISTS ') 
    for instruction in e_: 
        c.execute(instruction) 
        db.commit() 
    print('base de datos inicializada') 

def view(row): 
    print('name') 
    for table in row: 
        print(table) 

def resolucion(): 
    db, c = get_db() 
    c.execute('''SELECT  
            FROM  
            WHERE ''')
    view(c.fetchall()) 
if __name__ == '__main__': 
    create_table() 
    resolucion() 

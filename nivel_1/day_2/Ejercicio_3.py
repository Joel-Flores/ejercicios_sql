'''Ejercicio 3.
Delete Duplicate Emails

id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The query result format is in the following example.'''

from db import get_db 
from schema import e_3

def create_table(): 
    db, c = get_db() 
    c.execute('DROP TABLE IF EXISTS Person') 
    for instruction in e_3: 
        c.execute(instruction) 
        db.commit() 
    print('base de datos inicializada') 

def view(row): 
    print('id, email') 
    for table in row: 
        print(table) 

def consult_table():
    db, c = get_db()
    c.execute('''SELECT *
            FROM Person''')
    view(c.fetchall())
    
def resolucion(): 
    db, c = get_db()
    
    print('Tabla Antigua')
    consult_table()
    
    c.execute('''DELETE FROM Person WHERE id NOT IN 
                (SELECT id FROM 
                    (SELECT MIN(id) as id FROM Person GROUP BY email) 
                    as tbl);
              ''')
    db.commit()
    
    print('Tabla Nueva')
    consult_table()
    
if __name__ == '__main__': 
    create_table() 
    resolucion() 

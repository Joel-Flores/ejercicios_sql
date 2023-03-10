'''Ejercicio 2.
Swap Salary

id is the primary key for this table.
The sex column is ENUM value of type ('m', 'f').
The table contains information about an employee.

Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.

Note that you must write a single update statement, do not write any select statement for this problem.

The query result format is in the following example.'''

from db import get_db 
from schema import e_2

def create_table(): 
    db, c = get_db() 
    c.execute('DROP TABLE IF EXISTS Salary') 
    for instruction in e_2: 
        c.execute(instruction) 
        db.commit() 
    print('base de datos inicializada') 

def view(row): 
    print('id, name, sex, salary') 
    for table in row: 
        print(table) 
        
def consult_table():
    db, c = get_db()
    c.execute('''SELECT *
            FROM Salary''')
    view(c.fetchall())
    
def resolucion(): 
    db, c = get_db()
    
    print('Tabla Antigua')
    consult_table()
    
    c.execute('''UPDATE Salary
              SET sex = 
                CASE
                    WHEN sex = 'f' 
                        THEN 'm'
                        ELSE 'f'
                END
              ''')
    db.commit()
    
    print('Tabla Nueva')
    consult_table()
    
if __name__ == '__main__': 
    create_table() 
    resolucion() 

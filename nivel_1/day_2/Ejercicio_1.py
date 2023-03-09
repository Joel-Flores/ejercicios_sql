'''Ejercicio 1.
Calculate Special Bonus

employee_id is the primary key for this table.
Each row of this table indicates the employee ID, employee name, and salary.

Write an SQL query to calculate the bonus of each employee. The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.

The query result format is in the following example.'''

from db import get_db 
from schema import e_1

def create_table(): 
    db, c = get_db() 
    c.execute('DROP TABLE IF EXISTS Employees') 
    for instruction in e_1: 
        c.execute(instruction) 
        db.commit() 
    print('base de datos inicializada') 

def view(row): 
    print('employee_id') 
    for table in row: 
        print(table) 

def resolucion(): 
    db, c = get_db() 
    c.execute('''SELECT employee_id, 
                    CASE 
                        WHEN employee_id % 2 <> 0 AND name NOT LIKE 'M%'
                            THEN salary 
                            ELSE 0 
                    END AS bonus 
                FROM Employees 
                ORDER BY employee_id''')
    view(c.fetchall())
if __name__ == '__main__': 
    create_table() 
    resolucion() 

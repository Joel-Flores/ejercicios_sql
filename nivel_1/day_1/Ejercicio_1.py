'''Ejercicio 1.
Big Countries
name is the primary key column for this table.
Each row of this table gives information about the name of a country,
the continent to which it belongs, its area, the population, and its GDP value.
A country is big if:

    it has an area of at least three million (i.e., 3000000 km2), or
    it has a population of at least twenty-five million (i.e., 25000000).
    Write an SQL query to report the name, population, and area of the big countries.

Return the result table in any order.

The query result format is in the following example.
'''

from db import get_db
from schema import e_1

def create_table():
    db, c = get_db()
    c.execute('DROP TABLE IF EXISTS country')
    for instruction in e_1: 
        c.execute(instruction)
        db.commit()
    print('base de datos inicializada')
def view(row):
    print('name,    population,    area')
    for table in row:
        print(table)
        
def resolucion():
    db, c = get_db()
    c.execute('''SELECT name, population, area 
              FROM country
              WHERE area >= 3000000 OR population >= 25000000''')
    view(c.fetchall())

if __name__ == '__main__':
    create_table()
    resolucion()
    
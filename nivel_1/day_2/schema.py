example = [
    '''''',
    '''from db import get_db ''',
    '''from schema import e_ ''',
    '''''',
    '''def create_table(): ''',
    '''    db, c = get_db() ''',
    '''    c.execute('DROP TABLE IF EXISTS ') ''',
    '''    for instruction in e_: ''' ,
    '''        c.execute(instruction) ''',
    '''        db.commit() ''',
    '''    print('base de datos inicializada') ''',
    '''''',
    '''def view(row): ''',
    '''    print('name') ''',
    '''    for table in row: ''',
    '''        print(table) ''',
    '''''',
    '''def resolucion(): ''',
    '''    db, c = get_db() ''',
    """    c.execute('''SELECT  """,
    '''            FROM  ''',
    """            WHERE ''')""",
    '''    view(c.fetchall()) '''
    '''''',
    '''if __name__ == '__main__': ''',
    '''    create_table() ''',
    '''    resolucion() ''',
    ]
e_1 = [
    '''CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER
    )''',
    '''INSERT INTO Employees (employee_id, name, salary)
    VALUES
    (2, 'Meir', 3000),
    (3, 'Michael', 3800),
    (7, 'Addilyn', 7400),
    (8, 'Juan', 6100),
    (9, 'Kannon', 7700)'''
]
e_2 = [
    ''' CREATE TABLE Salary (
    id INTEGER PRIMARY KEY,
    name TEXT,
    sex TEXT,
    salary INTEGER
    )''',

    ''' INSERT INTO Salary 
    VALUES (1, 'A', 'm', 2500),
    (2, 'B', 'f', 1500),
    (3, 'C', 'm', 5500),
    (4, 'D', 'f', 500) '''

]
e_3 = [
    '''CREATE TABLE Person (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL
    )''',
    '''INSERT INTO Person (id, email) VALUES 
    (1, 'john@example.com'),
    (2, 'bob@example.com'),
    (3, 'john@example.com')'''
]

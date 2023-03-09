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

]
e_3 = [

]

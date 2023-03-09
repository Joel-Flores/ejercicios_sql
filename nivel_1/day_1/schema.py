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
    '''CREATE TABLE country (
    name TEXT PRIMARY KEY,
    continent  TEXT,
    area INTEGER,
    population INTEGER,
    gdp INTEGER
    )''',
    '''INSERT INTO country (name, continent , area, population , gdp) 
    VALUES ('Afganistán', 'Asia', 652230, 25500100, 20343000000),
    ('Albania', 'Europa', 28748, 2831741, 12960000000),
    ('Argelia', 'África', 2381741, 37100000, 188681000000),
    ('andorra', 'Europa', 468, 78115, 3712000000),
    ('Angola', 'África', 1246700, 20609294, 100990000000)
    '''
]
e_2 = [
    '''CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    low_fats TEXT,
    recyclable TEXT
    )''',
    '''INSERT INTO products (product_id, low_fats, recyclable)
    VALUES (0, 'Y', 'N'),
    (1, 'Y', 'Y'),
    (2, 'N', 'Y'),
    (3, 'Y', 'Y'),
    (4, 'N', 'N')
    '''
]
e_3 = [
    '''CREATE TABLE Customer(
        id INTEGER PRIMARY KEY,
        name TEXT,
        referee_id INTEGER,
        FOREIGN KEY (referee_id) REFERENCES Customer(id)
    )''',
    '''INSERT INTO Customer (name, referee_id) 
    VALUES ('Will', NULL),
    ('Jane', NULL),
    ('Alex', 2),
    ('Bill', NULL),
    ('Zack', 1),
    ('Mark', 2)
'''
]
e_4 = [
    '''CREATE TABLE Customers (
    id INTEGER PRIMARY KEY,
    name TEXT
    )''',
    '''CREATE TABLE Orders (
    id INTEGER PRIMARY KEY,
    customerId INTEGER,
    FOREIGN KEY (customerId) REFERENCES Customers(id)
    )''',
    '''INSERT INTO Customers (id, name)
    VALUES (1, 'Joe'),
    (2, 'Henry'),
    (3, 'Sam'),
    (4, 'Max')''',
    '''INSERT INTO Orders (id, customerId)
    VALUES (1, 3),
    (2, 1)'''
]
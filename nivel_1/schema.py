example = [
    '''CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    active INTEGER NOT NULL,
    created_in DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
    )''', 
    '''INSERT INTO user(user, password, active) 
    VALUES ("joel", "contraseña", 1),
    ("jorge", "contraseña1", 1)'''
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
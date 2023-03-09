import sqlite3
from schema import example
def get_db():
    try:
        db = sqlite3.connect('database/database.sqlite3')#, row_factory=sqlite3.Row)
        c = db.cursor()
        return db, c
    except Exception as ex:
        print(ex)
        
def crear_archivo(nombre_archivo, numero):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(f"'''Ejercicio {numero}.'''\n")
        for instruction in example:
            archivo.write(instruction + '\n')
    archivo.close()

def run(cantidad):
    for i in range(cantidad):
        nombre_archivo = f'Ejercicio_{i+1}.py'
        crear_archivo(nombre_archivo, i+1)
                      
if __name__ == '__main__':
    cantidad = int(input('cuantos Ejecicios se realizaran?: '))
    run(cantidad)
    
    
from prettytable import PrettyTable


# base de datos en memoria
libros = [{
    "isbn": "1",
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "estado": "Disponible",
    "socio_prestado": None
},
{
    "isbn": "2",
    "titulo": "Rayuela",
    "autor": "Julio Cortázar",
    "estado": "Disponible",
    "socio_prestado": None
},
{
    "isbn": "3",
    "titulo": "1984",
    "autor": "George Orwell",
    "estado": "Disponible",
    "socio_prestado": None
},
{
    "isbn": "4",
    "titulo": "El principito",
    "autor": "Antoine de Saint-Exupéry",
    "estado": "Disponible",
    "socio_prestado": None
}
          
]
socios = []
aux_contador = 1

# creamos una funcion para mostrar un menú 
def mostrar_menu():
    print("\n MINIBIBLIOTECA")
    print("1. Resgistrar Libro")
    print("2. Registrar un Socio")
    print("3. Prestar un Libro")
    print("4. Devolver Libro ")
    print("5. Ver Libro prestado")
    print("6. Ver todos los libros ")
    print("7. Ver Todos los Socios")
    print("0. Salir")
    
def registrar_libro():
    global libros 
    
    print("=================================")
    print("Registrar libros📖")  
    print("=================================")
    
    print("Digite 0 si desea cancelar la creación")
    
    titulo = input("Titulo del libro: ").strip().lower()
    
    if titulo == "0":
        return
    
    if not titulo:
        print(":❌El titulo no puede estar vacio❌")
        return
    
    autor = input("Autor del libro: ").strip().lower()
    
    if autor == "0":
        return
    
    if not autor:
        print("❌El Autor del libro no puede estar vacio❌")
        return 
    isbn = input("ISBN del libro: ").strip().lower()
    if isbn == "0":
        return
    
    if not isbn:
        print("❌El ISBN no puede estar vacio❌")
        return
    
    # con un ciclo for verificarmos que el isbn no se repita
    for l in libros:
        if l["isbn"] == isbn:
            print(f"❌El ISBN {isbn} ya ha sido registrado con otro libro❌")
            
    
    
    # crear un nuevo libro
    nuevo_libro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "estado": "Disponible",
        "socio_prestado": None
    }  
    
    libros.append(nuevo_libro)
    print("✅ Libro fue Registrado Exitosamente")
    print(f"📚 {titulo} - {autor}")
    print(f"ISBN: {isbn}")
   
    print("=================================") 
    
def registrar_socio():
    pass

def prestar_libro():
    pass

def devolver_libro():
    pass

def ver_libro_prestado():
    pass
     
def ver_todos_libros():
    ''''
    print("==================================================")
    print("📖Mostrando todos los libros📖")
    print("==================================================")
    
    if not libros:
        print("No hay libros registrados")
        return
    
    # creamos un ciclo for donde los interadores cumplan la funcion de clave y valor
    
    for i, libro in enumerate(libros, 1):
        print("===============================================")
        print(f"{i}.  Nombre del libro: {libro["titulo"]}")
        print(f"      Autor del libro: {libro["autor"]}")
        print(f"      ISBN del libro: {libro["isbn"]}")
        print(f"      Estado del libro: {libro["estado"]}")
        print("================================================")
        '''
    table = PrettyTable()
    
    table.field_names = ["titulo", "autor", "isbn", "estado"]
    
    table.title= "📖Mostrando todos los libros📖"
    
    for i, libro in enumerate(libros, 1):
        table.add_row([libro["titulo"], libro["autor"], libro["isbn"], libro["estado"]])
    
    print(table)

def ver_todos_socios():
    pass
    
    
def main():
     
    while True:
        mostrar_menu()
        
        opcion = input("seleccione una opcion (0-7): ").strip() 
        
        match opcion:
            case "1":
               registrar_libro()
            case "2":
                registrar_socio() # crear codigo
            case "3":
                prestar_libro()
            case "4":
                devolver_libro()
            case "5":
                ver_libro_prestado()
            case "6":
                ver_todos_libros()
            case "7":
                ver_todos_socios()# crear codigo
            
            case "0": 
                print("📚Gracias por usar mi MINIBIBLIOTECA!📚")
                print("📚Hasta Luego📚")
                break
                
main()        
   
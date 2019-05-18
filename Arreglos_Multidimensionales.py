"""Declaración de variables globales"""
f = int(5)
c = int(5)

Arreglo = []
Arreglo_Transpuesto = []

"""Declaración de la clase 'Arreglos_Multidimensionales' sin método constructor"""
class Arreglos_Multidimensionales:

    """Declaracón del método 'Crear_Arreglos5x5' encargado de crear los arreglos de cinco columnas por cinco filas,
    para posteriormente ser llenados por el usuario"""
    def Crear_Arreglos5x5(self):
        for a in range(f):
            Arreglo.append([0]*c)

        for a1 in range(f):
            Arreglo_Transpuesto.append([0]*c)

    """Método encargado de llenar el primer arreglo 5x5 mediante dos ciclos  for para asignar la posición del elemento 
    ingresado, y un try para que el valor que sea incorrecto ingresado por el usuario se convierta en cero"""
    def Rellenar_Arreglo(self):
        for a in range(f):
            for b in range(c):
                try:
                    var = int(input('Ingrese un número para rellenar el arreglo: '))
                    Arreglo[a][b] = var
                except: ValueError

    """Método encargado de mostrar o imprimir el arreglo 5x5 ingresado por el usuario"""
    def Mostrar_Arreglo(self):
        print("********************_Arreglo Multidimensional 5x5_******************** ")
        for f in range(0, len(Arreglo)):
            for c in range(0, len(Arreglo[f])):
                print(Arreglo[f][c], "\t", end="")
            print("\n")

    """Método encargado de transponer el arreglo ingresado cambiando las filas por columnas y viceversa mediante 
    el uso de dos ciclos for del arreglo anterior para cambiar la posición y guardarlas en el nuevo arreglo"""
    def Transponer_Arreglo(self):
        for f in range(0, len(Arreglo)):
            for c in range(0, len(Arreglo[f])):
                Arreglo_Transpuesto[f][c] = Arreglo [c][f]

    """Método encargado de mostrar el arreglo transpuesto de 5x5"""
    def Mostrar_Arreglo_Transpuesto(self):
        print("\n********************_Arreglo Multidimensional 5x5 Transpuesto_******************** ")
        for f in range(0, len(Arreglo_Transpuesto)):
            for c in range(0, len(Arreglo_Transpuesto[f])):
                print(Arreglo_Transpuesto[f][c], "\t", end="")
            print("\n")

"""Declaración de objetos para acceder a los diferentes métodos"""
arreglo = Arreglos_Multidimensionales()
arreglo.Crear_Arreglos5x5()
arreglo.Rellenar_Arreglo()
arreglo.Mostrar_Arreglo()
arreglo.Transponer_Arreglo()
arreglo.Mostrar_Arreglo_Transpuesto()
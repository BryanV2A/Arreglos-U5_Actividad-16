"""Se declaró un arreglo unidimensional global para toda la clase 'Arreglos_Unidimensionales' para realizar con más
facilidad el algoritmo y para que se vea más estético"""

Arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Se declaró la clase 'Arreglos_Unidimensionales' sin método constructor ya que el arreglo ya viene definido"""
class Arreglos_Unidimensionales:

    """Método encargado de organizar el arreglo de tal forma que los muestre en el siguiente orden: el primero,
    el último, el segundo, el penúltimo, el tercero, etc."""

    def Organizar_Arreglo(self):
        for f in range(0, int((len(Arreglo))/2)):
            print(Arreglo[f], "\t", end="")
            print(len(Arreglo) - f, "\t", end="")

#Declaración del objeto ´orden´ para acceder al método 'Organizar_Arreglo'
orden = Arreglos_Unidimensionales()
orden.Organizar_Arreglo()
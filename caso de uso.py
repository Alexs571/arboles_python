# Clase para representar un nodo en el árbol genealógico
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    # Agregar un hijo al nodo actual
    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

# Función para buscar una persona en el árbol y devolver su nodo
# Realiza una búsqueda en profundidad (DFS)
def buscar_nodo(raiz, nombre):
   # """CONVERTIMOS EL NOM RAIZ A MINUSCULA Y COMPARAMOS CON EL NOM INGRESADO EN MINUSCULAS"""
    if raiz.nombre.lower() == nombre.lower(): 
        return raiz
    for hijo in raiz.hijos:
        resultado = buscar_nodo(hijo, nombre)
        if resultado:
            return resultado
    return None

# Función para imprimir toda la descendencia de una persona
def imprimir_descendencia(nodo, nivel=0):
    print("--" * nivel + nodo.nombre)
    for hijo in nodo.hijos:
        imprimir_descendencia(hijo, nivel + 1)

# Construcción del árbol genealógico precargado
# Nivel 0
raiz = Nodo("Juan Pérez")

# Nivel 1
ana = Nodo("Ana Pérez")
carlos = Nodo("Carlos Pérez")
raiz.agregar_hijo(ana)
raiz.agregar_hijo(carlos)

# Nivel 2
maria = Nodo("María López")
pedro = Nodo("Pedro López")
ana.agregar_hijo(maria)
ana.agregar_hijo(pedro)

luis = Nodo("Luis Pérez")
sofia = Nodo("Sofía Pérez")
carlos.agregar_hijo(luis)
carlos.agregar_hijo(sofia)

# Nivel 3
# Hijos de María
clara = Nodo("Clara Martínez")
jorge = Nodo("Jorge Martínez")
maria.agregar_hijo(clara)
maria.agregar_hijo(jorge)

# Hijos de Pedro
elena = Nodo("Elena Gómez")
federico = Nodo("Federico Gómez")
pedro.agregar_hijo(elena)
pedro.agregar_hijo(federico)

# Hijos de Luis
raul = Nodo("Raúl Torres")
natalia = Nodo("Natalia Torres")
luis.agregar_hijo(raul)
luis.agregar_hijo(natalia)

# Hijos de Sofía
martin = Nodo("Martín Torres")
lucia = Nodo("Lucía Torres")
sofia.agregar_hijo(martin)
sofia.agregar_hijo(lucia)

# Nivel 4
# Hijos de Clara
soledad = Nodo("Soledad Díaz")
alejandro = Nodo("Alejandro Díaz")
clara.agregar_hijo(soledad)
clara.agregar_hijo(alejandro)

# Hijos de Jorge
manuel = Nodo("Manuel Díaz")
victoria = Nodo("Victoria Díaz")
jorge.agregar_hijo(manuel)
jorge.agregar_hijo(victoria)

# Hijos de Elena
gustavo = Nodo("Gustavo Fernández")
carolina = Nodo("Carolina Fernández")
elena.agregar_hijo(gustavo)
elena.agregar_hijo(carolina)

# Hijos de Federico
adrian = Nodo("Adrián Fernández")
valentina = Nodo("Valentina Fernández")
federico.agregar_hijo(adrian)
federico.agregar_hijo(valentina)

# Hijos de Raúl
daniela = Nodo("Daniela Herrera")
pablo = Nodo("Pablo Herrera")
raul.agregar_hijo(daniela)
raul.agregar_hijo(pablo)

# Hijos de Natalia
hernan = Nodo("Hernán Herrera")
camila = Nodo("Camila Herrera")
natalia.agregar_hijo(hernan)
natalia.agregar_hijo(camila)

# Hijos de Martín
javier = Nodo("Javier Herrera")
florencia = Nodo("Florencia Herrera")
martin.agregar_hijo(javier)
martin.agregar_hijo(florencia)

# Hijos de Lucía
agustin = Nodo("Agustín Herrera")
sofia_hija = Nodo("Sofía Herrera")
lucia.agregar_hijo(agustin)
lucia.agregar_hijo(sofia_hija)

# Ejecución principal: pedir al usuario el nombre a buscar
nombre_buscar = input("Ingrese el nombre completo de la persona para ver su descendencia: ")
nodo_encontrado = buscar_nodo(raiz, nombre_buscar)

if nodo_encontrado:
    print(f"\nDescendencia de {nodo_encontrado.nombre}:")
    imprimir_descendencia(nodo_encontrado)
else:
    print("Persona no encontrada en el árbol genealógico.")
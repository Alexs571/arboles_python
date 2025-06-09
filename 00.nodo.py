#declaracion básica de un nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = {}

    def agregar_hijo(self, nodo):
        self.hijos[nodo.valor] = nodo

    def mostrar(self, nivel=0):
        print('  ' * nivel + self.valor)
        for hijo in self.hijos.values():
            hijo.mostrar(nivel + 1)

    def mostrar(self, prefijo='', es_ultimo=True):
        print(prefijo + ('└── ' if es_ultimo else '├── ') + self.valor)
        hijos = list(self.hijos.values())
        for i, hijo in enumerate(hijos):
            es_ult = i == (len(hijos) - 1)
            nuevo_prefijo = prefijo + ('    ' if es_ultimo else '│   ')
            hijo.mostrar(nuevo_prefijo, es_ult)


################# =>ejemplo
# Creamos la raíz
raiz = Nodo('Animales')

# Primer nivel
mamiferos = Nodo('Mamíferos')
aves = Nodo('Aves')
reptiles = Nodo('Reptiles')

raiz.agregar_hijo(mamiferos)
raiz.agregar_hijo(aves)
raiz.agregar_hijo(reptiles)

# Segundo nivel
mamiferos.agregar_hijo(Nodo('Perro'))
mamiferos.agregar_hijo(Nodo('Gato'))

aves.agregar_hijo(Nodo('Águila'))
aves.agregar_hijo(Nodo('Paloma'))

reptiles.agregar_hijo(Nodo('Serpiente'))
reptiles.agregar_hijo(Nodo('Lagarto'))

raiz.mostrar()
################# =>mostrar


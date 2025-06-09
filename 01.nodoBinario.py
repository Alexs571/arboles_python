#Declaramo el nodo con Dos hijos uno izquirdo y otro derecho, y el valor es el contenedor de nuestro datos

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None



class ArbolBusquedaBinario:
    #Método de creacion de la raiz
    def __init__(self):
        self.raiz = None


    #Método para ver si esta vacío
    def imprimir_arbol(self):
        if self.raiz is None:
            print("El árbol está vacío.")
        else:
            self._imprimir_arbol(self.raiz, "", True)

    #Método recursivo para 
    def _imprimir_arbol(self, nodo, espacio, es_izquierda):
        if nodo is None:
            return
        self._imprimir_arbol(nodo.derecha, espacio + "   ", False)
        print(espacio + ("└── " if es_izquierda else "├── ") + str(nodo.valor)) 
        self._imprimir_arbol(nodo.izquierda, espacio + "   ", True)
        
        
        
        
    def insertar(self, valor):
        # Si la raiz está vacía, colocamos el valor proporcionado como raíz
        if self.raiz is None:
            self.raiz = Nodo(valor)
        # En otro caso, llamamos al método _insertar para insertar el valor
        # en la posición que corresponda
        else:
            self._insertar(self.raiz, valor)


    def _insertar(self, nodo, valor):
        # Si el valor ingresado es menor que el nodo ya presente en el árbol
        if valor < nodo.valor:
            # Si el nodo de la izquierda está vacío, colocamos el 
            # valor proporcionado en la izquierda
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            # En otro caso, seguimos bajando recursivamente por 
            # el árbol hasta insertarlo como hijo
            # izquierdo de algún nodo existente
            else:
                self._insertar(nodo.izquierda, valor)

        # Si el valor ingresado es mayor que el nodo ya presente en el árbol
        elif valor > nodo.valor:
            # Si el nodo de la derecha está vacío, colocamos el 
            # valor proporcionado en la derecha
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            # En otro caso, seguimos bajando recursivamente por el árbol 
            # hasta insertarlo como hijo
            # derecho de algún nodo existente
            else:
                self._insertar(nodo.derecha, valor)

    def preorden(self):
        print("Preorden:")
        self._preorden(self.raiz)
        print()

    def _preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden(nodo.izquierda)
            self._preorden(nodo.derecha)

    def inorden(self):
        print("Inorden:")
        self._inorden(self.raiz)
        print()

    def _inorden(self, nodo):
        if nodo:
            self._inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden(nodo.derecha)

    def postorden(self):
        print("Postorden:")
        self._postorden(self.raiz)
        print()

    def _postorden(self, nodo):
        if nodo:
            self._postorden(nodo.izquierda)
            self._postorden(nodo.derecha)
            print(nodo.valor, end=" ")

#delcaro un árbol
arbol = ArbolBusquedaBinario()

print("Ingrese 10 valores")

for i in range (10):
    valor = input(f"Ingrese valor {i} ")
    arbol.insertar(valor)


arbol.imprimir_arbol()
arbol.preorden()
arbol.inorden()
arbol.postorden()
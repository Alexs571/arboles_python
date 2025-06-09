#!/usr/bin/env python3

import ast

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value!r}, {self.left!r}, {self.right!r})"

def build_tree_from_list(data):
    """
    Construye un árbol binario a partir de una lista de la forma:
    [valor, subarbol_izq, subarbol_der]
    donde subarbol_izq y subarbol_der pueden ser None o listas en la misma forma.
    """
    if data is None:
        return None
    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("La lista debe tener la forma [valor, subarbol_izq, subarbol_der] o None")
    value, left_list, right_list = data
    left_node = build_tree_from_list(left_list) if left_list is not None else None
    right_node = build_tree_from_list(right_list) if right_list is not None else None
    return Node(value, left_node, right_node)


def print_tree(node, level=0):
    """
    Imprime el árbol en consola rotado 90° a la izquierda:
    - Raíz más a la izquierda
    - Subárbol derecho arriba
    - Subárbol izquierdo abajo
    """
    if node is not None:
        print_tree(node.right, level + 1)
        print('    ' * level + str(node.value))
        print_tree(node.left, level + 1)


def calculate_height(node):
    """
    Calcula la altura (profundidad) del árbol.
    La altura de un árbol vacío es 0.
    """
    if node is None:
        return 0
    left_height = calculate_height(node.left)
    right_height = calculate_height(node.right)
    return 1 + max(left_height, right_height)


def main():
    try:
        user_input = input(
            "Ingrese la lista que representa el árbol (ejemplo: ['A', ['B', None, None], ['C', ['D', None, None], ['E', None, None]]]): "
        )
        data = ast.literal_eval(user_input)
        tree = build_tree_from_list(data)
        print("\nÁrbol construido (vista rotada 90° a la izquierda):")
        print_tree(tree)

        altura = calculate_height(tree)
        print(f"\nAltura del árbol: {altura}")
    except Exception as e:
        print(f"Error al construir el árbol: {e}")

if __name__ == "__main__":
    main()

#Ejemplos:
#Ejemplo1 = ['A', ['B', None, None], ['C', ['D', None, None], ['E', None, None]]]
#Ejemplo2 = ['M',['G',['C',['A',None,None],['B',None,None]],['E',['D',None,None],['F',None,None]]],['T',['P',['N',None,None],None],['W',['S',None,None],['Y',None,None]]]]
#Ejemplo3 = [1,[2,[4,[8,None,None],[9,None,None]],[5,[10,None,None],[11,None,None]]],[3,[6,[12,None,None],[13,None,None]],[7,[14,None,None],[15,None,None]]]]
#Ejemplo4 = ['root',['L1',['L2',['L3',['L4',['L5',None,None],None],None],None],None],None]
#Ejemplo5 = [100,[50,[25,None,[30,None,None]],[75,[60,None,None],None]],[150,None,[200,[175,None,None],[250,None,[300,None,None]]]]]
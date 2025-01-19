import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_fuera_de_rango(self, min_valor, max_valor):
        actual = self.cabeza
        previo = None
        while actual:
            if actual.dato < min_valor or actual.dato > max_valor:
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
            else:
                previo = actual
            actual = actual.siguiente

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Generar lista enlazada con 50 números enteros aleatorios entre 1 y 999
lista = ListaEnlazada()
for _ in range(50):
    numero_aleatorio = random.randint(1, 999)
    lista.agregar(numero_aleatorio)

print("Lista original:")
lista.mostrar()

# Leer rango de valores desde el teclado
min_valor = int(input("Ingrese el valor mínimo del rango: "))
max_valor = int(input("Ingrese el valor máximo del rango: "))

# Eliminar nodos fuera de rango
lista.eliminar_fuera_de_rango(min_valor, max_valor)

print("Lista después de eliminar nodos fuera de rango:")
lista.mostrar()

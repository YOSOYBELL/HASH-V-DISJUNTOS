from sys import stdin
from random import randint

class HashTable:
    def __init__(self, size):
        self.elements = [[] for x in range(size)]


    def getElements(self):
        return self.elements

    def printElements(self):
        for index in range(len(self.elements)):
            print(index, ': ', self.elements[index])

    def hash(self, key):
        return hash(key) % len(self.elements)

    def assign(self, index, element):
        self.elements[index].append(element)

    def insert(self, key, value):
        index = self.hash(key)
        print('Inserting', value, 'with key', key, 'on index', index)
        self.assign(index, (key,value))

    def search(self, key):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                return e[1]
        return None

    def update(self, key, value2):
        index = self.hash(key)
        for e in self.elements[index]:
            if e[0] == key:
                e[1] = value2

    def delete(self, key):
        index = self.hash(key)
        element = self.search(key)
        if element:
            self.elements[index].remove(element)

def main():
    print("Ingrese cuantos pedidos va a agenedar: ")
    size = int(stdin.readline().strip())
    hashtable = HashTable(size)

    cont = size
    print("ingrese los pedidos un por uno de la forma ""Nombre fecha"": ")
    lista = []
    while cont > 0:
        el1, el2 = stdin.readline().strip().split()
        lista += [(el1, el2)]
        cont -= 1
    print(lista)

    for elem in lista:
        hashtable.insert(elem[0], elem[1])

    action = "4"

    while action != "0":
        print("Si desea buscar la hora de algun pedido ingrese hora, si desea ver todos sus pedidos ingrese resumen, si deasea salir ingrese 0")
        action = stdin.readline().strip()
        if action == "hora":
            print("Ingrese el nombre de la entrega : ")
            key = stdin.readline().strip()
            print(hashtable.search(key))
        if action == "resumen":
            hashtable.printElements()


print("si desea agendar sus pedidos ingrese 0")
resp = stdin.readline().strip()
if resp == "0":
    main()
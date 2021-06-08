class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista j tem elemt
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1

    def __len__(self):
        # retorna o tamanho da lista
        return self._size

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Indice da lista fora do alcance")
        if pointer:
            return pointer.data
        else:
            raise IndexError("Indice da lista fora do alcance")

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("Indice da lista fora do alcance")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("Indice da lista fora do alcance")

    def index(self, elem):
        # Retorna indice do elemento na lista
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
        raise ValueError("{} não está na lista".format(elem))

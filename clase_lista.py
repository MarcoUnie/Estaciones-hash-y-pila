class nodoLista():
    def __init__(self, info=None):
        self.info = info
        self.siguiente = None

def criterio(dato, campo=None):
        if hasattr(dato, '_dict_'):
            dic = dato._dict_
        else:
            dic = {}
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]
    
class nodoLista():
    def __init__(self):
        self.info = None
        self.siguiente = None
        self.sublista = Lista()  # Sublista inicializada por defecto


class Lista():
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar(lista, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) or (criterio(lista.inicio.info, campo) > criterio(dato, campo)):
            nodo.siguiente = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.siguiente
            while(act is not None and criterio(act.info, campo) < criterio(dato, campo)):
                ant = ant.siguiente
                act = act.siguiente
            nodo.siguiente = act
            ant.siguiente = nodo
        lista.tamaño += 1

    def lista_vacia(lista):
        return lista.inicio is None

    def buscar(lista, buscado, campo=None):
        aux = lista.inicio
        while(aux is not None and criterio(aux.info, campo) != criterio(buscado, campo)):
            aux = aux.siguiente
        return aux

    def eliminar(lista, clave, campo=None):
        dato = None
        if lista.inicio is None:
            return dato
        if(criterio(lista.inicio.info, campo) == criterio(clave, campo)):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.siguiente
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.siguiente
            while(actual is not None and criterio(actual.info, campo) != criterio(clave, campo)):
                anterior = anterior.siguiente
                actual = actual.siguiente
            if actual is not None:
                dato = actual.info
                anterior.siguiente = actual.siguiente
                lista.tamaño -= 1
        return dato

    def tamanio(lista):
        return lista.tamaño

    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.siguiente

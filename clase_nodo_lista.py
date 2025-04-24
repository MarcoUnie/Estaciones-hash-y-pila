class nodoLista():
    def __init__(self, info=None):
        self.info = info
        self.siguiente = None

class Lista():
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    
    def insertar(lista,dato):
        nuevo = nodoLista()
        nuevo.info = dato
        if lista.inicio == None or lista.inicio.info > dato:
            nuevo.siguiente = lista.inicio
            lista.inicio = nuevo
        else:
            ant = lista.inicio
            act = lista.inicio.siguiente
            while (act != None and ant.info < dato):
                ant = ant.siguiente
                act = act.siguiente
            nuevo.siguiente = act
            ant.siguiente = nuevo
        lista.tamaño += 1

    def lista_vacia(lista):
        return lista.inicio == None
    
    def eliminar(lista, clave):
        dato = None
        if(lista.inicio.info == clave):
            dato - lista.inicio.info
            lista.inicio = lista. inicio.sig
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while(actual is not None and actual.info != clave):
                anterior = anterior.sig
                actual = actual.sig
            if (actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamaño -= 1
        return dato
    
    def tamanio(lista):
        return lista.tamaño

    def buscar(lista, buscado):
        aux = lista.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux

    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
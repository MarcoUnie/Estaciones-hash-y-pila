from clase_lista import Lista
lista = Lista()
dato = input("Ingrese una palabra:")
while(dato != ""):
    Lista.insertar(lista, dato)
    dato = input("Ingrese una palabra:")

buscado = input("Ingrese la palabra a buscar:")
posicion = Lista.buscar(lista, buscado)
if(posicion is not None):
    dato = Lista.eliminar(lista, posicion.info)
    print("Elemento eliminado: ", dato)
else:
    print("No se econtro el elemento a eliminar")
Lista.barrido(lista)
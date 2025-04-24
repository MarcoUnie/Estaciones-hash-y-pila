from clase_lista import Lista
estaciones = Lista()

dato = input('Ingrese nombre de la estación: ')
Lista.insertar(estaciones, dato)

estacion = Lista.buscar(estaciones, dato)
if(estacion is not None):
    estado_clima = input('Cargar estado del clima: ')
    Lista.insertar(estacion.sublista, estado_clima)

buscado = input('Ingrese nombre de la estación a listar: ')
pos = Lista.buscar(estaciones, buscado)
if(pos is not None):
    Lista.barrido(pos.sublista)
from clase_lista import Lista
estaciones = Lista()

dato = input('Ingrese nombre de la estación: ')
while dato != '':
    Lista.insertar(estaciones, dato)
    estacion = Lista.buscar(estaciones, dato)
    if(estacion is not None):
        estado_clima = input('Cargar estado del clima: ')
        while estado_clima != '':
            Lista.insertar(estacion.sublista, estado_clima)
            estado_clima = input('Cargar estado del clima: ')
    dato = input('Ingrese nombre de la estación: ')

buscado = input('Ingrese nombre de la estación a listar: ')
pos = Lista.buscar(estaciones, buscado)
if(pos is not None):
    Lista.barrido(pos.sublista)
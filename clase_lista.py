import gradio as gr

class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return None

    def keys(self):
        result = []
        for bucket in self.buckets:
            result.extend(k for k, _ in bucket)
        return result


class nodoLista():
    def __init__(self):
        self.info = None
        self.siguiente = None
        self.sublista = Lista()


class Lista():
    def __init__(self):
        self.inicio = None
        self.tamaño = 0

    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        if (self.inicio is None) or (criterio(self.inicio.info, campo) > criterio(dato, campo)):
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            act = self.inicio.siguiente
            while(act is not None and criterio(act.info, campo) < criterio(dato, campo)):
                ant = ant.siguiente
                act = act.siguiente
            nodo.siguiente = act
            ant.siguiente = nodo
        self.tamaño += 1

    def buscar(self, buscado, campo=None):
        aux = self.inicio
        while(aux is not None and criterio(aux.info, campo) != criterio(buscado, campo)):
            aux = aux.siguiente
        return aux

    def barrido(self):
        elementos = []
        aux = self.inicio
        while(aux is not None):
            elementos.append(aux.info)
            aux = aux.siguiente
        return elementos


def criterio(dato, campo=None):
    if campo is None or not isinstance(dato, dict):
        return dato
    else:
        return dato.get(campo, None)


hash_estaciones = HashTable()


def agregar_estacion(nombre):
    if hash_estaciones.get(nombre) is None:
        lista = Lista()
        lista.insertar(nombre)  # nodo de nombre como cabecera
        hash_estaciones.insert(nombre, lista)
        return f"Estación '{nombre}' agregada."
    return f"La estación '{nombre}' ya existe."

def agregar_clima(estacion, clima):
    lista = hash_estaciones.get(estacion)
    if lista:
        nodo_estacion = lista.buscar(estacion)
        if nodo_estacion:
            nodo_estacion.sublista.insertar(clima)
            return f"Clima '{clima}' agregado a la estación '{estacion}'."
    return f"La estación '{estacion}' no fue encontrada."

def mostrar_estaciones():
    estaciones = hash_estaciones.keys()
    return "\n".join(estaciones) if estaciones else "No hay estaciones cargadas."

def mostrar_climas(estacion):
    lista = hash_estaciones.get(estacion)
    if lista:
        nodo_estacion = lista.buscar(estacion)
        if nodo_estacion:
            climas = nodo_estacion.sublista.barrido()
            return "\n".join(climas) if climas else "No hay climas para esta estación."
    return f"La estación '{estacion}' no fue encontrada."


with gr.Blocks() as demo:
    gr.Markdown("## Sistema de Estaciones Meteorológicas")

    with gr.Tab("Agregar estación"):
        estacion_input = gr.Textbox(label="Nombre de la estación")
        btn_agregar = gr.Button("Agregar")
        resultado_agregar = gr.Textbox(label="Resultado")
        btn_agregar.click(agregar_estacion, inputs=estacion_input, outputs=resultado_agregar)

    with gr.Tab("Agregar clima a estación"):
        nombre_estacion = gr.Textbox(label="Nombre de la estación")
        estado_clima = gr.Textbox(label="Estado del clima")
        btn_clima = gr.Button("Agregar clima")
        resultado_clima = gr.Textbox(label="Resultado")
        btn_clima.click(agregar_clima, inputs=[nombre_estacion, estado_clima], outputs=resultado_clima)

    with gr.Tab("Listar estaciones"):
        btn_listar = gr.Button("Mostrar estaciones")
        resultado_lista = gr.Textbox(label="Estaciones")
        btn_listar.click(mostrar_estaciones, outputs=resultado_lista)

    with gr.Tab("Ver climas de una estación"):
        buscar_estacion = gr.Textbox(label="Nombre de la estación")
        btn_ver_climas = gr.Button("Mostrar climas")
        salida_climas = gr.Textbox(label="Climas")
        btn_ver_climas.click(mostrar_climas, inputs=buscar_estacion, outputs=salida_climas)

demo.launch()

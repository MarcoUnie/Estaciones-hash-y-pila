import gradio as gr

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

estaciones = Lista()

def agregar_estacion(nombre):
    if estaciones.buscar(nombre) is None:
        estaciones.insertar(nombre)
        return f"Estación '{nombre}' agregada."
    return f"La estación '{nombre}' ya existe."

def agregar_clima(estacion, clima):
    nodo_estacion = estaciones.buscar(estacion)
    if nodo_estacion:
        nodo_estacion.sublista.insertar(clima)
        return f"Clima '{clima}' agregado a la estación '{estacion}'."
    return f"La estación '{estacion}' no fue encontrada."

def mostrar_estaciones():
    return "\n".join(estaciones.barrido()) or "No hay estaciones cargadas."

def mostrar_climas(estacion):
    nodo_estacion = estaciones.buscar(estacion)
    if nodo_estacion:
        return "\n".join(nodo_estacion.sublista.barrido()) or "No hay climas para esta estación."
    return f"La estación '{estacion}' no fue encontrada."


with gr.Blocks() as demo:
    gr.Markdown("## Sistema de Estaciones Meteorológicas 🌦️")

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

demo.launch(share=True)

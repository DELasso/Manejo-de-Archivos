from typing import Dict, Any


class AnalizadorEventos:

    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo

    def procesar_eventos(self) -> Dict[str, Any]:
        eventos_totales = 0
        eventos_por_tipo = {}
        eventos_por_servidor = {}

        with open("eventos.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if linea.strip():  # Significa ignorar espacios vacios
                    eventos_totales += 1
                    campos = linea.strip().split(': ') # Significa que divide una cadena en varias subcadenas
                    tipo_evento = campos[3][:-1]
                    servidor = campos[5]
                    if tipo_evento in eventos_por_tipo:
                        eventos_por_tipo[tipo_evento] += 1
                    else:
                        eventos_por_tipo[tipo_evento] = 1
                    if servidor in eventos_por_servidor:
                        eventos_por_servidor[servidor] += 1
                    else:
                        eventos_por_servidor[servidor] = 1

        estadisticas = {'eventos_totales': eventos_totales, 'eventos_por_tipo': eventos_por_tipo,
                        'eventos_por_servidor': eventos_por_servidor}

        return estadisticas


analizador = AnalizadorEventos('eventos.txt')
estadisticas = analizador.procesar_eventos()
print(estadisticas)

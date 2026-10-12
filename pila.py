
class PilaUrgencias:
    def __init__(self):
        self._elementos = []

    def esta_vacia(self):
        return len(self._elementos) == 0

    def push(self, cliente):
        self._elementos.append(cliente)

    def pop(self):
        if self.esta_vacia():
            return None
        return self._elementos.pop()

    def peek(self):
        if self.esta_vacia():
            return None
        return self._elementos[-1]

    def tamano(self):
        return len(self._elementos)

    def obtener_elementos(self):
        return list(reversed(self._elementos))

    def construir_desde_clientes(self, clientes):
        self._elementos.clear()

        elegibles = [
            c for c in clientes
            if c["tratamiento"].casefold() == "extraccion dental"
            and c["estado"].casefold() == "pendiente"
            and c["prioridad"].casefold() == "urgente"
        ]

        elegibles.sort(key=lambda c: (c["fecha"], c["hora"]))

        # Se insertan al reves para que la fecha mas cercana
        # quede en la parte superior de la pila.
        for cliente in reversed(elegibles):
            self.push(cliente)

    def generar_informe(self):
        if self.esta_vacia():
            return "No hay extracciones urgentes pendientes."

        lineas = [
            "INFORME DE URGENCIAS",
            "=" * 55,
            "Orden: fecha mas cercana a mas lejana",
            ""
        ]

        for i, c in enumerate(self.obtener_elementos(), start=1):
            lineas.append(
                f"{i}. {c['nombre']} | Cedula: {c['cedula']} | "
                f"Telefono: {c['telefono']} | Fecha: {c['fecha']} | "
                f"Hora: {c['hora']}"
            )

        return "\n".join(lineas)

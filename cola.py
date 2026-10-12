
from collections import deque


class ColaAtencion:
    def __init__(self):
        self._elementos = deque()

    def esta_vacia(self):
        return len(self._elementos) == 0

    def enqueue(self, cliente):
        self._elementos.append(cliente)

    def dequeue(self):
        if self.esta_vacia():
            return None
        return self._elementos.popleft()

    def front(self):
        if self.esta_vacia():
            return None
        return self._elementos[0]

    def tamano(self):
        return len(self._elementos)

    def obtener_elementos(self):
        return list(self._elementos)

    def construir_agenda(self, clientes, fecha_agenda):
        self._elementos.clear()

        elegibles = [
            c for c in clientes
            if c["fecha"] == fecha_agenda
            and c["estado"].casefold() == "pendiente"
        ]

        elegibles.sort(
            key=lambda c: (c["hora"], c["orden_registro"])
        )

        for cliente in elegibles:
            self.enqueue(cliente)

    def mostrar_agenda(self):
        if self.esta_vacia():
            return "No hay clientes pendientes en esta agenda."

        lineas = ["AGENDA DE ATENCION", "=" * 55]

        for i, c in enumerate(self.obtener_elementos(), start=1):
            lineas.append(
                f"{i}. {c['hora']} | {c['nombre']} | "
                f"Tratamiento: {c['tratamiento']} | "
                f"Estado: {c['estado']}"
            )

        return "\n".join(lineas)

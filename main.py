
from datetime import date, datetime, timedelta

from pila import PilaUrgencias
from cola import ColaAtencion


clientes = []
siguiente_orden = 1


def fecha_relativa(dias):
    return (date.today() + timedelta(days=dias)).isoformat()


def cargar_clientes_prueba():
    global siguiente_orden

    datos = [
        {
            "cedula": "1001",
            "nombre": "Laura Martinez",
            "telefono": "3001112233",
            "tratamiento": "Extraccion dental",
            "fecha": fecha_relativa(1),
            "hora": "08:00",
            "prioridad": "Urgente",
            "estado": "Pendiente",
        },
        {
            "cedula": "1002",
            "nombre": "Carlos Ramirez",
            "telefono": "3002223344",
            "tratamiento": "Extraccion dental",
            "fecha": fecha_relativa(0),
            "hora": "09:00",
            "prioridad": "Urgente",
            "estado": "Pendiente",
        },
        {
            "cedula": "1003",
            "nombre": "Sofia Torres",
            "telefono": "3003334455",
            "tratamiento": "Limpieza dental",
            "fecha": fecha_relativa(0),
            "hora": "08:00",
            "prioridad": "Normal",
            "estado": "Pendiente",
        },
        {
            "cedula": "1004",
            "nombre": "Andres Gomez",
            "telefono": "3004445566",
            "tratamiento": "Extraccion dental",
            "fecha": fecha_relativa(3),
            "hora": "10:00",
            "prioridad": "Urgente",
            "estado": "Pendiente",
        },
        {
            "cedula": "1005",
            "nombre": "Valentina Rojas",
            "telefono": "3005556677",
            "tratamiento": "Extraccion dental",
            "fecha": fecha_relativa(0),
            "hora": "11:00",
            "prioridad": "Normal",
            "estado": "Pendiente",
        },
        {
            "cedula": "1006",
            "nombre": "Mateo Hernandez",
            "telefono": "3006667788",
            "tratamiento": "Extraccion dental",
            "fecha": fecha_relativa(0),
            "hora": "10:00",
            "prioridad": "Urgente",
            "estado": "Atendido",
        },
    ]

    for cliente in datos:
        cliente["orden_registro"] = siguiente_orden
        siguiente_orden += 1
        clientes.append(cliente)


def mostrar_clientes():
    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\nLISTADO DE CLIENTES")
    print("=" * 70)

    for c in clientes:
        print(
            f"Cedula: {c['cedula']} | Nombre: {c['nombre']} | "
            f"Tratamiento: {c['tratamiento']} | Fecha: {c['fecha']} | "
            f"Hora: {c['hora']} | Prioridad: {c['prioridad']} | "
            f"Estado: {c['estado']}"
        )


def registrar_cliente():
    global siguiente_orden

    print("\nREGISTRAR CLIENTE")
    print("=" * 30)

    cedula = input("Cedula: ").strip()

    if not cedula:
        print("La cedula no puede estar vacia.")
        return

    if any(c["cedula"] == cedula for c in clientes):
        print("Ya existe un cliente con esa cedula.")
        return

    nombre = input("Nombre completo: ").strip()
    telefono = input("Telefono: ").strip()
    tratamiento = input(
        "Tratamiento (Extraccion dental / Limpieza dental): "
    ).strip()
    fecha = input("Fecha (AAAA-MM-DD): ").strip()
    hora = input("Hora (HH:MM): ").strip()
    prioridad = input("Prioridad (Urgente / Normal): ").strip()

    if not all([nombre, telefono, tratamiento, fecha, hora, prioridad]):
        print("Todos los campos son obligatorios.")
        return

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        datetime.strptime(hora, "%H:%M")
    except ValueError:
        print("Formato incorrecto de fecha u hora.")
        print("Ejemplo de fecha: 2026-10-12")
        print("Ejemplo de hora: 09:30")
        return

    if tratamiento.casefold() not in [
        "extraccion dental", "limpieza dental"
    ]:
        print("Tratamiento no valido.")
        return

    if prioridad.casefold() not in ["urgente", "normal"]:
        print("Prioridad no valida.")
        return

    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tratamiento": (
            "Extraccion dental"
            if tratamiento.casefold() == "extraccion dental"
            else "Limpieza dental"
        ),
        "fecha": fecha,
        "hora": hora,
        "prioridad": (
            "Urgente" if prioridad.casefold() == "urgente" else "Normal"
        ),
        "estado": "Pendiente",
        "orden_registro": siguiente_orden,
    }

    siguiente_orden += 1
    clientes.append(cliente)

    print("Cliente registrado correctamente.")


def buscar_cliente():
    cedula = input("\nEscribe la cedula que deseas buscar: ").strip()

    for c in clientes:
        if c["cedula"] == cedula:
            print("\nCliente encontrado:")
            for clave, valor in c.items():
                print(f"{clave.capitalize()}: {valor}")
            return

    print("No se encontro ningun cliente con esa cedula.")


def informar_urgencias():
    pila = PilaUrgencias()
    pila.construir_desde_clientes(clientes)

    print()
    print(pila.generar_informe())


def atender_urgencia():
    pila = PilaUrgencias()
    pila.construir_desde_clientes(clientes)

    cliente = pila.pop()

    if cliente is None:
        print("\nNo hay urgencias pendientes para atender.")
        return

    cliente["estado"] = "Atendido"

    print("\nATENCION DE URGENCIA")
    print(f"Cliente: {cliente['nombre']}")
    print(f"Telefono: {cliente['telefono']}")
    print(f"Fecha de cita: {cliente['fecha']}")
    print(f"Hora: {cliente['hora']}")
    print("Estado actualizado a: Atendido")


def crear_agenda():
    cola = ColaAtencion()

    fecha_agenda = input(
        "\nIngresa la fecha de la agenda (AAAA-MM-DD): "
    ).strip()

    try:
        datetime.strptime(fecha_agenda, "%Y-%m-%d")
    except ValueError:
        print("Fecha no valida. Usa el formato AAAA-MM-DD.")
        return

    cola.construir_agenda(clientes, fecha_agenda)

    print()
    print(cola.mostrar_agenda())


def mostrar_cola():
    cola = ColaAtencion()

    fecha_agenda = input(
        "\nIngresa la fecha de la agenda (AAAA-MM-DD): "
    ).strip()

    try:
        datetime.strptime(fecha_agenda, "%Y-%m-%d")
    except ValueError:
        print("Fecha no valida. Usa el formato AAAA-MM-DD.")
        return

    cola.construir_agenda(clientes, fecha_agenda)

    print()
    print("COLA DE ATENCION")
    print(cola.mostrar_agenda())


def atender_cola():
    cola = ColaAtencion()

    fecha_agenda = input(
        "\nIngresa la fecha de la agenda (AAAA-MM-DD): "
    ).strip()

    try:
        datetime.strptime(fecha_agenda, "%Y-%m-%d")
    except ValueError:
        print("Fecha no valida. Usa el formato AAAA-MM-DD.")
        return

    cola.construir_agenda(clientes, fecha_agenda)

    while not cola.esta_vacia():
        cliente = cola.dequeue()

        if cliente["estado"].casefold() == "pendiente":
            cliente["estado"] = "Atendido"

            print("\nSIGUIENTE CLIENTE DE LA COLA")
            print(f"Nombre: {cliente['nombre']}")
            print(f"Tratamiento: {cliente['tratamiento']}")
            print(f"Hora: {cliente['hora']}")
            print("Estado actualizado a: Atendido")
            return

    print("No hay clientes pendientes en esa agenda.")


def mostrar_menu():
    print("\n" + "=" * 45)
    print(" SISTEMA DE GESTION DEL CONSULTORIO")
    print("=" * 45)
    print("1. Registrar cliente")
    print("2. Mostrar todos los clientes")
    print("3. Buscar cliente por cedula")
    print("4. Generar informe de urgencias")
    print("5. Atender siguiente urgencia")
    print("6. Crear y mostrar agenda del dia")
    print("7. Mostrar cola de atencion")
    print("8. Atender siguiente cliente de la cola")
    print("0. Salir")


def main():
    cargar_clientes_prueba()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            mostrar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            informar_urgencias()
        elif opcion == "5":
            atender_urgencia()
        elif opcion == "6":
            crear_agenda()
        elif opcion == "7":
            mostrar_cola()
        elif opcion == "8":
            atender_cola()
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida. Intenta nuevamente.")


if __name__ == "__main__":
    main()

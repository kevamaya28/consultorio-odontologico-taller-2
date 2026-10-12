
# Sistema de Gestion del Consultorio Odontologico

## Descripcion
Programa desarrollado en Python para administrar clientes de un consultorio odontologico, identificar extracciones dentales urgentes y organizar la atencion diaria.

## Funcionalidades
- Registrar clientes.
- Consultar y buscar clientes.
- Identificar extracciones dentales urgentes pendientes.
- Generar un informe de urgencias ordenado por fecha y hora.
- Utilizar una pila para gestionar las urgencias.
- Crear agendas diarias.
- Utilizar una cola para atender a los clientes en orden de llegada a la agenda.

## Estructuras de datos
- **Pila (LIFO):** el ultimo elemento que entra es el primero que sale. Las urgencias se organizan para que la cita pendiente mas cercana quede primero.
- **Cola (FIFO):** el primer cliente que entra es el primero que sale.

## Archivos del proyecto
- `main.py`: programa principal y menu.
- `pila.py`: implementacion de la pila de urgencias.
- `cola.py`: implementacion de la cola de atencion.

## Requisitos
Python 3 instalado.

## Ejecucion
Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python main.py
```

En Windows tambien puedes probar:

```bash
py main.py
```

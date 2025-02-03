# Proyecto de Test con FastAPI y Pydantic

Este proyecto es una aplicación de prueba que utiliza FastAPI y Pydantic para la creación de APIs rápidas y eficientes. La gestión de dependencias y el entorno virtual se manejan con Poetry.

## Tecnologías Utilizadas

- **FastAPI**: Un framework web moderno y rápido para construir APIs con Python 3.7+ basado en estándares como OpenAPI y JSON Schema.
- **Pydantic**: Una biblioteca de validación de datos y configuración basada en anotaciones de tipo de Python.
- **Poetry**: Una herramienta de gestión de dependencias y empaquetado para Python.




## inicialización de el entorno virtual con poetry
```bash
poetry shell
```
ese comando se usa para activar el entorno virtual, hay que tener previamente instalado poetry, y validar la version de python con la que se inicia el proyecto


## Instalación

Para instalar las dependencias y configurar el entorno virtual, ejecuta los siguientes comandos:

```bash
poetry install
```

## Ejecución

Para levantar el servidor de desarrollo, utiliza el siguiente comando:

```bash
poetry run uvicorn main:app --reload
```

Esto iniciará el servidor en `http://127.0.0.1:8000` con recarga automática habilitada.

## Estructura del Proyecto
la estructura por el momento queda a criterio del dev
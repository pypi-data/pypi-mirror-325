
## Cursos disponibles

- Introducción a Linux [53 horas]
- Personalización de Linux [3 horas]
- Introducción al Hacking [53 horas]

## Instalación

Instala el paquete usando `pip3`:

```python3
pip3 install m4rtin
```

## Uso básico

## Listar todos los cursos

```python3
from m4rtin import list_courses

for course in list_courses:
    print(course)
```

### Obtener un curso por nombre

```python3
from m4rtin impor get_course_by_name

course = get_course_by_name('Introduccón a Linux')

print(course)
```

## Calcular duración total de los cursos

```python3
from m4rtin import total_duration

print(f"Duración total: {total_duration()} horas.")
```

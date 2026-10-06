# Proyecto universitario 331

Monorepo para el proyecto universitario.

## Stack

- **Backend:** Django 5.2, gestionado con [uv](https://docs.astral.sh/uv/).
- **Frontend:** React + Vite + TypeScript, gestionado con [Bun](https://bun.sh/).
- **Informe:** documento editable en formato `.odt`, ubicado en `doc/`.

## Requisitos

- Python 3.13 o superior
- uv
- Bun

## Desarrollo

### Backend

```bash
cd backend
uv run manage.py migrate
uv run manage.py runserver
```

El backend estará disponible en http://127.0.0.1:8000/.

### Frontend

En otra terminal:

```bash
cd frontend
bun install
bun run dev
```

El frontend estará disponible en la dirección que indique Vite, normalmente http://localhost:5173/.

Para comprobar el build de producción:

```bash
bun run build
```

## Estructura

```text
backend/   Proyecto Django y dependencias Python
frontend/  Aplicación React + Vite y dependencias Bun
doc/       Informe del proyecto en formato ODT
```

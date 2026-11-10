# Proyecto universitario 331

Repositorio del proyecto universitario. La aplicación completa utiliza **Django**, tanto para la lógica del servidor como para la interfaz web mediante plantillas HTML y archivos estáticos CSS y JavaScript.

## Tecnologías

- Django 5.2 y Python 3.13 o superior.
- [uv](https://docs.astral.sh/uv/) para gestionar dependencias y el entorno virtual.
- SQLite para desarrollo local.
- Informe editable en `doc/informe.odt`.

No se necesitan React, Vite, Bun ni Node.js.

## Desarrollo

Instala uv y ejecuta:

```bash
cd app
uv sync --locked
uv run manage.py migrate
uv run manage.py runserver
```

La aplicación estará disponible en http://127.0.0.1:8000/.
Un único servidor ejecuta tanto la interfaz como la lógica de la aplicación.

La configuración inicial es exclusivamente para desarrollo. Las variables de
`app/.env.example` documentan las opciones disponibles; Django las lee del
entorno del proceso, no carga automáticamente un archivo `.env`.

## Estructura

```text
app/
├── config/          # Configuración, rutas y pruebas de Django
├── templates/       # Dashboard principal de Star Admin
├── static/          # CSS y futuros archivos JavaScript e imágenes
├── manage.py
├── pyproject.toml
└── uv.lock
doc/
└── informe.odt      # Informe del proyecto
```

La página de inicio utiliza `app/templates/home.html`, adaptada del dashboard
principal de **Star Admin 2 Free (BootstrapDash)**. Sus recursos compilados se
encuentran en `app/static/staradmin/`, con las fuentes e imágenes utilizadas
por sus estilos. No se requiere instalar dependencias de JavaScript ni compilar.
Se conservan los gráficos y datos de demostración; no están conectados a modelos.
No se incluyen las demás páginas de ejemplo del template.

Se conserva `/api/health/` como comprobación del servicio y `/admin/` como
panel administrativo de Django. Para crear un administrador:

```bash
cd app
uv run manage.py createsuperuser
```

## Comprobaciones

Desde `app/`:

```bash
uv run manage.py check
uv run manage.py test
```

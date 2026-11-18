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
├── templates/       # Login, dashboard y registro de mascota
├── static/          # CSS y futuros archivos JavaScript e imágenes
├── manage.py
├── pyproject.toml
└── uv.lock
doc/
└── informe.odt      # Informe del proyecto
```

Las pantallas utilizan los estilos de **Star Admin 2 Free (BootstrapDash)**.
Sus recursos compilados se
encuentran en `app/static/staradmin/`, con las fuentes e imágenes utilizadas
por sus estilos. No se requiere instalar dependencias de JavaScript ni compilar.
El dashboard se ha simplificado sin gráficos ni estadísticas ficticias.
Comparte la navegación con el registro de mascotas mediante `app/templates/base.html`.
La identidad visual de **Inversiones Mundo Agropecuario CAM** se aplica al
dashboard, al login y al registro mediante `app/static/css/branding.css`, cargado después
de los estilos de Star Admin sin modificar los archivos del proveedor. La
paleta compartida utiliza verde `#73BF36`, verde oscuro `#3B7324` (para mejorar
el contraste con blanco), marrón carbón `#3E3733` y blanco `#FFFFFF`.
El logo original está en `app/static/branding/logo CAM.jpg.jpeg`; se conserva
su formato JPEG y su proporción. Los colores de estado mantienen sus distinciones originales.

También se incluye la pantalla de inicio de sesión en `/login/`, adaptada al
español en `app/templates/login.html` y con los mismos recursos locales de Star
Admin. Por ahora es únicamente una vista: no valida credenciales ni crea
sesiones y el botón de ingreso está deshabilitado. El dashboard sigue siendo
público en `/`. No se incluyen registro de usuarios, recuperación de contraseña, acceso con
redes sociales ni las demás páginas de ejemplo del template.

La tercera vista es `/mascotas/registrar/` (`app/templates/pet_register.html`).
Incluye los campos de Animal: identificador automático no editable, cliente,
especie, raza, nombre, fecha de nacimiento, sexo, peso inicial en kg, color y
observaciones. Los catálogos son ejemplos y el botón de guardar está deshabilitado:
no se crean modelos, registros ni sesiones. Se pueden editar y limpiar los campos
para revisar la interfaz. Las tres pantallas están enlazadas entre sí.

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

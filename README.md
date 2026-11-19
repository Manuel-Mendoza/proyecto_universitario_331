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
Incluye un resumen de mascotas, ventas del día, stock bajo y medicamentos
próximos a vencer; alertas de inventario; una tabla vacía de últimas mascotas
y un acceso al formulario de registro. Los indicadores sin información se
representan con «—» y las tablas muestran un estado vacío, sin cifras ficticias.
Los vencimientos se plantean por lote. No se manejan citas ni agenda y no
se agregan vistas de ventas o inventario en esta etapa.
Comparte la navegación con el registro de mascotas mediante `app/templates/layouts/app.html`.
La identidad visual de **Inversiones Mundo Agropecuario CAM** se aplica al
dashboard, al login y al registro mediante `app/static/css/branding.css`, cargado después
de los estilos de Star Admin sin modificar los archivos del proveedor. La
paleta compartida utiliza verde `#73BF36`, verde oscuro `#3B7324` (para mejorar
el contraste con blanco), marrón carbón `#3E3733` y blanco `#FFFFFF`.
Todos los colores propios se definen en el `:root` de `branding.css` por su
función: `--primary`, `--secondary`, `--texto`, `--texto-secundario`,
`--texto-inverso`, `--fondo`, `--superficie` y `--borde`. También se reservan
`--exito`, `--error`, `--advertencia` e `--informacion` para los estados.
El hover, fondo suave, foco y sombra se derivan con `color-mix()` de los
colores base; se pueden ajustar en el mismo bloque. Para cambiar el tema,
edita ese `:root`: las reglas de botones, formularios, tarjetas, tablas y
layouts consumen las variables, sin colores propios escritos fuera de él.
El logo es una imagen y no cambia al modificar las variables CSS.
El logo original está en `app/static/branding/logo CAM.jpg.jpeg`; se conserva
su formato JPEG y su proporción. Los colores de estado mantienen sus distinciones originales.

También se incluye la pantalla de inicio de sesión en `/login/`, adaptada al
español en `app/templates/accounts/login.html` y con los mismos recursos locales de Star
Admin. Por ahora es únicamente una vista: no valida credenciales ni crea
sesiones y el botón de ingreso está deshabilitado. El dashboard sigue siendo
público en `/`. No se incluyen registro de usuarios, recuperación de contraseña, acceso con
redes sociales ni las demás páginas de ejemplo del template.

La tercera vista es `/mascotas/registrar/` (`app/templates/pets/register.html`).
Incluye los campos editables de Animal: cliente,
especie, raza, nombre, fecha de nacimiento, sexo, peso inicial en kg, color y
observaciones. Especie y raza contienen opciones ilustrativas; el selector de
cliente está vacío y el botón de guardar está deshabilitado:
no se crean modelos, registros ni sesiones. Se pueden editar y limpiar los campos
para revisar la interfaz. Las tres pantallas están enlazadas entre sí.

### Plantillas reutilizables

```text
app/templates/
├── base.html                 # Documento HTML, estilos y favicon comunes
├── layouts/
│   ├── app.html              # Estructura del dashboard y formularios
│   └── auth.html             # Estructura de acceso, sin menú lateral
├── components/
│   ├── brand.html            # Logo compartido
│   ├── sidebar.html          # Navegación y enlace activo
│   ├── header.html
│   ├── footer.html
│   └── stat_card.html        # Tarjeta de indicador
├── accounts/login.html
├── dashboard/home.html
└── pets/register.html
```

Las páginas heredan un layout con `{% extends %}` y definen su título y
contenido con bloques. Los fragmentos se insertan con `{% include %}` y `only`
para recibir únicamente sus parámetros explícitos. Por ejemplo:

```django
{% include 'components/stat_card.html' with title='Mascotas registradas' value='—' value_label='Sin información' only %}
```

`stat_card.html` recibe `title`, `value` y una etiqueta accesible opcional
`value_label`. El menú recibe `active_page` desde el layout. El contenido
específico de cada pantalla permanece en su plantilla, sin componentes para
elementos que todavía no se reutilizan. Esta organización no cambia las rutas
ni incorpora autenticación, modelos o guardado.

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

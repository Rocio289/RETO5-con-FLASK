# 🔎 Reto 5 Flask y HTML: Buscador de Clientes


Aplicación web desarrollada con **Flask** como parte del reto 5.  
Permite buscar clientes en un archivo CSV por su **DNI** y mostrar el detalle de cada uno.

---

##  Estructura del proyecto

- run.py → Punto de entrada de la aplicación.  
-  miapp/routes.py → Define las rutas y vistas.
- miapp/utils.py → Funciones auxiliares, como lectura de clientes desde CSV.
- clientes.csv → Base de datos de clientes en formato CSV.
- templates/ → Plantillas HTML.
- static/ → Archivos estáticos (CSS, JS, imágenes).

---

##  Requisitos previos

Debes tener instalado en tu sistema:

Python 3.10+
pip (gestor de paquetes de Python)
virtualenv (opcional, pero recomendado)


---

##  Instalación y configuración

1. Clonar el repositorio:

git clone https://github.com/TU_USUARIO/TU_REPO.git
cd reto5-flask


2. Crear un entorno virtual:

python -m venv entorno


3. Activar el entorno virtual:

- En **Windows (PowerShell)**:

.\entorno\Scripts\Activate.ps1



- En **Linux/Mac**:

source entorno/bin/activate



4. Instalar dependencias:

pip install -r requirements.txt


---

##  Ejecución de la aplicación

Ejecutar con:

python run.py



La aplicación estará disponible en:

http://127.0.0.1:5000/



---

##  Funcionalidad

- Página principal con un **formulario** para buscar clientes por DNI.  
- Si se encuentra, muestra el resultado con un enlace a su detalle.  
- Si no se encuentra, muestra un mensaje de error.  
- Página de detalle con la información del cliente.  
- Página de error **404** personalizada.

---


##  Autoría

Proyecto desarrollado por **Rocío Martínez**  
Curso: KeepCoding Cero > Reto 5 con Flask
README - PracticaDocker3

Aplicación web de login desarrollada con Flask, conectada a MySQL, y dockerizada usando Docker Compose.

Repositorio: [https://github.com/DanielsGHIES/PracticaDocker3.git](https://github.com/DanielsGHIES/PracticaDocker3.git)

Requisitos:

* Docker
* Docker Compose
* Navegador web

Despliegue:

1. Clonar el repositorio:
   git clone [https://github.com/DanielsGHIES/PracticaDocker3.git](https://github.com/DanielsGHIES/PracticaDocker3.git)
   cd PracticaDocker3

2. Construir y levantar contenedores:
   sudo docker-compose up -d

3. Acceder a la aplicación en el navegador:
   [http://localhost:8080](http://localhost:8080)

Credenciales de prueba:

* Correo: [test@ejemplo.com](mailto:test@ejemplo.com)
* Contraseña: 123456

Estructura del proyecto:
PracticaDocker3/
├─ app.py
├─ requirements.txt
├─ docker-compose.yml
├─ Dockerfile
├─ static/
│   ├─ styles.css
│   └─ script.js
├─ templates/
│   ├─ index.html
│   └─ home.html
└─ README.md

Notas importantes:

* La contraseña de MySQL está en docker-compose.yml, cambiar en producción.
* Flask está en modo desarrollo, usar WSGI server en producción.
* Archivos del login organizados bajo containerLogin en CSS.

Autor: Daniel Gutierrez ([https://github.com/DanielsGHIES](https://github.com/DanielsGHIES))

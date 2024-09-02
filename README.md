# **Práctica Final: Dockers**

## **Descripción**

Este proyecto es una **aplicación web** para gestionar una base de datos de **adopción de mascotas**, desarrollada usando **Flask** y **MySQL**. Utiliza **Docker** y **Docker Compose** para facilitar la configuración y despliegue.

## **Requisitos Previos**

- **Docker**
- **Docker Compose**

## **Configuración**
La aplicación Flask y MySQL se configuran a través de **variables de entorno**, lo que permite una gran flexibilidad y facilita la configuración en diferentes entornos.

### **Variables de Entorno**
Puedes definir las siguientes **variables de entorno** para configurar la conexión a la base de datos:

- **DB_HOST**: El nombre del servicio o la dirección IP del contenedor MySQL.
- **DB_PORT**: El puerto en el que MySQL escucha dentro del contenedor.
- **DB_USER**: El nombre de usuario para conectarse a la base de datos.
- **DB_PASSWORD**: La contraseña para el usuario de la base de datos.
- **DB_NAME**: El nombre de la base de datos.

## **Archivo .env**
Crea un archivo `.env` en el directorio raíz del proyecto para definir estas variables de entorno. Aquí tienes un ejemplo de archivo `.env`:

```plaintext
DB_HOST=mysql-container
DB_PORT=3306
DB_USER=root
DB_PASSWORD=rootpassword
DB_NAME=mydb
```
## **Estructura del Proyecto**
La estructura del proyecto es la siguiente:


Entendido. Aquí tienes cómo deberías formatear el contenido en tu archivo README.md para que la estructura del proyecto se muestre en líneas separadas:

markdown
Copy code
## **Estructura del Proyecto**

La estructura del proyecto es la siguiente:

## Estructura del Proyecto
La estructura del proyecto es la siguiente:
```
.
├── app.py                   # Archivo principal de la aplicación Flask
├── Dockerfile               # Dockerfile para construir la imagen de la aplicación Flask
├── docker-compose.yml       # Configuración de Docker Compose
├── .env                     # Archivo para las variables de entorno
├── migrations/              # Directorio para las migraciones de base de datos (si usas Flask-Migrate)
└── requirements.txt         # Archivo con las dependencias de Python
```
## Configuración de Puertos
Si el puerto predeterminado de MySQL (3306) está en uso por otro servicio en tu máquina host, puedes cambiar el puerto expuesto en el archivo docker-compose.yml. Por ejemplo, para mapear el puerto 3306 del contenedor al puerto 3307 en tu máquina host, puedes modificar la configuración de la siguiente manera en el archivo yml:
```
ports:
  - "3307:3306"
```
## Ejecución de la Aplicación
1.	Construir y levantar los contenedores: Este comando construirá las imágenes para la aplicación Flask y la base de datos MySQL, y luego iniciará los contenedores.
```bash
docker-compose up --build
```
2. Verificar los Contenedores en Ejecución:
```bash
docker-compose ps
```
3.	Parar y eliminar los contenedores:
```bash
docker-compose down
```
## Añadir datos a la BBDD

Para añadir datos a la base de datos, se utiliza curl para hacer solicitudes HTTP a la API.
### Añadir un Usuario
```bash
curl -X POST http://localhost:8080/usuarios \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Sonia Martin",
    "email": "sonia.martin@example.com",
    "direccion": "Calle Piruleta 004",
    "CP": "28031",
    "localidad": "Madrid"
}'
```
### Añadir un Perro
```bash
curl -X POST http://localhost:8080/perros \
-H "Content-Type: application/json" \
-d '{
    "nombre": "Firulais",
    "raza": "Labrador",
    "idUsuario": 1
}'
```
### Añadir un Historial de Adopciones
```bash
curl -X POST http://localhost:8080/historialAdopciones \
-H "Content-Type: application/json" \
-d '{
    "fecha": "2024-08-22",
    "idUsuario": 1,
    "idPerro": 1
}'
```

## **Uso**

Una vez que los contenedores estén en ejecución, la aplicación Flask estará disponible en [http://localhost:8080](http://localhost:8080).

Puedes acceder a los siguientes endpoints:

- **GET /perros**: Obtiene una lista de todos los perros.
- **POST /perros**: Agrega un nuevo perro (requiere un cuerpo de solicitud con los campos necesarios).
- **GET /usuarios**: Obtiene una lista de todos los usuarios.
- **POST /usuarios**: Agrega un nuevo usuario (requiere un cuerpo de solicitud con los campos necesarios).
- **GET /historialAdopciones**: Obtiene el historial de adopciones.


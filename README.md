# **Configuración de Logs con Grafana y Loki**

## **Descripción**

Este documento detalla los pasos necesarios para configurar Grafana y Loki para capturar y visualizar logs en formato JSON utilizando Docker Compose.

## **Requisitos Previos**

- **Docker**
- **Docker Compose**

## **Configuración**
### Configuración del archivo docker-compose.yml para que defina los servicios para Grafana, Loki y Promtail.
### Creación de archivo de configuración para Loki llamado loki-config.yml.
### Creación de archivo de configuración para Promtail llamado promtail-config.yml.

### **Construir y levantar los contenedores**
```bash
docker-compose up -d
```
## **Acceso**
### **Acceso a Grafana**

- Abre tu navegador web y navega a http://localhost:3000.

- Iniciar Sesión, usando las credenciales predeterminadas:
```plaintext
Usuario: admin
Contraseña: admin123
```
### **Configurar Loki en Grafana**
- Crear data source:
1. En la barra lateral izquierda, haz clic en el ícono de engranaje (⚙️) y selecciona “Data Sources” (Fuentes de datos).
2. Haz clic en “Add data source” (Añadir fuente de datos).
3. Selecciona Loki.
4.  En URL, introduce http://localhost:3100.
5.  Haz clic en “Save & Test” para guardar la configuración y verificar la conexión.
- Crear un Dashboard
1. En la barra lateral izquierda, haz clic en el ícono “+” y selecciona “Create” (Crear) > “Dashboard” (Panel).
2. Haz clic en “Add new panel” (Añadir nuevo panel).
3. Selecciona Loki como la fuente de datos.
4. En la sección “Query” (Consulta), escribe una consulta para filtrar los logs. Por ejemplo: {job="varlogs"}.
5. Guarda el panel y el dashboard.
6. Ver Logs
Una vez que hayas configurado el dashboard, podrás ver y analizar los logs capturados en tiempo real. Puedes ajustar las consultas y visualizaciones para adaptarlas a tus necesidades específicas.

## **Errores**
En mi caso, al tener la aplicación en una máquina virtual no me reconocía el localhost. No he podido ver los logs.


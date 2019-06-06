# Zen Coin
Aplicación que simula el uso de una moneda electrónica.

## API
Fue desarrollada en Flask, usando librerías como flask-restful, flask-mail y mongoengine para la interacción con la base de datos.

## Requerimientos
Es necesario tener instaladas las siguientes librerías:</br></br>
1 - <b>Python</b> en su versión 3.x: Para ello dirigirse al siguiente <a href="https://www.python.org/downloads/" target="_blank">link</a></br>
2 - <b>Flask:</b> Instalarlo es sencillo, deben abrir la consola CMD en windows o terminal en linux y ejecutar el comando <b>pip install flask</b>.</br>
3 - <b>Dependencias de Flask:</b> Deben ejecutar en la consola el siguiente comando: <b>pip install flask-restful flask-mail flask-corn</b>.</br>
4 - <b>MongoDB:</b> Para instalar MongoDB deben dirigirse a la página oficial en el siguiente <a href="https://www.mongodb.com/download-center/community" target="_blank">enlace</a>, descargar el ejecutable e instalarlo.</br>
5 - <b>Mongoengine:</b> ORM utilizado para implementar los modelos de la aplicación. Para instalarlo deben ejecutar el comando <b>pip install mongoengine</b>.</br></br>
<i>NOTA:</i> Para aquellos que no posean el administrador de paquetes <b>PIP</b>, deben instalarlo.</br></br>

## Instalación
Para su instalación, se debe descargar el proyecto utilizando el comando <b>git clone https://github.com/Rokethor/zencoin.git</b></br>
Una vez descargado, se debe ingresar a la carpeta y ejecutar alguno de los siguientes comandos:</br>
1 - <b>python development.py</b> ---> Este comando levantará el servicio de la aplicación en un estado de debug, ya que tiene configuraciónes pre establecidas para fines de desarrollo.</br>
2 - <b>python main.py</b> ---> A diferencia del comando anterior, este levanta el servicio en estado productivo.

## Configuración de BBDD
Para que la aplicación se enlace de manera correcta con la base de datos, es necesario configurar los datos correspondientes en el archivo <b>config.py</b>.</br>
En este archivo, encontrarán las clases Development y Production. La clase Development se encarga de brindar la configuración al archivo development.py, mientras que la clase Production se encarga de la configuración del archivo main.py.</br>
Los datos relevantes a configurar para establecer la conexión con la base de datos son:</br>
1 - MONGODB_DB: Aquí debe colocarse el nombre de la base de datos.</br>
2 - MONGODB_HOST: Aquí debe ir la IP del Host. Si se ejecuta en un entorno local para fines de desarrollo, puede simplemente configurarse como localhost.</br>
3 - MONGODB_PORT: Aquí debe configurarse el puerto por el cual accederá.
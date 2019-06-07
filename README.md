# Zen Coin
Aplicación que simula el uso de una moneda electrónica.

## API
Fue desarrollada en Flask, usando librerías como flask-restful, flask-mail y mongoengine para la interacción con la base de datos.

## Frontend
Desarrollado en React.js, utilizando dependencias como react-router-dom y prop-types. Consume la API con axios.

## Instalación
Se debe descargar el proyecto utilizando el comando <b>git clone https://github.com/Rokethor/zencoin.git</b></br>
Una vez descargado, se debe ingresar a la carpeta y ejecutar alguno de los siguientes comandos:</br></br>
1 - <b>python development.py</b> ---> Este comando levantará el servicio de la aplicación en un estado de debug, ya que tiene configuraciónes pre establecidas para fines de desarrollo.</br>
2 - <b>python main.py</b> ---> A diferencia del comando anterior, este levanta el servicio en estado productivo.</br></br>

<i>Nota:</i> Para que la aplicación pueda ser ejecutada correctamente deben de tener todos los requerimientos explicados en el siguiente apartado.

## Requerimientos
Es necesario tener instaladas las siguientes librerías:</br></br>
1 - <b>Python</b> en su versión 3.x: Para ello dirigirse al siguiente <a href="https://www.python.org/downloads/">link</a>.</br>
2 - <b>virtualenv:</b> Instalarlo es sencillo, deben abrir la consola CMD en windows o terminal en linux y ejecutar el comando <b>pip install virtualenv</b>.</br>
3 - <b>Dependencias:</b> Deben generar una máquina virtual con el comando <b>python -m venv myvenv</b>, siendo myvenv la carpeta donde se creará. Luego deben levantar la máquina virtual ejecutando el comando myvenv/Scripts/activate. Por último deben acceder a la carpeta requirements ubicada en la carpeta ZenApi y ejecutar el comando <b>pip install -r requirements.txt</b>.</br>
4 - <b>MongoDB:</b> Para instalar MongoDB deben dirigirse a la página oficial en el siguiente <a href="https://www.mongodb.com/download-center/community">enlace</a>, descargar el ejecutable e instalarlo.</br>
5 - <b>Node.js y NPM:</b> Esto es necesario para poder levantar el servicio del Frontend.</br>
6 - <b>React.js:</b> Idem punto 5.

## Configuración de BBDD
Para que la aplicación se enlace de manera correcta con la base de datos, es necesario configurar los datos correspondientes en el archivo <b>config.py</b>.</br>
En este archivo, encontrarán las clases Development y Production. La clase Development se encarga de brindar la configuración al archivo development.py, mientras que la clase Production se encarga de la configuración del archivo main.py.</br></br>
Los datos relevantes a configurar para establecer la conexión con la base de datos son:</br></br>
1 - MONGODB_DB: Aquí debe colocarse el nombre de la base de datos.</br>
2 - MONGODB_HOST: Aquí debe ir la IP del Host. Si se ejecuta en un entorno local para fines de desarrollo, puede simplemente configurarse como localhost.</br>
3 - MONGODB_PORT: Aquí debe configurarse el puerto por el cual accederá.</br>
4 - Luego de realizar las configuraciones, es necesario que se ejecute el script de migraciones ubicado en la raíz de la API con el siguiente comando: <b>python migrate.py -e 'environment'</b>. 'environment' se debe reemplazar por 'development' o 'production'. Esta separación es para realizar la migración en la base de datos de desarrollo o productiva.

# Importante
El desarrollo no se encuentra finalizado, en el transcurso del desarrollo me vi limitado por falta de conocimiento sobre react.js, por lo que faltan detalles como el redireccionamiento de las páginas. Lo que se debe hacer para probar la aplicación es:</br></br>
1 - Autenticarse. Una vez se hayan logueado, no arrojará un aviso. En caso de no haber coincidido la combinación de email y contraseña, mostrará un mensaje de error.</br>
2 - Acceder a la ruta de la cuenta del usuario ('/panel'). Desde allí se podrá comenzar a operar sobre el sistema y realizar transferencias.</br>
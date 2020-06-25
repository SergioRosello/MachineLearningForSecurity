# Detección de Botnets usando Redes Neuronales

## Datos del estudiante

* **Nombre:** Sergio 
* **Apellidos:** Roselló Morell
* **DNI:** 53632974X
* **email:** Sergio-resello@hotmail.con

## Información sobre el entorno

* **Sistema Operativo:** Arch Linux
* **Entorno de escritorio:** dwm
* **Versión de Python:** Python 3.8.2
* **Editor de texto:** NeoVim
* **Generación del documento:** Escrito en MD, compilado a LaTeX con 

> `nnoremap <leader>e :! pandoc % -f markdown -t latex -s -o %:r.pdf<cr>`

## Resumen

En el trabajo de investigación a continuación, se va a revisar el uso de redes neuronales para catalogar y detectar Botnets en la red.
Los pasos que se realizan engloban de forma general cualquier problema de Machine Learning, en el que se obtiene el dataset, se trata, para que contenga los valores deseados, se entrena la red neuronal, se genera el modelo y se revisa, para luego refinar el resultado.

## Indice

* Planteamiento
    * Descripción y planteamiento del problema
    * Descripción de los datasets a utilizar
    * Algoritmos de AA que se pretenden usar 
    * Resultados esperados del proceso
* Implementación
    * Programas utilizados
    * Modificaciones sobre los datos
    * Pasos de ejecución
    * Limitaciones/restricciones en la implementación
* Pruebas y resultados
    * Proceso a seguir para obtener los datos
    * Aplicación de los programas/scripts
    * Casos comprobados y valores de datos iniciales y de parámetros
    * Resultados obtenidos e interpretación de los datos

## Planteamiento

### Descripción y planteamiento del problema

El problema que se plantea en este análisis es identificar trafico de red malicioso en una red a tiempo real.

La solución debe poder analizar a tiempo real los paquetes generados por la red y decidir si cada paquete individual es o no un paquete proveniente de un malware.

Este problema se adapta muy bien a una solución relacionada con Inteligencia Artificial.
Mas en concreto, a modelos como las redes neuronales.

El principal inconveniente a la hora de solucionar un problema de selección en tiempo real con modelos tradicionales, aparece cuando se pretende analizar el trafico y compararlo con varios ejemplos de malware.
Ya sea comparando directamente pequeños atributos, como el paquete de red entero, al final, estamos comparando con características que ya conocemos e identificamos como maliciosas.
Esto quiere decir que estamos reaccionando al problema, no tomando medidas pro-activas al problema en quistión.
La finalidad del problema es ser capaces de detectar malware, aunque no se haya detectado anteriormente el tipo especifico de malware siendo analizado.

Solucionar el problema en cuestión con métodos tradicionales, como bien puede ser comprobaciones secuenciales de características del paquete de red a analizar incrementa rápidamente la complejidad del algoritmo.
Ademas, cada vez que se detecten nuevos casos, se debe integrar la comprobación al programa.
Esto hace que sea imposible mantenerlo actualizado.

Existen otras técnicas, no tan primitivas, como por ejemplo comprobación de hashes, tanto completos, como parciales del paquete de red.
Si podemos identificar las características comunes en los paquetes de red enviados entre el malware y el servidor C&C, podemos cifrar estos datos en hashes, que se revisaran contra los paquetes de red a medida que pasan por la red.

### Descripción de los datos a utilizar

Para desarrollar un modelo de detección de paquetes maliciosos, lo mas importante es la calidad de los datos iniciales que tenemos.
Si generamos el modelo con datos buenos, el modelo puede inferir, en muchas ocasiones el trafico de red maligno.

Es muy importante tener unos datos tanto específicos, como generales, con distintas muestras y combinaciones de paquetes de red malignos, ya que estos son la parte mas critica del proyecto.

Como se ha mencionado superficialmente en la sección anterior, un modelo de detección basado en una red neuronal esta preparado para operar en un entorno de producción, en el que los paquetes de red que va a revisar no son exactamente iguales que con los que ha entrenado, de esta forma, entrenando con un conjunto de datos lo suficientemente rico, podemos inferir la clase del paquete de red.

En el caso del entrenamiento del modelo, vamos a seleccionar un dataset realista, que contenga tanto trafico de red benigno como maligno y varios ejemplos de cada tipo.

#### Selección de Dataset de entrenamiento

Se ha usado la pagina web de [www.secrepo.com](www.secrepo.com) para buscar un dataset que contenga las propiedades deseadas para el estudio.

Las cualidades que se necesitan en el dataset son:

* Trafico de malware hacia servidores C&C
* Trafico de aplicaciones no maliciosas
* Cantidad de información (Necesario para poder inferir comportamientos y generar modelos de datos)

Siguiendo los requisitos demarcados anteriormente, se han encontrado varios datasets, entre estos, se va a usar `ISOT HTTP Botnet Dataset`, desarrollado por Alenazi A y compañeros para una charla con titulo: "Intelligent, Secure, and Dependable Systems in Distributed and Cloud Environments".

Este dataset ha sido generado por la universidad de Victoria en el año 2017 y consiste en nueve capturas de trafico malicioso y 19 capturas de trafico de aplicaciones no maliciosas, como por ejemplo Dropbox o Avast.

Cada registro se puede trazar directamente a una IP que contiene únicamente el programa a analizar, ya sea malware o no.
Esto quiere decir que el dataset es claro, de forma que se puede analizar de forma manual y llegar a una serie de conclusiones desde el primer momento.
Esto nos permite deducir los posibles resultados del análisis con el algoritmo de aprendizaje automático.

Es importante que tanto los paquetes maliciosos como los corrientes se hayan capturado al mismo tiempo ya que es una de las formas que tenemos para generar un fragmento de entrenamiento y test verídico.

Una de las ventajas de este dataset frente a otros que también cumplían los requisitos es que los datos vienen en un formato `.pcap`.
Este detalle permite al investigador tomar el control de la información que se va a añadir al `.csv` para proporcionar al programa de generación del modelo.

#### Datos sobre los que opera el modelo en producción

Una vez este el modelo terminado, va a ser puesto en un punto estratégico de la red, en el que tiene visibilidad de los paquetes entrantes y salientes de la misma.
Un sitio en el que podría estar es en el router o switch de la red, actuando de firewall.

Cuando este desplegado, este sistema revisa cada paquete que entra o sale de la red y avisa (En caso de IDS) o ejecuta medidas preventivas (En caso de IPS) según el tipo de paquete que detecte.

En principio, si el modelo ha sido entrenado correctamente, no hace falta volver a entrenarlo con mas datos, pero si lo ponemos y vemos que no detecta correctamente el tipo de paquete que analiza, puede que tengamos un problema de especificidad de datos.
El dataset que hemos seleccionado para entrenar el modelo es bastante especifico, tiene datos concretos de aplicaciones concretas, como Dropbox, pero no de trafico realista de red, como usuarios buscando cosas en Google o otras aplicaciones diversas.
En caso de que el modelo no detecte correctamente los paquetes maliciosos es obtener una muestra de nuestra propia red y analizar su trafico, junto con muestras de botnets.

### Posibles algoritmos de aprendizaje automático a usar

En la asignatura cursada, se han realizado estudios sobre algoritmos de 'clustering', Clasificación, Probabilidad y 'Del Learning'

Teniendo en cuenta los algoritmos que se han aprendido durante el curso, se decide ahondar mas en los recursos sobre `Deep Learning`.

Los motivos por esta selección, entre otros son:

* Modelo adaptado al problema
* Preferencia personal

#### Breve comparación de los algoritmos estudiados
(Como se realiza el proceso (Transformación de datos e interpretación)

Hay dos grandes categorías de redes neuronales:

* RNN (Recurrent Neural Networks)
    * LSTM (Long Short-Term Memory)
* CNN (Convolutional Neural Networks)

#### Por que Redes neuronales

Entre los distintos tipos de redes neuronales existentes, se ha optado por entrenar el modelo con <++>

#### Elección del framework

A la hora de generar el modelo, nos encontramos con varias opciones para llegar a la misma finalidad.
Entre las opciones, tenemos:

* SciKit, un framework de aprendizaje automático
* PyTorch, un framework de aprendizaje profundo
* Keras, un framework de aprendizaje profundo

Viendo las opciones anteriores, decidimos usar Keras, debido a su versatilidad y abstracción de los algoritmos de aprendizaje profundo.
Este framework nos puede proporcionar la potencia de varios frameworks de redes neuronales como TensorFlow, Theano o CNTK.
Nosotros vamos a usar Keras en combinación con TensorFlow para generar el modelo.

Mas concretamente, vamos a usar el modelo `sequential_model` para generar nuestra red neuronal.

#### Gestión de datos (Entrenamiento, modelado, normalizarlos, categóricos)

Hay una serie de cambios que son necesarios hacer cuando se adapta un dataset de datos crudos a un dataset valido para ser la entrada de un modelo.

Los pasos que se van a tener que seguir son:

* Seleccionar _features_ con las que nos quedamos
* Convertir datos a `csv`
* Sanado el dataset
* Determinar datos categóricos y continuos
* Codificar datos categóricos y continuos
* Dividir el dataset en datos de prueba y entrenamiento

##### Elección de 'features'

Una de las decisiones mas importantes cuando seleccionamos un dataset es saber que los datos están disponibles de la forma mas pura posible.
Esto hace que sea mas complicado trabajar con ellos desde un inicio, debido a que se tienen que convertir y mutar para que sirvan como datos de entrada al modelo, pero la ventaja que tienen es que no son específicos, es decir, los mismos datos, pueden servir para solucionar distintos problemas.

En nuestro caso, al tener acceso a los datos en formato `pcap`, podemos decidir que datos nos interesan, de entre una gran variedad de posibilidades.

##### Conversión de datos a csv

Los algoritmos de aprendizaje automático como las redes neuronal usan una matriz como datos de entrada.
Una de las formas mas similares a las matrices, son las tablas `csv`, en la que la relación es evidente.
Se van a tener que mutar los datos crudos a datos con formato `csv`, que luego leeremos con `python` para importar a nuestro modelo.

##### Sanado de dataset

Es posible que el dataset generado tras convertir los datos de `pcap` a `csv` contenga errores.
Un ejemplo de error es que cualquier campo no tenga valor.
Si se detecta este error, debemos arreglarlo, ya que para las redes neuronales, es mejor que todos los campos tengan un valor. 
En este caso, el valor nulo lo cambiamos a `UNKNOWN`.
Todos estos errores deben ser contemplados y arreglados.

##### Determinar datos categóricos y continuos

Las variables categóricas son las que pueden obtener valores concretos, predefinidos dentro de una serie de posibilidades.

Las variables continuas, son las que pueden obtener valores infinitos, es decir, existe una infinidad de valores continuos.
Estas variables suelen ser numéricas.

##### Codificar datos categóricos y continuos

Tanto las variables categóricas como las continuas, se deben codificar de una forma especifica para que la red neuronal interprete los valores correctamente.

Las formas mas populares de codificar las variables categóricas es con encodeado `one-hot`, mientras que las continuas, se pueden encodear normalizando sus valores.

##### Dividir el dataset en entreno y test

Es buena practica subdividir el dataset en dos.
Estas dos secciones serán la sección de entreno y la sección de prueba.
El modelo se entrena con la sección de entreno, pero se reserva una sección, por lo general del 30% del tamaño del dataset para revisar el modelo al acabar la fase de entreno.
Una de las razones por las que se hace esto, es para asegurarnos que nuestro modelo funciona correctamente.
Esto es porque hemos usado unos datos para entrenar a nuestro modelo, pero estos datos, ya los ha visto, y el modelo se ha configurado de acorde con estos.
A nosotros nos interesa generar un modelo que sea capaz de decidir con datos que no se hayan usado nunca, ya que esta es su finalidad.

### Resultados esperados del proceso

Cuando se acabe de entrenar el modelo, este nos proporciona un porcentaje de acierto, basado en los datos de test.
Este sera siempre nuestro limite superior de probabilidad de acierto.
Una vez estemos satisfechos con este valor, si satisface nuestros requisitos a nivel de red, podremos desplegar el modelo.

## Implementación

### Programas utilizados

Para realizar este ejercicio, se ha contado con una plataforma creada por Google específicamente para realizar proyectos de estas características.
Aun así, todo lo que se puede ver a través del siguiente enlace <++>, se puede hacer desde el ordenador personal del lector.

Se van a separar los programas utilizados en local y en la plataforma de Google.

#### En local, Programas/Ayudas utilizadas

Los programas que he usado para realizar estas tareas son:

* Python
* bash
* tshark
* head
* tail
* sort
* NeoVim

#### En remoto

Se usa un framework hecho por Google llamado colaboratory, que deja todo preparado para realizar análisis de datos para Aprendizaje Automático.
Tiene la forma de los cuadernos Jupiter y permite tener código y texto en una misma vista.

#### Importación del dataset a Python

En este dataset conviven tanto datos categóricos como continuos.

Se ha tomado la decisión de no incluir los datos del `epoch_date` ya que no van tienen mucha relevancia a la hora de generar la red neuronal.

Los datos son categóricos, debemos cambiarlos a datos `dummy` antes de que los use el algoritmo de generación del modelo.
Para realizar este paso, usamos la codificación `one-hot`.

Los datos continuos, debemos normalizarlos, para eso, tenemos que asignar 0 al valor mas bajo y 1 al valor mas alto.
Una vez tengamos el dataset tratado para ser ingerido por el modelo de la red neuronal, podemos empezar a entrenar, con un 70% del dataset, para posteriormente revisar con un 30% del dataset.

La parte del script que genera esta nueva matriz se encuentra en el documento de Google llamado `PracticaFinal.ipynb`.
Los pasos que se toman para generara el dataset son:

#### Leer el `.csv`

En este paso, se usa el método `read_csv` de `pandas`, pasándole los tipos de datos que se va a encontrar en cada columna, para optimizar mas la carga del dataset.
Ademas, se le dice al método el numero de linea en el que se encuentra el nombre de cada columna.

#### Preparar la tabla

En esta sección, se codifican los datos categóricos y continuos en una matriz que el modelo es capaz de entender y utilizar.

Los métodos que se han usado para cifrar los datos son:

* _OneHotEncoder_ de sklearn.preprocessing
* _Normalize_ de sklearn.preprocessing

### Pasos de ejecución

Con el dataset incluido en la entrega del presente documento, seria suficiente cargar el entorno de Google colaboratory y ejecutar uno a uno los bloques.

En caso de no querer usar el entorno on-linea, se puede llegar al mismo resultado ejecutando los bloques de código presentes en la plataforma on-linea o el script con el nombre `model.py`.

### Limitaciones/restricciones en la implementación

Este modelo es capaz de discriminar los paquetes de red maliciosos de los comunes teniendo en cuenta el grupo reducido de paquetes que se ha usado.
A día de hoy, no se puede asegurar el funcionamiento del modelo con datos o programas maliciosos cuyo trafico no se ha capturado y utilizado para generar el modelo.
Dicho esto, es probable que el modelo pueda inferir en mayor o menor medida trafico no revisado anteriormente.

## Pruebas y resultados

### Proceso a seguir para obtener los datos

Vamos a establecer el directorio principal desde el cual trabajaremos durante todo el ejercicio.
De ahora en adelante, esta sera la carpeta base de esta practica. (`~/`)
Este se llama: 

> `TrabajoFinal`

#### 1. Configuración del espacio de trabajo

Descargamos el dataset desde la siguiente URL: [ISOT HTTP Botnet Database](https://drive.google.com/open?id=1LW-FNhgqTZfYswHSLPUxtwccwM75O4J4) a nuestro directorio raíz.

Extraemos el dataset en este directorio, de forma que se crea un directorio llamado `isot_app_and_botnet_dataset`.

#### 2. Tratado de datos

Copiar los scripts:

* `extraction.sh`
* `sanitize.py`
* `identifyAndsort.sh`
* `prepareData.sh`

Al directorio llamado `isot_app_and_botnet_dataset`.

Una vez tenemos estos archivos en nuestro directorio, procedemos a **ejecutar el `script` `extraction.sh`.**
Este script convierte todos los datos de `pcap` a `csv`. 
Ademas, concatena todos los datasets con paquetes maliciosos en un dataset que contiene únicamente paquetes maliciosos y todos los datasets con trafico legitimo en un solo dataset que contiene únicamente paquetes legítimos.

Seguimos **ejecutando el script `sanitize.py`**, que elimina las comas extra que contiene el campo `_ws.col.Info` y ademas, rellena los valores nulos con el valor *UNKNOWN*.

Al terminar la operación anterior, añadimos una columna extra a cada uno de los datasets, para que el modelo pueda identificar que paquete de red es legitimo y cual es *Botnet*.
Ademas, unimos y ordenamos por tiempo los paquetes de red.
Esto se hace **ejecutando el comando identifyAndsort.sh**

Como alternativa, se ha preparado un script que automáticamente genera los archivos indicados para importar con `Python`.
**Ejecutando prepareData.sh**.
Es necesario tener los requisitos necesarios por `Python` para ejecutar el script de `Python`.
Estos están en el archivo `requirements.txt`.
Para **instalar los requisitos, se ejecuta el comando `pip install -r requirements.txt`**

### Aplicación de los programas/scripts

El script en el que se define el modelo y se entrena se llama `model.py`.

Para **ejecutar este archivo, se puede usar el comando `python model.py`**

Automáticamente, se encodea el dataset para poder usarse con el modelo, se genera el modelo, se entrena el mismo y se calcula el porcentaje de aciertos basándose en los datos de prueba.

### Casos comprobados y valores de datos iniciales y de parámetros

### Resultados obtenidos e interpretación de los datos

### Otros valores a revisar

En esta practica se ha usado el modulo `sequential_model`, debido a que es una red neuronal sencilla, pero seria muy interesante entrenar el modelo con modelos mas avanzados, que contengan neuronas compartidas entre capas, distintas, entradas y salidas por capa o grafos de capas.
TODO

## Posibles mejoras

El dataset ha sido generado en una misma red.
Cada maquina ha estado enviando trafico especifico de un malware concreto.
Esto es beneficioso, porque podemos identificar a simple vista (Según la IP) si ese trafico es malicioso o no.
El inconveniente que introduce este método es que no es trafico de red verdadero, ya que en la vida real, una sola maquina genera trafico tanto normal como malicioso.

Otro inconveniente de la forma en la que se ha capturado el dataset es que los datos malignos se han capturado antes que los normales, haciendo que, si se ordena todo el dataset, todo el trafico de red este segmentado por naturaleza.

# Comentarios sobre la realización de la actividad

# Bibliografía 

* *Neural networks*:
    * `https://scikit-learn.org/stable/modules/
    neural_networks_supervised.html`
* *Dataset*:
    * Alenazi A., Traore I., Ganame K., Woungang I. (2017) Holistic Model for HTTP Botnet 
Detection Based on DNS Traffic Analysis. In: Traore I., Woungang I., Awad A. (eds) Intelligent, 
Secure, and Dependable Systems in Distributed and Cloud Environments. ISDDC 2017. Lecture 
Notes in Computer Science, vol 10618. Springer, Cham 
* *one_not encoding*
    * `https://scikit-learn.org/stable/modules/
    generated/sklearn.preprocessing.OneHotEncoder.html`
* *Categorical_functions*
    * `https://keras.io/api/utils/python_utils
    /#to_categorical-function`
* *read_csv*
    * `https://pandas.pydata.org/pandas-docs/
    stable/reference/api/pandas.read_csv.html`
* *Keras sequential model*:
    * `https://keras.io/guides/sequential_model/`
* *Keras training and evaluation*:
    * `https://keras.io/guides/training_with_built_in_methods/`
* *Keras functional model*:
    * `https://keras.io/guides/functional_api/`

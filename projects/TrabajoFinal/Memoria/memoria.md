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

(Ventajas de IA sobre métodos tradicionales)

En el presente documento se estudia la capacidad que tiene un modelo generado por una red neuronal en determinar si el trafico de red que analiza es benigno o malicioso.
Una aplicación de un modelo de estas características puede ser un sistema de prevención o detección de riesgos.
Una aplicación así puede ser una gran ayuda en una red industrial critica, empresarial o incluso domestica.
Ademas, si se mantiene actualizada la red neuronal con las ultimas características de los paquetes de red que generan programas maliciosos, aumentamos el nivel de precisión a la hora de detectar la amenaza interna.

Siguiendo por las lineas del comentario anterior, una de las ventajas de los modelos de redes neuronales es que son capaces de distinguir entre trafico benigno y maligno aunque no haya paquetes de red que cumplan exactamente con las características analizadas.
Esta flexibilidad hace que sea el tipo perfecto de comprobación de trafico de red, ya que la mayoría de los paquetes de red que revise el modelo no se van a repetir, pero es capaz de detectar su tipo, basándose en algunos aspectos clave del paquete.


### Descripción de los datos a utilizar

(Entrenamiento y pruebas)
(Fuente en caso real y fuente en este caso ficticio)

Como se ha mencionado superficialmente en la sección anterior, un modelo de detección basado en una red neuronal esta preparado para operar en un entorno de producción, en el que los paquetes de red que va a revisar no son exactamente iguales que con los que ha entrenado, de esta forma, entrenando con un conjunto de datos lo suficientemente rico, podemos inferir la clase del paquete de red.

#### Selección de Dataset

Se ha usado la pagina web de [www.secrepo.com](www.secrepo.com) para buscar un dataset que contenga las propiedades deseadas para el estudio.

Las cualidades que se necesitan en el dataset son:

* Trafico de malware hacia servidores C&C
* Trafico de aplicaciones no maliciosas
* Cantidad de información (Necesario para poder inferir comportamientos y generar modelos de datos)

Siguiendo los requisitos demarcados anteriormente, se va a usar uno de los datasets que satisfacen los requisitos.

Este dataset ha sido generado por la universidad de Victoria en el año 2017 y consiste en nueve capturas de trafico malicioso y 19 capturas de trafico de aplicaciones no maliciosas, como por ejemplo Dropbox o Avast.

Cada registro se puede trazar directamente a una IP que contiene únicamente el programa a analizar, ya sea malware o no.
Esto quiere decir que el dataset es claro, de forma que se puede analizar de forma manual y llegar a una serie de conclusiones desde el primer momento.
Esto nos permite deducir los posibles resultados del análisis con el algoritmo de aprendizaje automático.

Es importante que tanto los paquetes maliciosos como los corrientes se hayan capturado al mismo tiempo ya que es una de las formas que tenemos para generar un fragmento de entrenamiento y test verídico.

Una de las ventajas de este dataset frente a otros que también cumplían los requisitos es que los datos vienen en un formato `.pcap`.
Este detalle permite al investigador tomar el control de la información que se va a añadir al `.csv` para proporcionar al programa de generación del modelo.

### Algoritmos de AA que se pretenden usar 

Debido a una curiosidad por modelos basados en redes neuronales y a la cabida de los anteriores en un proyecto de detección de malware como este, se ha decidido optar por las redes neuronales como principal algoritmo de generación del modelo.

#### Breve comparación de los algoritmos estudiados
(Como se realiza el proceso (Transformación de datos e interpretación)

#### Posibles algoritmos a usar

#### Por que Redes neuronales

#### Elección del framework

A la hora de generar el modelo, nos encontramos con varias opciones para llegar a la misma finalidad.
Entre las opciones, tenemos:

* SciKit, un framework de aprendizaje automático
* PyTorch, un framework de aprendizaje profundo
* Keras, un framework de aprendizaje profundo

Viendo las opciones anteriores, decidimos usar Keras, debido a su versatilidad y abstracción de los algoritmos de aprendizaje profundo.
Este framework nos puede proporcionar la potencia de varios frameworks de redes neuronales como TensorFlow, Theano o CNTK.
Nosotros vamos a usar Keras en combinación con TensorFlow para generar el modelo.

### Resultados esperados del proceso
(Interpretación)


## Implementación

### Programas utilizados

#### En local, Programas/Ayudas utilizadas

Los programas que he usado para realizar estas tareas son:

* Python
* bash
* tshark
* head
* tail
* sort
* NeoVim
#
#### En remoto

Se usa un framework hecho por Google llamado colaboratory, que deja todo preparado para realizar análisis de datos para Aprendizaje Automático.
Tiene la forma de los cuadernos Jupiter y permite tener código y texto en una misma vista.

### Modificaciones sobre los datos

#### Generación y formato del dataset

Es importante extraer las propiedades que nos interesan en el dominio del problema al que nos encontramos, de lo contrario, sufriremos problemas de rendimiento, especialmente cuando tratamos con datasets muy grandes e incluso podemos llegar a generar un modelo menos preciso, debido a la cantidad de información irrelevante que introducimos en la generación del modelo.

Se trata de hallar el punto intermedio que nos proporcione los mejores resultados posibles con la menor dimensionalidad posible.
Existen multitud de estudios realizados únicamente pare hallar las mejores propiedades.
Como esta no es nuestra finalidad, se procederá a determinar las propiedades por relevancia percibida.

Las propiedades que vamos a extraer del dataset son:

* epoch_date
* Source
* Destination
* Protocol
* Length
* Info

* `epoch_date` es importante porque cabe la posibilidad de que el programa se comunique con el servidor C&C de forma constante.
* Aunque `Source` es aparentemente uno de los campos mas importantes, es posible que no sea tan relevante en la generación del modelo.
Puede ser interesante hacer un estudio, para averiguar si es necesario tener dicho campo como propiedad, pero como no es nuestra prioridad, se incluye, a riesgo de sobreaprendizaje.
Una de las consecuencias que temo, es que sobre aprenda dado que cada dirección IP genera un campo especifico de trafico.
En un entorno de producción, esto no es lo común, ya que cada dirección IP genera mas variedad de trafico.
* `Destination` es un indicador claro de un programa malicioso.
Aunque estamos en una situación parecida a la mencionada anteriormente com `Source`, independientemente de la dirección IP desde la que se genera el trafico, la dirección `Destination` va a ser la misma, por tanto, si que se va a incluir esta propiedad.
* `Protocol` Puede ser uno de los indicadores clave para identificar el malware, aunque en mi opinión, debería ser tratado como un comprobante, no como una primera decisión.
* Al igual que la propiedad anterior, `Length` es un buen comprobante para revisar el tipo de paquete.
* `Info` proporciona información adicional que se puede usar para discriminar un paquete malicioso.

Los pasos que vamos a realizar para generar un dataset correcto para analizar los datos son los siguientes:

* Extraer los datos necesarios de las capturas de red a archivos `.csv` independientes
* Sanitizamos el dataset, para que los campos no tengan ningún símbolo prohibido
* Añadimos una columna a cada dataset para indicar si son botnets o trafico de red convencional

Para extraer los datos del dataset, hemos usado la herramienta `tshark`, que permite convertir flujos de red (Codificados en un archivo con extensión `.pcap`) en archivos `.csv`.
Esta es la extensión que se usa para entrenar la red neuronal.

El proceso anteriormente descrito, se realiza con el script llamado `extraction.sh`.

Aunque se haga exactamente el mismo procedimiento en ambos bucles, es necesario distinguirlos porque tenemos que añadir una columna (y) a cada dataset, para indicar si es trafico malicioso o regular.

Uno de los problemas al que me he tenido que enfrentar es que el archivo generado por la herramienta `tshark` es que a pesar de indicarle que los separadores de datos se codifican con el carácter `,`, ha incluido valores en los campos que incluyen el valor `,`. 
Debido ha esto, se ha tenido que generar el script `sanitize.py`, que revisa el numero de apariciones de cada `,` en cada linea del archivo.
Si es mayor al numero de columnas predefinidas, elimina el carácter del archivo.

Ahora, queda añadir a cada archivo una columna para indicando si el paquete de red es uno benigno o malicioso.
Este ejercicio aparece en el script `identifyAndsort.sh`.

En este momento, tenemos los archivos de red benignos y los maliciosos organizados y configurados para ser analizados.

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

#### Preparar la table

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

### Aplicación de los programas/scripts

### Casos comprobados y valores de datos iniciales y de parámetros

### Resultados obtenidos e interpretación de los datos

### Otros valores a revisar

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

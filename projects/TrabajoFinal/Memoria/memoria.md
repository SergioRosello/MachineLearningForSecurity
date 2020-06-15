
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

### Apartado 1 - Obtención de datos

#### 1.1 Selección de Dataset

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

Es importante que tanto los paquetes maliciosos como los corrientes se hayan capturado al mismo tiempo ya que es una de las formas que tenemos para generar un fragmento de entrenamiento y test.

Una de las ventajas de este dataset frente a otros que también cumplían los requisitos es que los datos vienen en un formato '.pcap'.
Este detalle permite al investigador tomar el control de la información que se va a añadir al '.csv' para proporcionar al programa de generación del modelo.

### Apartado 2 - Extracción, Codificación y Vectorización de propiedades

Es importante extraer las propiedades que nos interesan en el dominio del problema al que nos encontramos, de lo contrario, sufriremos problemas de rendimiento, especialmente cuando tratamos con datasets muy grandes e incluso podemos llegar a generar un modelo menos preciso, debido a la cantidad de información irrelevante que introducimos en la generación del modelo.

Se trata de hallar el punto intermedio que nos proporcione los mejores resultados posibles con la menor dimensionalidad posible.
Existen multitud de estudios realizados únicamente pare hallar las mejores propiedades.
Como esta no es nuestra finalidad, se procederá a determinar las propiedades por relevancia percibida.

#### 2.1 Extracción

Las propiedades que podemos usar son:

* No.
* Time
* Source
* Destination
* Protocol
* Length
* Info

De las cuales, vamos a quedarnos con todas excepto 'No.' y 'Source'.

* 'Time' es importante porque cabe la posibilidad de que el programa se comunique con el servidor C&C de forma constante.
* Aunque 'Source' es aparentemente uno de los campos mas importantes, es posible que no sea tan relevante en la generación del modelo.
Seria interesante hacer un estudio, para averiguar si es necesario tener dicho campo como propiedad.
Una de las consecuencias que temo, es que sobre aprenda dado que cada dirección IP genera un campo especifico de trafico.
En un entorno de producción, esto no es lo común, por tanto, tomo la decisión de eliminar dicho campo.
* 'Destination' es un indicador claro de un programa malicioso.
Aunque estamos en una situación parecida a la mencionada anteriormente com 'Source', independientemente de la dirección IP desde la que se genera el trafico, la dirección 'Destination' va a ser la misma, por tanto, si que se va a incluir esta propiedad.
* 'Protocol' Puede ser uno de los indicadores clave para identificar el malware, aunque en mi opinión, debería ser tratado como un comprobante, no como una primera decisión.
* Al igual que la propiedad anterior, 'Length' es un buen comprobante para revisar el tipo de paquete.
* 'Info' proporciona información adicional que se puede usar para discriminar un paquete malicioso.

Al tener varios archivos, 


#### 2.2 Codificación

#### 2.3 Vectorización

### Apartado 3 - Generación del modelo

#### Valores de parámetros se han usado

#### Modificaciones de código

#### Fallos o errores y solución

### Apartado 4 - Comprobación del modelo

### Apartado 5 - Posibles mejoras

## Comentarios y opiniones

#### Dificultades/Problemas encontradas

#### Programas/Ayudas utilizadas

Los programas que he usado para realizar estas tareas son:

* Python
* sort
* shuf
* NeoVim y su capacidad de búsqueda y sustitución

## Comentarios sobre la realización de la actividad

## Bibliografía 

* *Neural networks*:
    * 'https://scikit-learn.org/stable/modules/
    neural_networks_supervised.html'
* *Dataset*:
    * Alenazi A., Traore I., Ganame K., Woungang I. (2017) Holistic Model for HTTP Botnet 
Detection Based on DNS Traffic Analysis. In: Traore I., Woungang I., Awad A. (eds) Intelligent, 
Secure, and Dependable Systems in Distributed and Cloud Environments. ISDDC 2017. Lecture 
Notes in Computer Science, vol 10618. Springer, Cham 

# HPC
## Tópicos Especiales en Telemática: Proyecto 3 – Clústering de Documentos a partir de Métricas de Similitud

Este proyecto plantea los retos de un típico buscador en la web (Google, Facebook, Amazon, Spotify, Netflix, entre otros), en los que se necesitan sistemas de recomendación que sugieran busquedas relacionadas, en donde se requiere hacer procesamiento natural del lenguaje, etc. 
El diseño e implementación de este algoritmo ha sido pensado para ejecutarse en paralelo, usando los diferentes núcleos independendiente del número que sean, gracias al uso del paradigma de paso de mensaje **(MPI)**.
El reto a afrontar es el clustering de un conjunto de documentos utilizando el algoritmo de k–means y una métrica de similaridad entre documentos. Para este úlitimo caso la métrica que usamos fue el algoritmo **Jaccard** que se puede encontrar paralelizar fácilmente. Los tipos de datos a usar son los fundamentales y los que ofrece python como los diccionarios y numpy_arrays. La estrategia de paralelización que usamos es la del tipo "embarazosamente" paralela, pues dividimos el set de datos entre los diferentes nodos sin necesitar comunicación entre ellos, es una estructura del tipo master-slave y la tecnología a utilizar es MPI principalmente y bibliotecas standares como numpy.

#### Análisis comparativo de datasets procesados

A continuación una tabla de tiempos mostrando las diferentes implementaciones vs. los datasets que probamos

| __Tabla de Tiempos__ | __Archivos Locales__ | __Gutenberg__ 
| :-----------:     | :------: | :------: |
| Serial         |  0.017442941665649414 seg   | +2h
| Paralelo Distribuído  | 0.011871099472045898   | +1h

### Documentación de Usuario

##### Requisitos
* Tener instalado Python 2.7 y mpi4py (`pip install mpi4py`)
* Tener un dataset: https://drive.google.com/file/d/0B2Mzhc7popBga2RkcWZNcjlRTGM/edit
* Copiar el dataset desde la maquina local al DCA:
`pscp C:\Users\MauricioHoyosArdila\Downloads\Gutenberg.zip jzapat80@192.168.10.115:/home/jzapat80`

Para cambiar la k diríjase** al código en el main en la línea 110 (sujeto a cambios), ahí está la k explícita

** Tenga en cuenta que esta es una aplicación no interactiva, ya que lo que se requiere es poder usarla en un clúster MPI, por lo que para hacer cambios a la k debe hacerse de esta manera.

Para ejecutar el código serial:
`python ./serialDocumentClustering.py <folder con archivos>`

Para ejecutar el código paralelo:
`mpiexec -np <numero de nucleos en su maquina> python ./parallelDocumentClustering.py <folder con archivos>`

### Referencias:

* [Algoritmo Jaccard] https://en.wikipedia.org/wiki/Jaccard_index
* [Deep Jaccard Documentation] http://www.iaeng.org/publication/IMECS2013/IMECS2013_pp380-384.pdf
* [Dataset Gutenberg] https://drive.google.com/uc?id=0B_4oKjh0Qca5RWlGZkRRT1pVLU0&export=download

## Código de Honor

En este projecto reconocemos los créditos y autoría de componentes reutilizados de otros proyectos a nivel de código fuente,
documentación (correcta citación), diseños o algoritmos. Este algoritmo se diseñó en colaboración con otros compañeros de la materia.

Yo, Jonathan Zapata, reconozco que el trabajo es auténtico, original, no copiado, no enviado a realizar por un tercero, y reconozco a los terceros que aportaron al proyecto directa o indirectamente.
Yo, Mauricio Hoyos, reconozco que el trabajo es auténtico, original, no copiado, no enviado a realizar por un tercero, y reconozco a los terceros que aportaron al proyecto directa o indirectamente.



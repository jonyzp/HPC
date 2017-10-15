# HPC
## Tópicos Especiales en Telemática: Proyecto 3 – Clústering de Documentos a partir de Métricas de Similitud

Este proyecto plantea los retos de un típico buscador en la web (Google, Facebook, Amazon, Spotify, Netflix, entre otros), en los que se necesitan sistemas de recomendación que sugieran busquedas relacionadas, en donde se requiere hacer procesamiento natural del lenguaje, etc. 
El diseño e implementación de este algoritmo ha sido pensado para ejecutarse en paralelo, usando los diferentes núcleos independendiente del número que sean, gracias al uso del paradigma de paso de mensaje **(MPI)**.
El reto a afrontar es el clustering de un conjunto de documentos utilizando el algoritmo de k–means y una métrica de similaridad entre documentos. Para este úlitimo caso la métrica que usamos fue el algoritmo **Jaccard** que se puede encontrar paralelizar fácilmente. Los tipos de datos a usar son los fundamentales y los que ofrece python como los diccionarios y numpy_arrays. La estrategia de paralelización que usamos es la del tipo "embarazosamente" paralela, pues dividimos el set de datos entre los diferentes nodos sin necesitar comunicación entre ellos, es una estructura del tipo master-slave y la tecnología a utilizar es MPI principalmente y bibliotecas standares como numpy.

#### Análisis comparativo de datasets procesados

A continuación una tabla de tiempos mostrando las diferentes implementaciones vs. los datasets que probamos

| __Tabla de Tiempos__ | __Gutenberg__ | __Dado por el artículo__
| :-----------:     | :------: | :------: |
| Serial         | 16 seg   | t
| Paralelo Distribuído  | t   | t

### Documentación de Usuario

Para cambiar la k diríjase** al código en el main en la línea 110 (sujeto a cambios), ahí está la k explícita

** Tenga en cuenta que esta es una aplicación no interactiva, ya que lo que se requiere es poder usarla en un clúster MPI, por lo que para hacer cambios a la k debe hacerse de esta manera.

Para ejecutar el código serial:
`python ./serial`

Para ejecutar el código paralelo:
`mpiexec -np <numero de nucleos en su maquina> python ./parallel`

### Referencias:

* [Algoritmo Jaccard] https://en.wikipedia.org/wiki/Jaccard_index
* [Dataset Gutenberg] https://drive.google.com/uc?id=0B_4oKjh0Qca5RWlGZkRRT1pVLU0&export=download

## Código de Honor

En este projecto reconocemos los créditos y autoría de componentes reutilizados de otros proyectos a nivel de código fuente,
documentación (correcta citación), diseños o algoritmos.

Yo, Jonathan Zapata, reconozco que el trabajo es auténtico, original, no copiado, no enviado a realizar por un tercero, y reconozco a los terceros que aportaron al proyecto directa o indirectamente.



### Solución Geométrica para un problema de optimización lineal:

La solución geométrica asociada a un problema de optimización lineal se realizó de la siguiente forma:

Paso 1: Se usan todas las restricciones del problema y se grafican en el plano como rectas.

Paso 2: Se hallan las intercepciones entre estas rectas, las cuales constituyen puntos.

Paso 3: Se elije entre todos los puntos de intercepción solo aquellos que cumplan todas las restricciones del problema, los demás se descartan.

Paso 4: Luego se usa la función objetivo para determinar cuáles son las evaluaciones de estos puntos en la misma y ordenarlos en cuanto a su valor para encontrar el mínimo y el máximo.

Paso 5: Los resultados de la evaluación se almacenan en una estructura diccionario donde el identificador es un entero entre 0 y la cantidad de puntos de intersección encontrados, después de haber sido ordenados.

Paso 6: Se crean dos listas __m__, __n__ que contienen las los valores de __x__, __y__ respectivamente de los puntos ordenados.

Paso 7: Para encontrar el mínimo se escoge de la estructura diccionario anteriormente descrita el identificador que pertenece al menor valor almacenado en este y se utiliza como posición para indexar en las listas __m__, __n__ y de esta forma obtenemos el mínimo. De igual forma obtenemos el máximo buscando el identificador del mayor valor en el diccionario.

Luego para graficar en Manim, lo que hacemos es ir siguiendo los pasos hasta obtener todos los datos necesarios tales como las rectas, las intersecciones de estas rectas que son válidas para el problema así como el punto máximo y mínimo. Hacemos aparecer las líneas, luego los puntos intersección, luego el poligono asociado a estos puntos y por último los puntos de máximo y mínimo en caso de existir.

##### Detalles del código:

Todo el proceso para hayar las intersecciones así como mínimo y máximo están en el archivo __geometric.py__ en un método llamado __geometric_aproach__, el cual recibe 4 parámetros, las restricciones en forma de listas de strings, la ecuación objetivo en forma de string y dos listas de valores __x__, __y__ con los cuales se formaran las rectas. 

Luego el proceso para graficar com Manim se encuentra en el archivo __Geo_Manim.py__ donde primero se realiza el llamado a __geometric_aproach__ para obtener todos los datos necesarios y luego se procede a graficar en orden las líneas, puntos de intersección, el polígono asociado a estos puntos y por último los puntos de máximo y mínimo.

Por último, los detalles como la función y las restricciones se almacenan en un archivo __geometric_aproach.json__ el cual se utiliza como configuración del problema a resolver.

Se utilizó como nombre de variables "x" y "y". 



### Penalty:

Método de Penalización:

Este método reemplaza la función objetivo con restricciones por una función sin restricciones, la cual es formada por:

-La función objetivo

-Un término adicional por cada constraint, que es positivo si el punto actual __x__ viola las restricciones o 0 de otra forma.

La mayoría de las formas de este método usan un coeficinetepositivo el cual se utiliza para multiplicar la parte de la funcion de las restricciones. Haciendo que este coeficiente sea más grande se penaliza más fuerte cada ves la violación de las restricciones para llegar más cerca a la región factible para el problema restringido.

Estos son considerados "exterior penalty method", dado que el término de penalización en la función para cada restricción no es 0 cuando x es no factible con respecto a esa restricción.

El método cuadrático de penalización es el que cada término de penalización es elevado al cuadrado. Además las restricciones de igualdad y desigualdad tienen distintas formas:

-igualdad: h(x) => $(h(x))^2$

-desigualdad: g(x) => $max(0, g(x))^2$

$\Phi(x)$

##### Detalles del código:

Todo el proceso para hayar las intersecciones así como mínimo y máximo están en el archivo __penalty_newton.py__ en un método llamado __penalty_newton__. 

El método se puede describir en pseudo código de la siguiente forma:

dados el coeficiente de penalización ($\mu_0$), una tolerancia ($\tau_0>0$) y un punto inicial ($x_0$)

for $k$ = 0, 1,2, . . .

​	encontrar un minimizador aproximado x_k para la función y termina cuando $||\nabla \Phi(x_k)||<= \tau_k$

​	if se satisface el test de convergencia final parar con la aproximacion $x_k$.

​	else aumentar el coeficiente de penalización y coger el punto hayado como nuevo start_point, repetir el proceso.

end ( for) 

En el proceso se va modificando la función de penalización dado que el coeficiente por el que se multiplican los términos de penalización varía.

Al final se devuelve un diccionario con la cantidad de iteraciones realizadas, los puntos intermedios y el una lista con los valores de __x__, __y__ y el resultado de evaluar la funcion en estos (__z__).

Luego el proceso para graficar com Manim se encuentra en el archivo __Penalty_Manim.py__ donde primero se realiza el llamado a __penalty_newton__ para obtener todos los datos necesarios y luego se procede a graficar en orden el eje de coordenadas, la función y los puntos resultantes.

Por último, los detalles como la función y las restricciones se almacenan en un archivo __penalty_settings.json__ el cual se utiliza como configuración del problema a resolver.

Se utilizó como nombre de variables "x" y "y". 
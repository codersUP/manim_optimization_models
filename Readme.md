# Requerimientos:

- scipy
- sympy
- numpy
- cylp

### Solución Geométrica para un problema de optimización lineal:

La solución geométrica asociada a un problema de optimización lineal se realizó de la siguiente forma:

Paso 1: Se usan todas las restricciones del problema y se grafican en el plano como rectas.

Paso 2: Se hallan las intercepciones entre estas rectas, las cuales constituyen puntos.

Paso 3: Se elije entre todos los puntos de intercepción solo aquellos que cumplan todas las restricciones del problema, los demás se descartan.

Paso 4: Luego se usa la función objetivo para determinar cuáles son las evaluaciones de estos puntos en la misma y ordenarlos en cuanto a su valor para encontrar el mínimo y el máximo.

Paso 5: Los resultados de la evaluación se almacenan en una estructura diccionario donde el identificador es un entero entre 0 y la cantidad de puntos de intersección encontrados, después de haber sido ordenados.

Paso 6: Se crean dos listas **m**, **n** que contienen los valores de **x**, **y** respectivamente de los puntos ya ordenados.

Paso 7: Para encontrar el mínimo se escoge de la estructura diccionario anteriormente descrita el identificador que pertenece al menor valor almacenado en este y se utiliza como posición para indexar en las listas **m**, **n** y de esta forma obtenemos el mínimo. De igual forma obtenemos el máximo buscando el identificador del mayor valor en el diccionario.

Luego para graficar en Manim, lo que hacemos es ir siguiendo los pasos hasta obtener todos los datos necesarios tales como las rectas, las intersecciones de estas rectas que son válidas para el problema así como el punto máximo y mínimo. Hacemos aparecer las líneas, luego los puntos intersección, luego el polígono asociado a estos puntos y por último los puntos de máximo y mínimo en caso de existir.

##### Detalles del código:

Todo el proceso para hallar las intersecciones así como el mínimo y el máximo están en el archivo **geometric.py** en un método llamado **geometric_aproach**, el cual recibe 4 parámetros, las restricciones en forma de listas de strings, la ecuación objetivo en forma de string y dos listas de valores **x**, **y** con los cuales se formarán las rectas.

Luego el proceso para graficar con Manim se encuentra en el archivo **Geo_Manim.py** donde primero se realiza el llamado a **geometric_aproach** para obtener todos los datos necesarios y luego se procede a graficar en orden las líneas, puntos de intersección, el polígono asociado a estos puntos y por último los puntos de máximo y mínimo.

Por último, los detalles como la función y las restricciones se almacenan en un archivo **geometric_aproach.json** el cual se utiliza como configuración del problema a resolver.

Luego el proceso para graficar con Manim se encuentra en el archivo **Geo_Manim.py** donde primero se realiza el llamado a **geometric_aproach** para obtener todos los datos necesarios y luego se procede a graficar en orden las líneas, puntos de intersección, el polígono asociado a estos puntos y por último los puntos de máximo y mínimo.

Por último, los detalles como la función y las restricciones se almacenan en un archivo **geometric_aproach.json** el cual se utiliza como configuración del problema a resolver.

Se utilizó como nombre de variables "x" y "y".

### Penalty:

Método de Penalización:

Este método reemplaza la función objetivo con restricciones por una función sin restricciones, la cual es formada por:

-La función objetivo.

-Un término adicional por cada constraint, que es positivo si el punto actual **x** viola las restricciones o 0 de otra forma.

La mayoría de las formas de este método usan un coeficiente positivo el cual se utiliza para multiplicar la parte de la función de las restricciones. Haciendo que este coeficiente sea más grande se penaliza más fuerte cada ves la violación de las restricciones para llegar más cerca a la región factible para el problema restringido.

Estos son considerados "exterior penalty method", dado que el término de penalización en la función para cada restricción no es 0 cuando x es no factible con respecto a esa restricción.

El método cuadrático de penalización es el que cada término de penalización es elevado al cuadrado. Además para las restricciones de igualdad y desigualdad el término de penalización tienen distintas formas:

-igualdad: h(x) => $(h(x))^2$

-desigualdad: g(x) => $max(0, g(x))^2$

$\Phi(x)$

##### Detalles del código:

Todo el proceso para hallar las intersecciones así como el mínimo y el máximo están en el archivo **penalty_newton.py** en un método llamado **penalty_newton**.

El método se puede describir de la siguiente forma:

dados el coeficiente de penalización ($\mu_0$), una tolerancia ($\tau_0>0$) y un punto inicial ($x_0$)

for $k$ = 0, 1,2, . . .

 encontrar un minimizador aproximado x_k para la función y termina cuando $||\nabla \Phi(x_k)||<= \tau_k$

 if se satisface el test de convergencia final parar con la aproximacion $x_k$.

 else aumentar el coeficiente de penalización y coger el punto hayado como nuevo start_point, repetir el proceso.

end ( for)

En el proceso se va modificando la función de penalización dado que el coeficiente por el que se multiplican los términos de penalización varía.

Al final se devuelve un diccionario con la cantidad de iteraciones realizadas, los puntos intermedios y el una lista con los valores de **x**, **y** y el resultado de evaluar la función en estos (**z**).

Luego el proceso para graficar con Manim se encuentra en el archivo **Penalty_Manim.py** donde primero se realiza el llamado a **penalty_newton** para obtener todos los datos necesarios y luego se procede a graficar en orden el eje de coordenadas, la función y los puntos resultantes.

Por último, los detalles como la función y las restricciones se almacenan en un archivo **penalty_settings.json** el cual se utiliza como configuración del problema a resolver.

Se utilizó como nombre de variables "x" y "y".

# Ramificación y acotación:

Este método se encuentra dentro del archivo `bab.py` y se utiliza para encontrar soluciones enteras en un problema de minimización agregando restricciones a medida que se va resolviendo la problemática original.

    def branch_and_bound_int(
        vars, func, constraints, initial_point, verbose=False
    ):

- vars (list[string]): variables que posee la función a minimizar
- func (string): función que se desea minimizar
- constraints (list[string]): restricciones que posee la función a minimizar
- initial_point (list[float]): punto inicial para comenzar el algorítmo de minimización
- verbose (bool) _opcional_: imprimir los pasos que va realizando el método a medida que va minimizando

Retorna:

    {
        "min": min,
        "min_values": min_values,
        "tree": tree
    }

- "min" (float): mínimo valor alcanzado
- "min_values" (list[float]): x en que se alcanza el mínimo valor
- "tree" (root): el recorrido que se realizó para alcanzar el mínimo valor

root posee la estructura:

    {
        "father": father,
        "added_constraints": added_constraints,
        "childrens": childrens,
        "lv": lv,
        "step": step,
        "initial_point": initial_point,
        "constraints": constraints,
        "best_point": best_point,
        "evaluation": evaluation,
    }

- "father" (root): el nodo padre desde el que se agregó la nueva restricción
- "added_constraints" (sp.Relational): restricción añadida con respecto al nodo padre
- "childrens" (list[root]): nodos hijos que surgen al agregar nuevas restricciones al nodo actual
- "lv" (int): nivel en el árbol del nodo(la raíz posee lv 0)
- "step" (int): indica cuantos nodos fueron procesados antes del actual
- "initial_point" (list[float]): punto inicial utilizado para la optimización del nodo actual
- "constraints" (list[constraint]): lista de restricciones utilizadas en el nodo actual
- "best_point" (list[float]): x en que se alcanza el mínimo valor en el nodo actual
- "evaluation" (float): mínimo valor alcanzado en el nodo actual

constraint posee la estructura:

    {
        "type": type,
        "fun": fun,
    }

- "type" ("eq" o "ineq"): indica si la restricción es una inecuación o una ecuación
- "fun" (lambda list[float]: float): la evaluación de la restricción en un punto dado

La idea central detrás del algorítmo es ir agregando restricciones mientras las componentes del vector no sean enteras. Por cada una de las variables no enteras se crean dos nodos hijos, asumamos que la variable no entera es x y su valor es f, entonces los dos hijos nuevos creados poseen las restricciones x <= parte_entera_por_debajo(f) y x >= parte_entera_por_debajo(f) + 1 respectivamente.

## Graficar con manim

La implementación se encuentra dentro del archivo `manim_bab.py`y se utiliza para generar una animación del proceso de optimización utilizando ramificación y acotación de una problemática planteada dentro de un archivo que debe ser creado con el nombre `bab.json`. Esta debe tener la siguiente estructura:

    {
        "vars": vars,
        "func": func,
        "constraints": constraints,
        "initial_point": initial_point,
        "u_range": u_range,
        "v_range": v_range,
        "stroke_width": stroke_width
    }

- "vars" (list[string]): las diferentes variables que se encuentran en la función a minimizar
- "func" (string): la función que se desea minimizar
- "constraints" (list[string]): las diferentes restricciones que se desean agregar
- "initial_point" (list[float]): punto inicial que se tomará para la minimización de la función
- "u_range" ([float, float]): el intervalo que se generará en el gráfico en el eje x
- "v_range" ([float, float]): el intervalo que se generará en el gráfico en el eje y
- "stroke_width" (float): grosor de las líneas en el gráfico a generar

Ejemplo:

    {
        "vars": ["x", "y"],
        "func": "- (7 * x * y / 2.71828 ** ( x ** 2 + y ** 2))",
        "constraints": ["x >= -2", "y >= -2", "x <= 2", "y <= 2"],
        "initial_point": [1, 1],
        "u_range": [-5, 5],
        "v_range": [-5, 5],
        "stroke_width": 0.5
    }

La idea central en esta función es representar la función a minimizar como centro de la animación e ilustrar los distintos nodos de la solución alcanzados mediante un recorrido del arbol de soluciones.

# Métodos numéricos para la optimización no lineal

Estos métodos se encuentran dentro de los archivos `gradient.py`, `gradient_conj` y `newton`, estos implementan el Método de gradiente, Método de gradiente conjugado y el Método de Newton respectivamente. Estos se utilizan para encontrar soluciones mínimas en una función sin restricciones, tienen la ventaja que no necesitan que la función sea lineal.

    def gradient(vars, func, initial_point, cycles=100, verbose=False):
    def gradient_conj(vars, func, initial_point, cycles=100, verbose=False):
    def def newton(vars, func, initial_point, cycles=100):

- vars (list[string]): variables que posee la función a minimizar
- func (string): función que se desea minimizar
- initial_point (list[float]): punto inicial para comenzar el algorítmo de minimización
- cycles (int): cantidad de iteraciones máximas que se desean realizar para obtener una aproximación del mínimo valor.
- verbose (bool) _opcional_: imprimir los pasos que va realizando el método a medida que va minimizando

Retorna:

    {
        "min": min,
        "min_values": min_values,
        "points": points
    }

- "min" (list[float]): x en que se alcanza el mínimo valor
- "min_values" (float): mínimo valor alcanzado
- "points" (list[point]): el recorrido que se realizó para alcanzar el mínimo valor

point posee la estructura:

En caso del Método del gradiente

    {
        "point": point,
        "value": value,
        "iteration": iteration,
        "gradient": gradient,
        "step_arrived": step_arrived,
    }

En caso del Método del gradiente conjugado

    {
        "point": point,
        "value": value,
        "iteration": iteration,
        "gradient": gradient,
        "s": s,
        "step_arrived": step_arrived,
    }

- "point" (list[float]): valores de las componentes del punto mínimo actual
- "value" (float): mínimo valor alcanzado en el punto acutal
- "iteration" (int): indica cuantos puntos fueron procesados antes del actual
- "gradient" (list[float]): Evaluación del gradiente en el punto actual
- "s" (list[float]): En caso del Método del gradiente este valor no está presente pues siempre es el opuesto del gradiente, pero en el Método del gradiente conjugado, este valor se recalcula en cada iteración con respecto a resultados de este anteriores y por esto se almacena.
- "step_arrived" (float): tamaño de paso utilizado en la iteración anterior para llegar al punto actual.

En el caso del Método de Newton

    list(float)

Las ideas detrás de estos algoritmos consiste en dado un punto inicial desplazarse en una dirección que asegure que la función disminuya, para esto se hace uso de las derivadas de la función en cada componente y se desplaza en sentido contrario al gradiente. Para calcular cuanto debe ser el desplazamiento en una dirección se optimiza el tamaño del paso utilizando un algoritmo de optimización de una sola variable.

## Graficar con manim

La implementación se encuentra dentro del archivo `manim_numerical_optimization.py`y se utiliza para generar una animación del proceso de optimización utilizando distintos métodos de optimización numérica para problemas no lineales, la problemática debe estar planteada dentro de un archivo que debe ser creado con el nombre `numerical_optimization.json`. Esta debe tener la siguiente estructura:

    {
        "vars": vars,
        "func": func,
        "initial_point": initial_point,
        "u_range": u_range,
        "v_range": v_range,
        "stroke_width": stroke_width
        "cycles": cycles
    }

- "vars" (list[string]): las diferentes variables que se encuentran en la función a minimizar
- "func" (string): la función que se desea minimizar
- "initial_point" (list[float]): punto inicial que se tomará para la minimización de la función
- "u_range" ([float, float]): el intervalo que se generará en el gráfico en el eje x
- "v_range" ([float, float]): el intervalo que se generará en el gráfico en el eje y
- "stroke_width" (float): grosor de las líneas en el gráfico a generar
- "cycles" (int): cantidad de iteraciones máximas que se desean realizar para obtener una aproximación del mínimo valor.

Ejemplo:

    {
        "vars": ["x", "y"],
        "func": "- (7 * x * y / 2.71828 ** ( x ** 2 + y ** 2))",
        "initial_point": [1, 1],
        "u_range": [-5, 5],
        "v_range": [-5, 5],
        "stroke_width": 0.5,
        "cycles": 500
    }

La idea central en esta función es representar la función a minimizar como centro de la animación e ilustrar los distintos puntos de la solución alcanzados mediante un recorrido de la lista de soluciones de los distintos métodos.



## Planos cortantes

Dado un problema lineal de optimización con restricciones, el método construct de la escena Canvas en /src/cutting_planes/gomory_cutting_planes.py se encarga de computar los cortes, basado en la estrategia de cortes de Gomory para problemas con solución entera, del problema especificado en el archivo /src/cutting_planes/model_cp.json



**Un ejemplo de entrada**:

```json
{
  "vars": ["x", "y"],
  "func": "2*x-3*y",
  "constraints": ["x + 3*y <= 5", "2*x + y <= 6", "-x <= 0", "-y <= 0"],
  "x_range": [0, 8],
  "y_range": [0, 8],
  "A": [[ 1,  3],
  [  2,  1],
  [  -1,  0],
  [  0,  -1]
  ],
  "b": [5, 6, 0, 0],
  "c": [2, -3]
}
```

Se deben especificar las variables a usar, así como las restricciones con signo <=, la función a optimizar debe estar escrita en términos que permitan minimizarla, es decir, se debe utilizar el opuesto de los coeficientes si se desea hallar el máximo. Además, deben proveerse la matriz A, y vectores b,c, de manera tal que el problema sea expresado como $$\min{ca} ~~\text{tal que}~~ Ax \leq b$$.

Primeramente, se cargan de entrada en el método **load_cp_model** del módulo **input_parser**, el cual recibe como parámetro la ubicación del archivo que contiene los datos, en este caso, por defecto se hará:

 load_cp_model('./src/cutting_planes/model_cp.json')



Con esto, se graficarán las restricciones del problema, y luego utilizando una versión modificada del método bnSolve de la libería coinor.cuppy, cuya versión modificada se adjunta con el código de nuestro proyecto dentro de /src/cutting_planes/cuttingPlanes.py

Para graficar las restricciones se hace un preprocesamiento, donde se detectan aquellas restricciones de la forma $$x \leq c$$, con c constante, pues de estas restricciones no es posible generar una función lambda que pasarle a manim para graficar, y como alternativa se usa la función get_vertical_line.

Para computar los cortes además existen dos métodos, especificado como parámetro a la función bnSolve. Uno de ellos, el más eficiente, es gomoryMixedIntegerCut, el cual en ocasiones genera cortes con coeficientes extremadamente grandes. Esto no es necesariamente malo, pero manim a la hora de representar esto tiene bugs visuales debido a la manera en que grafica, de modo que pueden aparecer varios cortes en lugar de uno. Esto ocurre con el ejemplo adicional provisto en el archivo **module_cp_2.json**. Como alternativa, se puede usar el método liftAndProject. Este, por otra parte, es considerablemente más ineficiente y genera múltiples cortes innecesarios, en cambio, las representaciones visuales son más exactas.

Una vez obtenidos los cortes, estos se grafican, luego se agregan los ejes de coordenadas para rápida referencia. Finalmente, agregamos el punto óptimo calculado y sus coordenadas a la escena.





## Búsqueda en la línea

Dado un problema de optimización(no necesariamente lineal) con restricciones, la función construct de la escena ThreeDCanvas en /src/line_search/line_search.py se encarga de computar el punto óptimo para el problema especificado en el archivo /src/line_search/model_ls.json

**Ejemplo de input**:

```json
{
  "vars": ["x", "y"],
  "func": "x**2 *y",
  "constraints": ["x**2 + y**2 <= 3"],
  "initial_point": [1, 1],
  "x_range": [-2,2],
  "y_range": [-2,2],
  "camera_phi": 45,
  "camera_theta": -45
  
}
```

Se deben especificar las variables a usar, así como las restricciones con signo <=, la función a optimizar debe estar escrita en términos que permitan minimizarla, es decir, se debe utilizar el opuesto de los coeficientes si se desea hallar el máximo. También se debe especificar un punto inicial, así como el rango de x e y que se desea graficar. Opcionalmente, debido a que muchas veces las funciones obstruirán los puntos que se desean ver, o directamente obstruirán la cámara en su totalidad, se pueden especificar los ángulos de rotación para la cámara centrada en la escena.



Primeramente se  procesarán los datos del problema especificados en el archivo de input, el cual por defecto será /src/line_search/model_ls.json. Se creará un objeto de tipo Surface para graficar la función principal con los valores de x_range y y_range dados. Además, se colocará la cámara en el ángulo especificado, y se hará rotar a la misma con respecto a la escena, debido a que en ocasiones la complejidad de las funciones con las que se trabaja hará muy tedioso el proceso de ajustar la cámara a un ángulo específico para observar los puntos óptimos computados.

Para hallar el valor óptimo mediante la estrategia de búsqueda en la línea utilizamos como dirección de descenso siempre el opuesto al gradiente de la función evaluada en el punto inicial, llamémosle a este valor $D$. Luego utilizando la función scipy.line_search, calculamos el valor de $\alpha$ óptimo por el cual debemos multiplicar el opuesto del gradiente, y posteriormente nos movemos en esa dirección p*alpha unidades, de manera que si el punto del q partimos es $p_0$, avanzaríamos hasta $p_1=p_0+\alpha D$. Si el punto que obtenemos siguiendo esta idea cumple con todas las restricciones del problema, si no se detecta un descenso infinito, y si la diferencia entre el k-ésimo punto y el k+1-ésimo punto computado es mayor que cierta tolerancia, actualizamos el valor del gradiente que utilizaremos para la siguiente iteración, y seguimos el ciclo en la línea 78, en caso contrario, graficamos los puntos obtenidos luego de obtener sus coordenadas con respecto al eje de coordenadas de tres dimensiones que utilizamos como punto de referencia para la escena.
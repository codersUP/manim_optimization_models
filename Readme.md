# Requerimientos:

- scipy
- sympy
- numpy

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

Todo el proceso para hayar las intersecciones así como el mínimo y el máximo están en el archivo **geometric.py** en un método llamado **geometric_aproach**, el cual recibe 4 parámetros, las restricciones en forma de listas de strings, la ecuación objetivo en forma de string y dos listas de valores **x**, **y** con los cuales se formarán las rectas.

Luego el proceso para graficar con Manim se encuentra en el archivo **Geo_Manim.py** donde primero se realiza el llamado a **geometric_aproach** para obtener todos los datos necesarios y luego se procede a graficar en orden las líneas, puntos de intersección, el polígono asociado a estos puntos y por último los puntos de máximo y mínimo.

Por último, los detalles como la función y las restricciones se almacenan en un archivo **geometric_aproach.json** el cual se utiliza como configuración del problema a resolver.

Luego el proceso para graficar com Manim se encuentra en el archivo **Geo_Manim.py** donde primero se realiza el llamado a **geometric_aproach** para obtener todos los datos necesarios y luego se procede a graficar en orden las líneas, puntos de intersección, el polígono asociado a estos puntos y por último los puntos de máximo y mínimo.

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

Todo el proceso para hayar las intersecciones así como el mínimo y el máximo están en el archivo **penalty_newton.py** en un método llamado **penalty_newton**.

El método se puede describir de la siguiente forma:

dados el coeficiente de penalización ($\mu_0$), una tolerancia ($\tau_0>0$) y un punto inicial ($x_0$)

for $k$ = 0, 1,2, . . .

​ encontrar un minimizador aproximado x_k para la función y termina cuando $||\nabla \Phi(x_k)||<= \tau_k$

​ if se satisface el test de convergencia final parar con la aproximacion $x_k$.

​ else aumentar el coeficiente de penalización y coger el punto hayado como nuevo start_point, repetir el proceso.

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

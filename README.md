# Requerimientos:

- scipy
- sympy
- numpy

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
- "tree" (root): el recorrido que se realizo para alcanzar el mínimo valor

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

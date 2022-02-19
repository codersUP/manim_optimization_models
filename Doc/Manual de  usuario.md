### Informe para el usuario:

Este sería un ejemplo de como ejecutar el programa, el flag **-ql** es para la calidad, la **l** significa low, existen otros como **m**, **h**, **k** los cuales corresponden a medium, high y 4k respectivamente. Se debe tener cuidado al usar estos por el consumo de CPU. También podemos añadirle **-p** al flag anterior quedando **-pql** para que al terminar de ejecutar el programa muestre el resultado en un video. Los demás parámetros deben ser el nombre del .py a ejecutar y el nombre de la clase que implementa las clases de Manim. El flag --format=gif es usado para que el archivo que retorne sea en formato gif y no un video.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 18-04-38.png)

Un ejemplo del proceso del programa.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-37-20.png)

Cuando llegue aquí ya terminó el proceso y muestra el path donde se encuentra el archivo.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-38-00.png)

Esta sería la configuración del **penalty_settings.json** la cual consiste en 2 objetos, el primer string corresponde a la función objetivo y el segundo es una lista con las restricciones descritas a través de strings. Los otros parámetros son más específicos del método de penalización, la cantidad de iteraciones como caso de parada, el coeficiente de penalización, el valor para aumentar este, los rangos de x y las y.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-47-22.png)

Esta sería la configuración del **geometric_aproach.json** la cual consiste en 2 objetos, el primer string corresponde a la función objetivo y el segundo es una lista con las restricciones descritas a través de strings.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-47-32.png)

A continuación tenemos ejemplos de lo realizado.

![drag-gif](./imagenes utilizadas/Screenshot from 2022-02-18 18-15-49.png)

![drag-gif](./imagenes utilizadas/Screenshot from 2022-02-18 18-15-17.png)

Aquí podemos observar como sería el resultado de graficar una función con esta herramienta en 3d.

![drag-gif](./imagenes utilizadas/Screenshot from 2022-02-18 17-52-55.png)

![drag-gif](./imagenes utilizadas/Screenshot from 2022-02-18 18-15-38.png)

### Ramificación y acotación:

Para realizar una animación del método de ramificación y acotación se debe definir un json con el nombre `bab.json` que posea la siguiente estructura:

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

Podemos poner como ejemplo:

    {
        "vars": ["x", "y"],
        "func": "- (7 * x * y / 2.71828 ** ( x ** 2 + y ** 2))",
        "constraints": ["x >= -2", "y >= -2", "x <= 2", "y <= 2"],
        "initial_point": [1, 1],
        "u_range": [-5, 5],
        "v_range": [-5, 5],
        "stroke_width": 0.5
    }

Este json anterior nos daría como resultado una animación como se muestra en la siguiente imagen:

![drag-gif](./imagenes utilizadas/bab3d.jpg)

En cambio si lo modificamos para que posea una sola variable obtendremos algo como el siguiente ejemplo:

![drag-gif](./imagenes utilizadas/bab2d.jpg)

### Métodos numéricos para la optimización no lineal

Para realizar una animación del Método del gradiente, Método del gradiente conjugado y el Método de Newton se debe definir un json con el nombre `numerical_optimization.json` que posea la siguiente estructura:

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

Podemos poner como ejemplo:

    {
        "vars": ["x", "y"],
        "func": "- (7 _ x _ y / 2.71828 ** ( x ** 2 + y \*\* 2))",
        "constraints": ["x >= -2", "y >= -2", "x <= 2", "y <= 2"],
        "initial_point": [1, 1],
        "u_range": [-5, 5],
        "v_range": [-5, 5],
        "stroke_width": 0.5,
        "cycles": 500
    }

Este json anterior nos daría como resultado una animación como se muestra en la siguiente imagen:

![drag-gif](./imagenes utilizadas/no3d.jpg)

En cambio si lo modificamos para que posea una sola variable obtendremos algo como el siguiente ejemplo:

![drag-gif](./imagenes utilizadas/no2d.jpg)

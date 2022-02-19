### Informe para el usuario:

Para iniciar la aplicación debe ejecutar la siguiente linea de codigo en una consola

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-19 13-18-50.png)

Este sería el menú principal de nuestra aplicación. En este damos a conocer los datos de los integrantes del equipo y del proyecto en general, así como las opciones del programa a la izquierda. 

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-19 13-13-32.png)

A continuación mostramos un ejemplo predeterminado para el problema de la solución geométrica. De esta forma se puede apreciar la forma en que se llenan las casillas de los parámetros necesarios para ejecutar este. 

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-19 13-13-53.png)

A continuación mostramos un ejemplo predeterminado para el problema de Penalización. De esta forma se puede apreciar la forma en que se llenan las casillas de los parámetros necesarios para ejecutarlo. 

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-19 13-15-47.png)

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-19 13-16-01.png)

Este sería un ejemplo de como ejecutar el programa en Manim, el flag **-ql** es para la calidad, la **l** significa low, existen otros como **m**, **h**, **k** los cuales corresponden a medium, high y 4k respectivamente. Se debe tener cuidado al usar estos por el consumo de CPU. También podemos añadirle **-p** al flag anterior quedando **-pql** para que al terminar de ejecutar el programa muestre el resultado en un video. Los demás parámetros deben ser el nombre del .py a ejecutar y el nombre de la clase que implementa las clases de Manim. El flag --format=gif es usado para que el archivo que retorne sea en formato gif y no un video.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 18-04-38.png)

Un ejemplo del proceso del programa.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-37-20.png)

Cuando llegue aquí ya terminó el proceso y muestra el path donde se encuentra el archivo.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-38-00.png)

Esta sería la configuración del **penalty_settings.json** la cual consiste en 2 objetos, el primer string corresponde a la función objetivo y el segundo es una lista con las restricciones descritas a través de strings. Los otros parámetros son más específicos del método de penalización, la cantidad de iteraciones como caso de parada, el coeficiente de penalización, el valor para aumentar este, los rangos de x y las y. Los valores del mismo se llenan a traves de la aplicación antes de ejecutar este algoritmo.

![drag-img](./imagenes utilizadas/Screenshot from 2022-02-18 17-47-22.png)

Esta sería la configuración del **geometric_aproach.json** la cual consiste en 2 objetos, el primer string corresponde a la función objetivo y el segundo es una lista con las restricciones descritas a través de strings. Los valores del mismo se llenan a traves de la aplicación antes de ejecutar este algoritmo al igual que el anterior.

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





## Planos cortantes

El archivo con los datos de entrada para el algoritmo de planos cortantes debe encontrarse estar en /src/cutting_planes/model_cp.json.

Para ejecutar el script principal con manim, ejecutar en este caso:

<div>manim -p ./src/cutting_planes/gomory_cutting_planes.py Canvas</div>

al acabar, se reproducirá el video resultante de graficar el problema con sus restricciones, eje de coordenadas, cortes generados, y el punto óptimo así como sus coordenadas.

![Alt text](./imagenes utilizadas/cutting_planes_final_sc.png "Resultado final de planos cortantes")




## Búsqueda en la línea
De manera análoga para el algoritmo de búsqueda en la línea, se deberá hacer:

<div>manim -p ./src/line_search/line_search.py ThreeDCanvas</div>



Este otro método permite especificar parámetros para ajustar el ángulo de la cámara, pues en muchas escenas es probable que la cámara quede obstruida totalmente por la función graficada, en cuyo caso la imagen será un recuadro completo de color rojo. También se debe tener cuidado al especificar el rango de las **x** y de las **y** que se quiere representar. De no tenerse en consideración estos parámetros, es altamente probable que el video renderizado o no contenga la zona de interés para el problema, o se vea totalmente obstruida la cámara por la función a optimizar.





![Alt text](./imagenes utilizadas/line_search_init.png "Primeramente se plotea la función")

Comenzaremos graficando la función objetivo, y gradualmente se agregarán los ejes de coordenadas, así como los puntos secuencialmente en el mismo orden en que son computados por las iteraciones. Además, debido a que en muchas ocasiones las funciones y los puntos serán difíciles de observar correctamente, la cámara girará alrededor de la escena lentamente según todo esto ocurre.

![Alt text](./imagenes utilizadas/line_search_mid.png "")

![Alt text](./imagenes utilizadas/line_search_final.png "Resultado final de line_search")

En color rojo, el punto inicial, especificado en los datos de entrada en /src/line_search/model_ls.json

En color azul, los puntos intermedios obtenidos, y finalmente en verde(parcialmente obstruido por otro punto azul en esta escena), el punto óptimo computado para la función, dadas las restricciones especificadas.
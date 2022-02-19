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

Se deben especificar las variables a usar, así como las restricciones con signo <=, la función a optimizar debe estar escrita en términos que permitan minimizarla, es decir, se debe utilizar el opuesto de los coeficientes si se desea hallar el máximo. Además deben proveerse la matriz A, y vectores b,c, de manera tal que el problema sea expresado como $$\min{ca} ~~\text{tal que}~~ Ax \leq b$$.

Primeramente se cargan de entrada en el método **load_cp_model** del módulo **input_parser**, el cual recibe como parámetro la ubicación del archivo que contiene los datos, en este caso, por defecto se hará:

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



Primeramente se  procesarán los datos del problema especificados en el archivo de input, el cual por defecto será /src/line_search/model_ls.json. Se creará un objeto de tipo Surface para graficar la función principal con los valores de x_range y y_range dados. Además se colocará la cámara en el ángulo especificado, y se hará rotar a la misma con respecto a la escena, debido a que en ocasiones la complejidad de las funciones con las que se trabaja hará muy tedioso el proceso de ajustar la cámara a un ángulo específico para observar los puntos óptimos computados.

Para hallar el valor óptimo mediante la estrategia de búsqueda en la línea utilizamos como dirección de descenso siempre el opuesto al gradiente de la función evaluada en el punto inicial, llamémosle a este valor $D$. Luego utilizando la función scipy.line_search, calculamos el valor de $\alpha$ óptimo por el cual debemos multiplicar el opuesto del gradiente, y posteriormente nos movemos en esa dirección p*alpha unidades, de manera que si el punto del q partimos es $p_0$, avanzaríamos hasta $p_1=p_0+\alpha D$. Si el punto que obtenemos siguiendo esta idea cumple con todas las restricciones del problema, si no se detecta un descenso infinito, y si la diferencia entre el k-ésimo punto y el k+1-ésimo punto computado es mayor que cierta tolerancia, actualizamos el valor del gradiente que utilizaremos para la siguiente iteración, y seguimos el ciclo en la línea 78, en caso contrario, graficamos los puntos obtenidos luego de obtener sus coordenadas con respecto al eje de coordenadas de tres dimensiones que utilizamos como punto de referencia para la escena.
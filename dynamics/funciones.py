# dynamics/funciones.py

"""Proporciona un par de funciones útiles para la resolución de problemas dinámicos.

Este modulo permite al usuario resolver problemas dinámicos genéricos.
              
El módulo contiene las siguientes funciones:

- `dyn_generator(oper, state)` - Retorna el resultado de la conmutación [oper, state] multiplicada por la constante imaginaria -i.
- `rk4(func, oper, state, h)` -  Retorna el estado actualizado tras un calculo con el método Runge-Kutta de orden 4 (RK4) de la combinación de las cuatro pendientes ponderadas después de un paso de tamaño h.
"""
import numpy as np

def dyn_generator(oper, state):
    
    """Ejecuta la operación de conmutación entre dos operadores lineales y retorna el resultado multiplicado por la constante imaginaria -i.
    
    Ejemplo:
        >>> dyn_generator(np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]))
        
        [[0.-0.j, 0.+1.j],
        
        [0.-1.j, 0.-0.j]]
    
    Argumentos:
        **oper:** Un operador lineal representando la primer entrada en la operación de conmutación.
        
        **state:** Un operador lineal representando la segunda entrada en la operación de conmutación.
                
    Retorna:
        El resultado de la conmutación [oper, state] multiplicada por la constante imaginaria -i.
    """
    return (np.dot(oper, state) - np.dot(state, oper)) * -1.0j
    

def rk4(func, oper, state, h):
  
    """Implementa el método de Runge-Kutta de orden 4 (RK4), un método numérico para resolver ecuaciones
     diferenciales ordinarias (ODEs)
     
    Ejemplo:
        >>> rk4(dyn_generator, np.array([[0, 1], [1, 0]]), np.array([[1, 0], [0, 0]]), 0.001)
        
        [9.99998999e-01+0.j        0.00000000e+00+0.0010005j],
        
        [0.00000000e+00-0.0010005j 1.00099992e-06+0.j       ]
     
    Argumentos:
        **func:** Es una función que describe la evolución del sistema y toma dos argumentos: un operador (oper)
        y un estado (state). Esta función representa la derivada del estado con respecto al operador.
        
        **oper:** Representa algún operador del sistema, como podría ser un operador de evolución temporal o espacial,
        por ejemplo, en física cuántica, un Hamiltoniano.
        
        **state:** El estado actual del sistema, que puede ser un vector o una matriz, por ejemplo,
        en mecánica cuántica, puede ser un estado cuántico.
        
        **h:** El tamaño del paso. Controla cuánto se incrementa el valor del operador como por ejemplo, el paso
        en el tiempo si el operador está relacionado con la evolución temporal.
                
    Cálculo de las pendientes (k_1, k_2, k_3, k_4):
    
        k_1 es la primera evaluación de la función func, utilizando el operador y el
        estado actuales.
        
        k_2 se evalúa en el punto medio del paso (oper + h/2), usando el estado
        actualizado en base a la primera pendiente (state + h/2 * k_1).
        
        k_3 también se evalúa en el punto medio del paso, pero ahora usando la segunda
        pendiente k_2 para ajustar el estado.
        
        k_4 se evalúa en el extremo final del paso (oper + h), usando el estado modificado por
        la tercera pendiente k_3.
                
    Retorna:
        Retorna el estado actualizado tras un calculo con el método Runge-Kutta de orden 4 (RK4)
        de la combinación de las cuatro pendientes ponderadas después de un paso de tamaño h.
    """
    k_1 = func(oper, state)
    k_2 = dyn_generator(oper + h/2, state + h/2 * k_1)
    k_3 = dyn_generator(oper + h/2, state + h/2 * k_2)
    k_4 = dyn_generator(oper + h, state + h * k_3)

    return state + h/6 * (k_1 + 2 * k_2 + 2 * k_3 + k_4)

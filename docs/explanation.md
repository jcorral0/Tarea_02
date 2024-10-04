# Método Runge-Kutta de orden 4 (RK4)

Es un método numérico para resolver ecuaciones diferenciales ordinarias (ODEs), aproxima soluciones a ecuaciones diferenciales utilizando varios puntos intermedios dentro de un paso de integración. Es usado ampliamente en simulaciones de sistemas dinámicos. 

Provee una solución númerica al problema 

\begin{equation}
\frac{dy}{dt} = f(t, y),
\end{equation}
sujeta a la condición inicial
\begin{equation}
y(t_0) = y_0.
\end{equation}
El método consiste en escoger un timestep h > 0, tal que
\begin{equation}
y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4),
\end{equation}
donde
\begin{equation}
k_1 = f(t_n, y_n)
\end{equation}
\begin{equation}
k_2 = f(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_1)
\end{equation}
\begin{equation}
k_3 = f(t_n + \frac{h}{2}, y_n + \frac{h}{2}k_2)
\end{equation}
\begin{equation}
k_4 = f(t_n + h, y_n + hk_3) \\
\end{equation}

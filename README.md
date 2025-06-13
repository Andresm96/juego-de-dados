Resumen
Este documento describe el desarrollo de 'Tres o Más', un juego de dados interactivo diseñado en Python utilizando Tkinter como interfaz gráfica. El juego simula una competencia por turnos entre dos jugadores, con una mecánica de puntuación basada en las combinaciones obtenidas al lanzar 3 dados animados.

Introducción
El presente proyecto fue desarrollado como ejercicio de programación en Python, con el fin de integrar estructuras de control, funciones, listas, uso de librerías externas (Pillow) y elementos visuales mediante la interfaz Tkinter. El juego busca combinar lógica de juego, visualización gráfica e interacción usuario-programa.

Objetivos
- Implementar un juego de dados por turnos.
- Utilizar imágenes y animaciones para mejorar la experiencia visual.
- Aplicar principios básicos de desarrollo estructurado en Python.
Marco Teórico
Se hace uso de Python 3, específicamente de su módulo Tkinter para interfaces gráficas y Pillow para procesamiento de imágenes. Se modela el turno de cada jugador, se generan números aleatorios con la librería random y se presentan resultados visuales e históricos.
Metodología
La programación se realizó en Python. Las imágenes de dados fueron preparadas en formato PNG con nombres del tipo icono-_dado-1.png a icono-_dado-6.png. Se cargaron con Pillow y se actualizaron en pantalla a través de Labels de Tkinter. Se estructuraron funciones para lógica de juego, evaluación de puntos, control de turnos, animación, reinicio y visualización de resultados.
Resultados
El juego permite a dos jugadores lanzar dados alternadamente por 5 turnos cada uno. Se animan los dados antes de mostrar el resultado real. Se calcula automáticamente la puntuación por ronda y se presenta al ganador por pantalla con su puntaje.


Diagrama: https://miro.com/app/board/uXjVIqFlI_k=/?share_link_id=59048818519


Desarrollado por Andrés Felipe Murillo
Proyecto académico - 2025
PREICA2501B020077 - grupo 15

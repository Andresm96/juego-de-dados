import tkinter as tk
import random
#instalar Pillow si no está instalado: pip install Pillow en cmd para que sirvan las imágenes
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()

# cargar las imágenes de los dados
imagenes_dados = [ImageTk.PhotoImage(Image.open(f"icono-_dado-{i}.png").resize((70, 70))) for i in range(1, 7)]

# Variables globales
resultado_jugadores = {"jugador1": [], "jugador2": []}
jugador_actual = "jugador1"
puntajes = {"jugador1": 0, "jugador2": 0}
tiradas_por_jugador = {"jugador1": 0, "jugador2": 0}
nombre_jugador1 = ""
nombre_jugador2 = ""

# función que evalúa los dados lanzados y retorna los puntos correspondientes
def evaluar_tirada(d1, d2, d3):
    dados = [d1, d2, d3]
    repeticiones = max(dados.count(n) for n in dados)
    if repeticiones == 3:
        return 3
    elif repeticiones == 2:
        return 1
    else:
        return 0

# Función para determinar quién ganó y mostrar nombre + puntaje
def mostrar_ganador():
    if puntajes["jugador1"] > puntajes["jugador2"]:
        resultado = f"🎉 ¡Ganó {nombre_jugador1} con {puntajes['jugador1']} puntos!"
    elif puntajes["jugador2"] > puntajes["jugador1"]:
        resultado = f"🎉 ¡Ganó {nombre_jugador2} con {puntajes['jugador2']} puntos!"
    else:
        resultado = "🤝 ¡Empate!"
    
    label_turno.config(text=resultado)
    boton_reiniciar.pack(pady=10)

# Función para animar los dados antes de mostrar el resultado final
def animar_dados(pasos=10, delay=50):
    def girar(i=0):
        if i < pasos:
            label_dado1.config(image=random.choice(imagenes_dados))
            label_dado2.config(image=random.choice(imagenes_dados))
            label_dado3.config(image=random.choice(imagenes_dados))
            ventana.after(delay, lambda: girar(i + 1))
        else:
            lanzardados()  # al terminar la animación, lanza los dados reales

    girar()

# Función para lanzar los dados
def lanzardados():
    global jugador_actual

    # Verificar si ya terminaron las 5 tiradas por jugador
    if tiradas_por_jugador["jugador1"] >= 5 and tiradas_por_jugador["jugador2"] >= 5:
        mostrar_ganador()
        return

    # generar valores aleatorios para cada dado
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)

    label_lanzardados.config(text=f"resultado de los dados: {dado1}, {dado2}, {dado3}")

    # actualizar las imágenes reales al final de la animación
    label_dado1.config(image=imagenes_dados[dado1 - 1])
    label_dado2.config(image=imagenes_dados[dado2 - 1])
    label_dado3.config(image=imagenes_dados[dado3 - 1])

    # guardar los resultados de la tirada
    resultado_jugadores[jugador_actual].append((dado1, dado2, dado3))

    # calcular los puntos y actualizar puntaje
    puntos = evaluar_tirada(dado1, dado2, dado3)
    puntajes[jugador_actual] += puntos
    tiradas_por_jugador[jugador_actual] += 1

    # actualizar etiqueta de puntajes
    label_puntajes.config(text=f"Puntaje Jugador 1: {puntajes['jugador1']} | "
                               f"Puntaje Jugador 2: {puntajes['jugador2']}")

    # mostrar el historial de jugador 1
    label_resultado.config(text=f"resultados de Jugador 1:\n" + "\n".join(
        f"Tirada {i}: {d1}, {d2}, {d3}"
        for i, (d1, d2, d3) in enumerate(resultado_jugadores["jugador1"], 1)
    ))

    # mostrar el historial de jugador 2
    label_resultado2.config(text=f"resultados de Jugador 2:\n" + "\n".join(
        f"Tirada {i}: {d1}, {d2}, {d3}"
        for i, (d1, d2, d3) in enumerate(resultado_jugadores["jugador2"], 1)
    ))

    # cambiar turno al otro jugador
    cambiar_jugador()

# Función para alternar el jugador actual
def cambiar_jugador():
    global jugador_actual
    jugador_actual = "jugador2" if jugador_actual == "jugador1" else "jugador1"
    label_turno.config(text=f"Turno de: {jugador_actual}")

# Función para capturar nombres e iniciar saludo
def enviar():
    global nombre_jugador1, nombre_jugador2
    nombre_jugador1 = entrada_j1.get()
    nombre_jugador2 = entrada_j2.get()
    label_saludo.config(text=f"Hola {nombre_jugador1} y {nombre_jugador2}!")
    label_turno.config(text=f"Turno de: {jugador_actual}")
    boton_lanzar.config(state="normal")
    boton_enviar.config(state="disabled")

# Función para reiniciar el juego completamente
def reiniciar_juego():
    global resultado_jugadores, jugador_actual, puntajes, tiradas_por_jugador, nombre_jugador1, nombre_jugador2
    resultado_jugadores = {"jugador1": [], "jugador2": []}
    puntajes = {"jugador1": 0, "jugador2": 0}
    tiradas_por_jugador = {"jugador1": 0, "jugador2": 0}
    jugador_actual = "jugador1"
    nombre_jugador1 = ""
    nombre_jugador2 = ""
    
    label_turno.config(text=f"Turno de: {jugador_actual}")
    label_resultado.config(text="resultados de jugador actual:")
    label_resultado2.config(text="")
    label_lanzardados.config(text="resultado de los dados:")
    label_puntajes.config(text="Puntaje Jugador 1: 0 | Puntaje Jugador 2: 0")
    label_saludo.config(text="")
    label_dado1.config(image="")
    label_dado2.config(image="")
    label_dado3.config(image="")
    entrada_j1.delete(0, tk.END)
    entrada_j2.delete(0, tk.END)
    boton_reiniciar.pack_forget()
    boton_lanzar.config(state="disabled")
    boton_enviar.config(state="normal")

# Configuración visual
ventana.config(background="ivory")
ventana.title("Juego de dados Tres o Más")
ventana.geometry("1000x700")

# Label para el título
tk.Label(ventana, text="Ingresa nombre del jugador 1:").pack()
entrada_j1 = tk.Entry(ventana)
entrada_j1.pack()

tk.Label(ventana, text="Ingresa nombre del jugador 2:").pack()
entrada_j2 = tk.Entry(ventana)
entrada_j2.pack()

# Botón para enviar el nombre del jugador
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar)
boton_enviar.pack()

label_saludo = tk.Label(ventana, text="")
label_saludo.pack()

# Label para mostrar el turno actual
label_turno = tk.Label(ventana, text=f"Turno de: {jugador_actual}")
label_turno.pack()

# Label para mostrar el puntaje de cada jugador
label_puntajes = tk.Label(ventana, text="Puntaje Jugador 1: 0 | Puntaje Jugador 2: 0")
label_puntajes.pack()

# Label para mostrar el historial de resultados
label_resultado = tk.Label(ventana, text="resultados de jugador actual:")
label_resultado.pack()
label_resultado2 = tk.Label(ventana, text="")
label_resultado2.pack()

# Label para mostrar resultado textual de los dados
label_lanzardados = tk.Label(ventana, text="resultado de los dados:")
label_lanzardados.pack()

# Labels donde se mostrará la imagen de cada dado
label_dado1 = tk.Label(ventana)
label_dado1.pack()
label_dado2 = tk.Label(ventana)
label_dado2.pack()
label_dado3 = tk.Label(ventana)
label_dado3.pack()

# Botón para lanzar dados (ahora llama a la animación)
boton_lanzar = tk.Button(ventana, text="Lanzar dados", command=animar_dados, state="disabled")
boton_lanzar.pack()

# Botón para reiniciar el juego
boton_reiniciar = tk.Button(ventana, text="Volver a jugar", command=reiniciar_juego)

# Ejecutar la ventana
ventana.mainloop()

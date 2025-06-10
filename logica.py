import tkinter as tk
from PIL import Image, ImageTk
import random

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Juego de dados Tres o Más")
ventana.geometry("1000x700")
ventana.config(background="ivory")

# cargar las imágenes de los dados
imagenes_dados = [ImageTk.PhotoImage(Image.open(f"icono-_dado-{i}.png").resize((70, 70))) for i in range(1, 7)]

# Variables globales
resultado_jugadores = {"jugador1": [], "jugador2": []}
jugador_actual = "jugador1"
puntajes = {"jugador1": 0, "jugador2": 0}
tiradas_por_jugador = {"jugador1": 0, "jugador2": 0}
nombre_jugador1 = ""
nombre_jugador2 = ""

# Frames para diseño visual
frame_top = tk.Frame(ventana, bg="ivory")
frame_top.pack(pady=10)

frame_dados = tk.Frame(ventana, bg="ivory")
frame_dados.pack(pady=10)

frame_info = tk.Frame(ventana, bg="ivory")
frame_info.pack(pady=10)

frame_historial = tk.Frame(ventana, bg="ivory")
frame_historial.pack(pady=10)

# Funciones principales
def evaluar_tirada(d1, d2, d3):
    dados = [d1, d2, d3]
    repeticiones = max(dados.count(n) for n in dados)
    if repeticiones == 3:
        return 3
    elif repeticiones == 2:
        return 1
    else:
        return 0

def mostrar_ganador():
    if puntajes["jugador1"] > puntajes["jugador2"]:
        resultado = f"🎉 ¡Ganó {nombre_jugador1} con {puntajes['jugador1']} puntos!"
    elif puntajes["jugador2"] > puntajes["jugador1"]:
        resultado = f"🎉 ¡Ganó {nombre_jugador2} con {puntajes['jugador2']} puntos!"
    else:
        resultado = "🤝 ¡Empate!"
    label_turno.config(text=resultado)
    boton_reiniciar.pack(pady=10)

def animar_dados(pasos=10, delay=50):
    def girar(i=0):
        if i < pasos:
            label_dado1.config(image=random.choice(imagenes_dados))
            label_dado2.config(image=random.choice(imagenes_dados))
            label_dado3.config(image=random.choice(imagenes_dados))
            ventana.after(delay, lambda: girar(i + 1))
        else:
            lanzardados()
    girar()

def lanzardados():
    global jugador_actual
    if tiradas_por_jugador["jugador1"] >= 5 and tiradas_por_jugador["jugador2"] >= 5:
        mostrar_ganador()
        return

    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)

    label_lanzardados.config(text=f"Resultado: {dado1}, {dado2}, {dado3}")
    label_dado1.config(image=imagenes_dados[dado1 - 1])
    label_dado2.config(image=imagenes_dados[dado2 - 1])
    label_dado3.config(image=imagenes_dados[dado3 - 1])

    resultado_jugadores[jugador_actual].append((dado1, dado2, dado3))
    puntos = evaluar_tirada(dado1, dado2, dado3)
    puntajes[jugador_actual] += puntos
    tiradas_por_jugador[jugador_actual] += 1

    label_puntajes.config(text=f"Puntaje {nombre_jugador1}: {puntajes['jugador1']} | {nombre_jugador2}: {puntajes['jugador2']}")

    label_resultado1.config(text="\n".join(
        f"Tirada {i}: {d1}, {d2}, {d3}" for i, (d1, d2, d3) in enumerate(resultado_jugadores["jugador1"], 1)))
    label_resultado2.config(text="\n".join(
        f"Tirada {i}: {d1}, {d2}, {d3}" for i, (d1, d2, d3) in enumerate(resultado_jugadores["jugador2"], 1)))

    cambiar_jugador()

def cambiar_jugador():
    global jugador_actual
    jugador_actual = "jugador2" if jugador_actual == "jugador1" else "jugador1"
    label_turno.config(text=f"Turno de: {nombre_jugador1 if jugador_actual == 'jugador1' else nombre_jugador2}")

def enviar():
    global nombre_jugador1, nombre_jugador2
    nombre_jugador1 = entrada_j1.get()
    nombre_jugador2 = entrada_j2.get()
    label_saludo.config(text=f"Hola {nombre_jugador1} y {nombre_jugador2}!")
    label_turno.config(text=f"Turno de: {nombre_jugador1}")
    boton_lanzar.config(state="normal")
    boton_enviar.config(state="disabled")

def reiniciar_juego():
    global resultado_jugadores, jugador_actual, puntajes, tiradas_por_jugador, nombre_jugador1, nombre_jugador2
    resultado_jugadores = {"jugador1": [], "jugador2": []}
    puntajes = {"jugador1": 0, "jugador2": 0}
    tiradas_por_jugador = {"jugador1": 0, "jugador2": 0}
    jugador_actual = "jugador1"
    nombre_jugador1 = ""
    nombre_jugador2 = ""
    label_turno.config(text="Turno de: ")
    label_resultado1.config(text="")
    label_resultado2.config(text="")
    label_lanzardados.config(text="")
    label_puntajes.config(text="")
    label_saludo.config(text="")
    label_dado1.config(image="")
    label_dado2.config(image="")
    label_dado3.config(image="")
    entrada_j1.delete(0, tk.END)
    entrada_j2.delete(0, tk.END)
    boton_reiniciar.pack_forget()
    boton_lanzar.config(state="disabled")
    boton_enviar.config(state="normal")

# Sección superior: nombres y turno
tk.Label(frame_top, text="Nombre Jugador 1:").grid(row=0, column=0)
entrada_j1 = tk.Entry(frame_top)
entrada_j1.grid(row=0, column=1, padx=5)

tk.Label(frame_top, text="Nombre Jugador 2:").grid(row=1, column=0)
entrada_j2 = tk.Entry(frame_top)
entrada_j2.grid(row=1, column=1, padx=5)

boton_enviar = tk.Button(frame_top, text="Enviar", command=enviar)
boton_enviar.grid(row=2, column=0, columnspan=2, pady=5)

label_saludo = tk.Label(frame_top, text="", bg="ivory", font=("Helvetica", 12))
label_saludo.grid(row=3, column=0, columnspan=2)

label_turno = tk.Label(frame_top, text="", font=("Helvetica", 14, "bold"), bg="ivory")
label_turno.grid(row=4, column=0, columnspan=2, pady=5)

# Puntajes y botón de lanzar
label_puntajes = tk.Label(frame_info, text="", font=("Helvetica", 12), bg="ivory")
label_puntajes.pack()

label_lanzardados = tk.Label(frame_info, text="", bg="ivory")
label_lanzardados.pack()

boton_lanzar = tk.Button(frame_info, text="Lanzar Dados", command=animar_dados, state="disabled")
boton_lanzar.pack(pady=10)

boton_reiniciar = tk.Button(frame_info, text="Volver a Jugar", command=reiniciar_juego)

# Dados horizontales
label_dado1 = tk.Label(frame_dados, bg="ivory")
label_dado1.pack(side="left", padx=10)
label_dado2 = tk.Label(frame_dados, bg="ivory")
label_dado2.pack(side="left", padx=10)
label_dado3 = tk.Label(frame_dados, bg="ivory")
label_dado3.pack(side="left", padx=10)

# Historiales lado a lado
label_resultado1 = tk.Label(frame_historial, text="", justify="left", bg="ivory", font=("Courier", 10))
label_resultado1.pack(side="left", padx=40)

label_resultado2 = tk.Label(frame_historial, text="", justify="left", bg="ivory", font=("Courier", 10))
label_resultado2.pack(side="right", padx=40)

# Iniciar ventana
ventana.mainloop()

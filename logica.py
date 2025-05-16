import tkinter as tk
import random 
ventana = tk.Tk() 


resultado_jugadores = {"jugador1":[], "jugador2":[]}
jugador_actual = "jugador1"

def enviar():
    nombre = entrada.get()
    label_saludo.config(text=f"Hola, {nombre}!")
    


def lanzardados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    dado3 = random.randint(1, 6)
    
    label_lanzardados.config(text=f"resultado de los dados: {dado1}, {dado2}, {dado3}")
    
    resultado_jugadores[jugador_actual].append((dado1, dado2, dado3))
    
    label_resultado.config(text=f"resultados de {jugador_actual}:\n" + "\n"
    .join(f"Tirada {i}: {d1}, {d2}, {d3}"
         for i, (d1, d2, d3) in enumerate(resultado_jugadores[jugador_actual],1)))
        


#visual


ventana.config(background="ivory")
ventana.title("Juego de dados Tres o Mas")
ventana.geometry("1000x700")

#Label para el título

tk.Label(ventana, text="Ingresa nombre del jugardor 1:").pack()
entrada = tk.Entry(ventana)
entrada.pack()

#Botón para enviar el nombre del jugador

tk.Button(ventana, text="Enviar", command=enviar).pack()
label_saludo = tk.Label(ventana, text="")
label_saludo.pack()

#Botón para lanzar dados

tk.Button(ventana, text="Lanzar dados", command=lanzardados).pack()
label_lanzardados = tk.Label(ventana, text="resultado de los dados:")
label_lanzardados.pack()

#Label para mostrar la lista de los resultados
label_resultado = tk.Label(ventana, text="resultados de jugador actual:")
label_resultado.pack()


ventana.mainloop()


#determinar quien lanza los dados
#definir dados o resultados y definir el loop de lanzar dados (ejecutar evento con el boton)
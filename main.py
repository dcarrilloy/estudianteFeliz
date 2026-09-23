import tkinter as tk
import random


COLOR_FONDO = "#fff8ef"
COLOR_AZUL = "#174a7e"
COLOR_CORAL = "#f05d5e"
COLOR_AMARILLO = "#ffc857"
COLOR_VERDE = "#35a27f"
COLOR_MORADO = "#8067b7"


def dibujar_confeti():
	colores = [COLOR_CORAL, COLOR_AMARILLO, COLOR_VERDE, COLOR_MORADO]
	for _ in range(28):
		x = random.randint(20, 480)
		y = random.randint(8, 108)
		color = random.choice(colores)
		if random.choice([True, False]):
			canvas.create_oval(x, y, x + 8, y + 8, fill=color, outline="")
		else:
			canvas.create_rectangle(x, y, x + 7, y + 12, fill=color, outline="")


def felicitar():
	mensaje.config(
		text="¡Feliz Día del Estudiante!\n\nQue nunca les falten curiosidad, valentía y sueños por alcanzar. ✨"
	)
	boton.config(text="¡A celebrar! 🎉", bg=COLOR_CORAL, activebackground="#d94b4c")
	dibujar_confeti()
	ventana.after(2200, lambda: boton.config(text="¡Felicitar estudiantes! 🎓", bg="#2f80ed", activebackground="#1c64c4"))


def felicitar():
	mensaje.config(
		text="¡Feliz Día del Estudiante!\nSigan aprendiendo y cumpliendo sus sueños."
	)


ventana = tk.Tk()
ventana.title("Día del Estudiante")
ventana.geometry("500x430")
ventana.configure(bg=COLOR_FONDO)
ventana.resizable(False, False)

encabezado = tk.Frame(ventana, bg=COLOR_FONDO)
encabezado.pack(fill="x", pady=(20, 0))

titulo = tk.Label(
	encabezado,
	text="Día del Estudiante",
	font=("Arial", 24, "bold"),
	bg=COLOR_FONDO,
	fg=COLOR_AZUL,
)
titulo.pack()

subtitulo = tk.Label(
	encabezado,
	text="Una celebración para quienes aprenden, crean y se atreven",
	font=("Arial", 10, "italic"),
	bg=COLOR_FONDO,
	fg="#8a5a44",
)
subtitulo.pack(pady=(4, 0))

canvas = tk.Canvas(ventana, width=500, height=115, bg=COLOR_FONDO, highlightthickness=0)
canvas.pack()
dibujar_confeti()
canvas.create_oval(205, 23, 295, 113, fill=COLOR_AMARILLO, outline="")
canvas.create_text(250, 68, text="🎓", font=("Arial", 42))
canvas.create_text(135, 64, text="♥", fill=COLOR_CORAL, font=("Arial", 28, "bold"))
canvas.create_text(365, 64, text="★", fill=COLOR_VERDE, font=("Arial", 28, "bold"))

mensaje = tk.Label(
	ventana,
	text="Haz clic para recibir una felicitación",
	font=("Arial", 14),
	bg=COLOR_FONDO,
	fg="#333333",
	wraplength=430,
	justify="center",
)
mensaje.pack(pady=(8, 14))

boton = tk.Button(
	ventana,
	text="¡Felicitar estudiantes!",
	command=felicitar,
	font=("Arial", 13, "bold"),
	bg="#2f80ed",
	fg="white",
	activebackground="#1c64c4",
	activeforeground="white",
	padx=20,
	pady=10,
	cursor="hand2",
)
boton.pack(pady=10)

pie = tk.Label(
	ventana,
	text="Aprender también es una forma de celebrar. 💛",
	font=("Arial", 10),
	bg=COLOR_FONDO,
	fg="#8a5a44",
)
pie.pack(pady=(12, 0))

ventana.mainloop()

import tkinter as tk
import crud
from crud import login

formulario_inicio = tk.Tk()
formulario_inicio.geometry("500x500")
formulario_inicio.title("Iniciar Sesión")
formulario_inicio.resizable(False, False)

# ---------- FRAME IMAGEN ----------
frame_img = tk.Frame(formulario_inicio)
frame_img.pack(pady=20)

img = tk.PhotoImage(
    file=r"C:\Users\Admin\OneDrive\Desktop\sqlite-tkinter\image.png"
)

# Agrandar imagen
img = img.zoom(1, 1)

img_usuario = tk.Label(
    frame_img,
    image=img,
    bg=formulario_inicio["bg"],
    borderwidth=0
)
img_usuario.image = img
img_usuario.pack()

# ---------- FRAME FORMULARIO ----------
frame_form = tk.Frame(formulario_inicio)
frame_form.pack(pady=20)

tk.Label(
    frame_form,
    text="Nombre de usuario:",
    font=("Arial", 14)
).grid(row=0, column=0, padx=10, pady=15, sticky="e")

nombre = tk.Entry(frame_form, width=25)
nombre.grid(row=0, column=1, padx=10, pady=15)

tk.Label(
    frame_form,
    text="Contraseña:",
    font=("Arial", 14)
).grid(row=1, column=0, padx=10, pady=15, sticky="e")

contraseña = tk.Entry(frame_form, show="*", width=25)
contraseña.grid(row=1, column=1, padx=10, pady=15)



tk.Button(formulario_inicio, 
          text="Iniciar Sesión", 
          font=("Arial, 12"), 
          cursor="hand2", command=login(nombre.get(), contraseña.get())).pack()

formulario_inicio.mainloop()



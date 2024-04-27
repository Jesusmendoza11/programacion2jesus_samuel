import tkinter as tk
from time import strftime

def actualizar_hora():
    # Obtener la hora actual
    hora_actual = strftime('%H:%M:%S %p')
    # Actualizar la etiqueta de la hora con la hora actual
    etiqueta_hora.config(text=hora_actual)
    # Llamar a esta función nuevamente después de 1000 ms (1 segundo)
    ventana.after(1000, actualizar_hora)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("reloj digital")
ventana.geometry("350x200")  
# Tamaño de la ventana (ancho x alto)

# Crear etiqueta para mostrar la hora
etiqueta_hora = tk.Label(ventana, font=('algerian', 40, 'bold'), background='blue', foreground='black')
etiqueta_hora.pack(expand=True)  # Expande la etiqueta para llenar el espacio disponible
etiqueta_hora.config(anchor='center')  # Centra la etiqueta en la ventana

# Iniciar la actualización de la hora
actualizar_hora()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()

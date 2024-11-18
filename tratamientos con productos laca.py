import tkinter as tk
from tkinter import messagebox

# Función que proporciona los tratamientos según el tipo de piel
def obtener_informacion_tratamiento(tipo_piel):
    tratamientos = {
        "grasa": "Para la piel grasa, se recomienda usar limpiadores suaves, tónicos astringentes, y evitar cremas muy oleosas. También puedes usar productos que controlen el exceso de sebo.",
        "seca": "La piel seca necesita hidratación. Usa limpiadores suaves sin alcohol, cremas ricas en ceramidas, ácido hialurónico y aceites naturales.",
        "acneica": "Para piel acneica, se recomiendan productos con ácido salicílico, peróxido de benzoilo o retinoides. Evita productos comedogénicos.",
        "seborreica": "La piel seborreica requiere productos que controlen la producción de grasa y eviten la inflamación. Usa champús antimicóticos y geles limpiadores no agresivos.",
        "rosacea": "Para la rosácea, es fundamental usar productos calmantes, como cremas con niacinamida, y evitar la exposición al sol. No uses productos con alcohol o fragancias.",
        "melasma": "El tratamiento del melasma incluye el uso de protectores solares de amplio espectro y productos despigmentantes como hidroquinona o ácidos exfoliantes suaves.",
        "arrugas": "Para tratar las arrugas, se recomienda el uso de productos con retinoides, antioxidantes, y cremas con péptidos que estimulen la producción de colágeno.",
    }
    return tratamientos.get(tipo_piel.lower(), "Lo siento, no tengo información sobre este tipo de piel.")

# Función que procesa los datos del formulario y muestra los resultados
def procesar_formulario():
    edad = entry_edad.get()
    tipo_piel = entry_tipo_piel.get().lower()
    enfermedades_previas = entry_enfermedades.get().lower()
    color_piel = entry_color_piel.get().lower()
    tiene_acne = entry_acne.get().lower()

    tratamiento = obtener_informacion_tratamiento(tipo_piel)
    resultado = f"Recomendación de tratamiento:\n{tratamiento}"

    if enfermedades_previas == "sí":
        resultado += "\nEs importante consultar con un dermatólogo para un tratamiento más personalizado."
    
    if tiene_acne == "sí":
        resultado += "\nTe sugerimos revisar opciones de tratamientos para acné, como cremas con ácido salicílico o peróxido de benzoilo."

    messagebox.showinfo("Resultado del Tratamiento", resultado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Tratamientos Cutáneos")
ventana.geometry("400x400")

# Agregar el ícono (aquí se asume que el archivo "icono.ico" está en el mismo directorio que el script)
ventana.iconbitmap("icono.ico")  # Reemplaza con la ruta correcta del ícono

# Etiquetas y campos de entrada para los datos del usuario
label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()

entry_edad = tk.Entry(ventana)
entry_edad.pack()

label_tipo_piel = tk.Label(ventana, text="Tipo de piel (grasa, seca, acneica, etc.):")
label_tipo_piel.pack()

entry_tipo_piel = tk.Entry(ventana)
entry_tipo_piel.pack()

label_enfermedades = tk.Label(ventana, text="¿Enfermedades cutáneas previas? (Sí/No):")
label_enfermedades.pack()

entry_enfermedades = tk.Entry(ventana)
entry_enfermedades.pack()

label_color_piel = tk.Label(ventana, text="Color de piel (claro, medio, oscuro):")
label_color_piel.pack()

entry_color_piel = tk.Entry(ventana)
entry_color_piel.pack()

label_acne = tk.Label(ventana, text="¿Tienes acné? (Sí/No):")
label_acne.pack()

entry_acne = tk.Entry(ventana)
entry_acne.pack()

# Botón para procesar la información
boton_procesar = tk.Button(ventana, text="Obtener Tratamiento", command=procesar_formulario)
boton_procesar.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
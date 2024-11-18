import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout

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

# Definir la clase principal de la app Kivy
class SkinCareApp(App):
    def build(self):
        # Crear la estructura del layout
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Título
        self.title_label = Label(text="Consulta de Tratamientos Cutáneos", font_size=24, size_hint=(1, None), height=50)
        self.layout.add_widget(self.title_label)

        # Entrada de edad
        self.label_edad = Label(text="Edad:")
        self.entry_edad = TextInput(multiline=False)
        self.layout.add_widget(self.label_edad)
        self.layout.add_widget(self.entry_edad)

        # Entrada de tipo de piel
        self.label_tipo_piel = Label(text="Tipo de piel (grasa, seca, acneica, etc.):")
        self.entry_tipo_piel = TextInput(multiline=False)
        self.layout.add_widget(self.label_tipo_piel)
        self.layout.add_widget(self.entry_tipo_piel)

        # Entrada de enfermedades previas
        self.label_enfermedades = Label(text="¿Enfermedades cutáneas previas? (Sí/No):")
        self.entry_enfermedades = TextInput(multiline=False)
        self.layout.add_widget(self.label_enfermedades)
        self.layout.add_widget(self.entry_enfermedades)

        # Entrada de color de piel
        self.label_color_piel = Label(text="Color de piel (claro, medio, oscuro):")
        self.entry_color_piel = TextInput(multiline=False)
        self.layout.add_widget(self.label_color_piel)
        self.layout.add_widget(self.entry_color_piel)

        # Entrada de acné
        self.label_acne = Label(text="¿Tienes acné? (Sí/No):")
        self.entry_acne = TextInput(multiline=False)
        self.layout.add_widget(self.label_acne)
        self.layout.add_widget(self.entry_acne)

        # Botón para procesar
        self.boton_procesar = Button(text="Obtener Tratamiento", size_hint=(1, None), height=50)
        self.boton_procesar.bind(on_press=self.procesar_formulario)
        self.layout.add_widget(self.boton_procesar)

        return self.layout

    def procesar_formulario(self, instance):
        edad = self.entry_edad.text
        tipo_piel = self.entry_tipo_piel.text.lower()
        enfermedades_previas = self.entry_enfermedades.text.lower()
        color_piel = self.entry_color_piel.text.lower()
        tiene_acne = self.entry_acne.text.lower()

        tratamiento = obtener_informacion_tratamiento(tipo_piel)
        resultado = f"Recomendación de tratamiento:\n{tratamiento}"

        if enfermedades_previas == "sí":
            resultado += "\nEs importante consultar con un dermatólogo para un tratamiento más personalizado."
        
        if tiene_acne == "sí":
            resultado += "\nTe sugerimos revisar opciones de tratamientos para acné, como cremas con ácido salicílico o peróxido de benzoilo."

        # Mostrar resultado en una ventana emergente
        popup = Popup(title="Resultado del Tratamiento",
                      content=Label(text=resultado),
                      size_hint=(None, None), size=(400, 400))
        popup.open()

# Ejecutar la app
if __name__ == "__main__":
    SkinCareApp().run()

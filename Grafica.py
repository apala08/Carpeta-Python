import tkinter as tk
import plotly.graph_objects as go

# Calculadora de IMC
def imc_calculator(weight, height):
    return weight / (height**2)

# Función para mostrar el gráfico
def show_graph():
    try:
        entry_weight = float(input_weight.get())
        entry_height = float(input_height.get())
        imc = imc_calculator(entry_weight, entry_height)

        # Crear el gráfico de indicador
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=imc,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Índice de Masa Corporal (IMC)"},
            gauge={
                'axis': {'range': [0, 40]},
                'steps': [
                    {'range': [0, 18.5], 'color': "lightblue"},  # Bajo Peso
                    {'range': [18.5, 24.9], 'color': "lightgreen"},  # Peso Normal
                    {'range': [25, 29.9], 'color': "yellow"},  # Sobrepeso
                    {'range': [30, 40], 'color': 'pink'},  # Obesidad
                ],
                'bar': {'color': "darkblue"}  # Color de Barra
            }
        ))

        # Mostrar el gráfico
        fig.show()
    except ValueError:
        labelResults.config(text="Ingrese únicamente valores numéricos")

# Interfaz de la Calculadora
def imc_calculator_interface():
    try:
        entry_weight = float(input_weight.get())
        entry_height = float(input_height.get())
        imc = imc_calculator(entry_weight, entry_height)
        labelResults.config(text=f"Tu Índice de Masa Corporal es {imc:.2f}")
    except ValueError:
        labelResults.config(text="Ingrese únicamente valores numéricos")

# Interfaz de Usuario
window = tk.Tk()
window.title("Calculadora de IMC con Medidor")
window.geometry("800x600")

# Peso del Usuario
label_weight = tk.Label(
    window,
    text="Ingrese su Peso en Kilogramos",
    font=("Inter", 16, "bold"),
    fg="dim gray",
    bg="gray70"
)
label_weight.pack()

input_weight = tk.Entry(window)
input_weight.pack()

# Estatura del Usuario
label_height = tk.Label(
    window,
    text="Ingrese su Estatura en Metros",
    font=("Inter", 16, "bold"),
    fg="dim gray",
    bg="gray70"
)
label_height.pack()

input_height = tk.Entry(window)
input_height.pack()

# Botones
calculate_button = tk.Button(
    window, text="Calcular mi Índice de Masa Corporal (IMC)",
    command=imc_calculator_interface
)
calculate_button.pack()

show_graphic_button = tk.Button(
    window, text="Mostrar los Resultados",
    command=show_graph
)
show_graphic_button.pack()

# Resultados
labelResults = tk.Label(
    window,
    text="",
    font=("Inter", 16, "bold"),
    fg="lightgray",
    bg="gray70"
)
labelResults.pack()

# Ejecutar la interfaz gráfica
window.mainloop()
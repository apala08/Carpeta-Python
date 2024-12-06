import tkinter as tk
import plotly.graph_objects as go
import math as math

#Calculadora de IMC
def imc_calculator(weight, height):
    imc = weight / (height**2)
    return round(imc)

#Interfaz de la Calculadora
def imc_calculator_interface():
    try:
        entry_weight = float(input_weight.get())
        entry_height = float(input_height.get())
        imc = imc_calculator(entry_weight, entry_height)
        show_figure(imc, get_imc_text(imc)) 
        labelResults.config(text="Tu Indice de Masa Corporal es " + str(imc))
    except ValueError:
        labelResults.config(text="Ingrese únicamente valores númericos")

def get_imc_text(imc):
    if imc <= 18.5:
        return"Usted se encuentra en un estado de Bajo de Peso. Realiza más ejercicio."
    elif 18.5<= imc <= 24.9:
        return"Usted se encuentra en un estado Normal de Peso. Su IMC es de una persona en un rango sano."
    elif 25<= imc <=  29.9:
        return"Usted se encuentra en un estado de Sobre Peso. Consulte con una nutricionista para conocer más."
    elif 30 <= imc <= 40:
        return"Usted se encuentra en un estado de Obesidad. Consulte inmediatamente con un experto."
    
def show_figure(imc, annotations_text):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = imc,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Índice de Masa Corporal (IMC)"},
    gauge={
        'axis' : {'range':[0,40]},
        'steps': [
            {'range': [0,18.5],'color': "lightblue" }, #Bajo Peso
            {'range': [18.5,24.9], 'color': "lightgreen"}, #Peso Normal
            {'range': [25,29.9], 'color':"yellow"}, #Sobrepeso
            {'range': [30,40],'color':'pink'},#Obesidad 
        ],
        'bar': {'color':"darkblue"} #Color de Barra 
    }
    ))
    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=1,
                              xanchor='center', yanchor='top',
                              text= annotations_text,
                              font=dict(family='Inter',
                                        size=16,
                                        color='rgb(150,150,150)'),
                              showarrow=False))
    fig.update_layout(annotations=annotations)
    fig.show()


#Interfaz
window = tk.Tk()
window.title("Calculadora de IMC con Medidor")
window.geometry("800x400")
window['bg'] = 'gray100'

#Header del Programa
label_header = tk.Label (window,
                        text="Para calcular su índice de masa corporal, ingrese su estatura y peso.", width=120,
                        font=("Inter", 16, "bold"),
                        fg = "white",
                        bg = "steelblue",
                        pady=15
)

label_header.pack()

#Peso del Usuario
label_weight= tk.Label (window, 
                    text="Ingrese su Peso en Kilogramos:",
                    font=("Inter", 16, "bold"),
                    fg="gray10",
                    bg="white",
                    justify="center",
                    pady=10,
)

label_weight.pack()
input_weight= tk.Entry(window,
                    background="gray90",
                    foreground="gray10" 
)
input_weight.pack()

#Estatura del Usuario
label_height = tk.Label (window, 
                          text="Ingrese su Estatura en Metros:",
                          font=("Inter", 16,"bold"),
                          fg="gray10",
                          bg="white",
                          justify="center",
)

label_height.pack()

input_height= tk.Entry(window,
                       background="gray90",
                       foreground="gray10" 

)
input_height.pack()

#Botton

#Calcular el Promedio de IMC

calculate_botton = tk.Button(window, 
                             text="Mostrar los Resultados", 
                             command= imc_calculator_interface,
                             bg= "steelblue",
                             font=("Inter",12, "bold"),
                             fg="white",
                             relief= "raised",
                             state="active",
                             padx=60

)

calculate_botton.pack()

#Results

labelResults = tk.Label(window,
                        text="",
                        font=("Inter", 24, "bold"),
                        fg="steelblue",
                        bg="white"
)

labelResults.pack()


window.mainloop()
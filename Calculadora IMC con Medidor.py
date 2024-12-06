#  Programa de Calculadora de IMC con Medidor

#Calculadora de IMC
def imc_calculator(weight, height):
    imc = weight / (height**2)
    return imc
print(imc_calculator(85,1.85))
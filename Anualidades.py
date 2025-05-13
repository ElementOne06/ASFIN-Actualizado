from Temas.Interes_Compuesto import *
from math import log10
'''
CÁLCULO DE ANUALIDADES:
- Anualidad anticipada: pagos al inicio del periodo.
- Anualidad vencida: pagos al final del periodo.
- Anualidad perpetua: pagos indefinidos en el tiempo (con/sin capitalizción entre periodos).
'''

# Funcion de referencias para el tipo de anualidades y variables
def opcion_de_anualidad(anualidad):
    switch = {
        1: "Anualidad vencida",
        2: "Anualidad anticipada",
        3: "Anualidad perpetua",
        0: "Salir"
    }

    return switch.get(anualidad, "Opción no válida")

def Anualidad(): 
    "Selección del tipo de anualidad"
    print('''Por favor, seleccione el tipo de anualidad (1,2,3)
        1. Vencida
        2. Anticipada
        3. Perpetua 
        0. Salir''')
    opcion_anualidad = int(input("Escribir el número de la opción deseada: "))
    tipo = opcion_de_anualidad(opcion_anualidad)
    
    return tipo

def opcion_de_variable(variable):
    switch = {
        'A': "Valor de los pagos",
        'I': "Tasa de interés",
        'N': "Número de periodos",
        'VP': "Valor presente",
        'VF': "Valor futuro",
    }

    return switch.get(variable, "Opción no válida")

def Variable():
    "Selección de la variable a calcular"
    print('''Por favor, seleccione la variable a calcular (A,i,n,VP,VF,k)
        A = Valor de los pagos
        i = Tasa de interés (perpetuidades)
        n = Número de periodos
        VP = Valor presente
        VF = Valor futuro''')
    opcion_variable = input("Escribir la(s) letra(s) de la opción deseada: ").upper().strip()
    tipo_variable = opcion_de_variable(opcion_variable)
    
    return tipo_variable

def presente_futuro(pf):
    switch = {
        'VP': "Valor presente",
        'VF': "Valor futuro",
    }

    return switch.get(pf, "Opción no válida")

def valor_presente_futuro():
    "Selección de la variable a calcular"
    print('''Por favor, seleccione la variable con la que se cuenta (VP,VF)
        VP = Valor presente
        VF = Valor futuro ''')
    opcion_vpf = input("Escribir la letra de la opción deseada: ").upper().strip()
    tipo_vpf = presente_futuro(opcion_vpf)
    
    return tipo_vpf
    
# Funciones para pedir los valores
def pagos():
    A = float(input("Ingrese el valor de los pagos: "))
    return A
def tasa_interes():
    i = input("Introduzca la tasa de interés (indica si es diaria, semanal, mensual, bimestral, trimestral, cuatrimestral, semestral o anual): "
    "Ejemplo: 15% anual compuesto mensual \n")
    return (i)
def plazo():
    n = input("Introduzca el plazo (indica si es en: días, semanas, quincenas, meses, bimestres, trimestres, cuatrimestres, semestres, años o décadas): "
    "Ejemplo: 5 meses \n")
    cap = input("Porfavor si puedes introducir el tipo de capitalizacion que es la tasa:(anual, semestral, cuatrimestral, trimestral, bimestral, mensual, quincenal, diaria) \n")
    return (n,cap)
def valor_presente():
    VP = float(input("Ingrese el valor presente: "))
    return VP
def valor_futuro():
    VF = float(input("Ingrese el valor futuro: "))
    return VF

# Funciones para eficientar a la hora de pedir los valores
# Para anualidades anticipadas y vencidas
def VP_o_VF():
    A = pagos()
    i = conversor_tasa_c(tasa_interes())
    n = conversor_nplazos(plazo())
    return (A, i, n)

def A_VP():
    i = conversor_tasa_c(tasa_interes())
    n = conversor_nplazos(plazo())
    VP = valor_presente()
    return (i, n, VP)

def A_VF():
    i = conversor_tasa_c(tasa_interes())
    n = conversor_nplazos(plazo())
    VF = valor_futuro()
    return (i, n, VF)

def n_VP():
    A = pagos()
    i = conversor_tasa_c(tasa_interes())
    VP = valor_presente()
    return (A, i, VP)

def n_VF():
    A = pagos()
    i = conversor_tasa_c(tasa_interes())
    VF = valor_futuro()
    return (A, i, VF)

# Para anualidades perpetuas
def A_VP_perpetua():
    VP = valor_presente()
    i = conversor_tasa_c(tasa_interes())
    return (VP, i)

def i_VP_perpetua():
    A = pagos()
    VP = valor_presente()
    return (A, VP)

def VP_perpetua():
    A = pagos()
    i = conversor_tasa_c(tasa_interes())
    return (A, i)

# Funciones de cálculos de valores
# Anualidades  vencidas
def calculo_vf_av(A, i, n):
    VF = A * (((1 + i) ** n) - 1 ) / i
    return VF

def calculo_vp_av(A, i, n):
    VP = A * (1 - (1 + i) ** -n) / i
    return VP

def caculo_A_av_vp(i, n, VP):
    A = VP * i / (1 - (1 + i) ** -n)
    return A

def calculo_A_av_vf(i, n, VF):
    A = VF * i / (((1 + i) ** n) - 1)
    return A

def calculo_n_av_vf(A, i, VF):
    n = log10(VF * i / A + 1) / log10(1 + i)
    return n

def calculo_n_av_vp(A, i, VP):
    n = -log10(1 - (VP * i / A)) / log10(1 + i)
    return n

# Anualidades Anticipadas
def calculo_vf_aa(A, i, n):
    VF = (A * (((1 + i) ** n) - 1 ) / i) * (1 + i)
    return VF

def calculo_vp_aa(A, i, n):
    VP = (A * (1 - (1 + i) ** -n) / i) * (1 + i)
    return VP

def calculo_A_aa_vp(i, n, VP):
    A = VP * i / ((1 - (1 + i) ** -n) * (1 + i))
    return A

def calculo_A_aa_vf(i, n, VF):
    A = VF * i / ((((1 + i) ** n) - 1) * (1 + i))
    return A

def calculo_n_aa_vf(A, i, VF):
    n = log10((VF * i) / (A * (1 + i)) + 1) / log10(1 + i)
    return n

def calculo_n_aa_vp(A, i, VP):
    n = -log10(1 - ((VP * i) / (A * (1 + i)))) / log10(1 + i)
    return n

# Anualidades Perpetuas
def calculo_VP_ap(A, i):
    VP = A / i
    return VP

def calculo_i_ap(A, VP):
    i = A / VP
    return i

def calculo_A_ap(VP, i):
    A = VP * i
    return A

# Funcion para ver qué tipo de anualidad se queriere
def Anualidades():
    while True:
        print("Bienvenido al calculador de anualidades, para salir escoger la opcion 0")
        tipo_anualidad = Anualidad()
        if tipo_anualidad == "Anualidad vencida":
            print("Anualidad vencida")
            tipo_variable = Variable()
            if tipo_variable == "Valor de los pagos":
                tipo_valor = valor_presente_futuro()
                if tipo_valor == "Valor presente":
                    i, n, VP = A_VP()
                    A = caculo_A_av_vp(i, n, VP)
                    print(f"El valor de los pagos es de: {round(A, 2)}")
                elif tipo_valor == "Valor futuro":
                    i, n, VF = A_VF()
                    A = calculo_A_av_vf(i, n, VF)
                    print(f"El valor de los pagos es de: {round(A, 2)}")
            elif tipo_variable == "Número de periodos":
                if valor_presente_futuro() == "Valor presente":
                    A, i, VP = n_VP()
                    n = calculo_n_av_vp(A, i, VP)
                    print(f"El número de periodos es de: {round(n, 2)}")
                elif valor_presente_futuro() == "Valor futuro":
                    A, i, VF = n_VF()
                    n = calculo_n_av_vf(A, i, VF)
                    print(f"El número de periodos es de: {round(n, 2)}")
            elif tipo_variable == "Valor presente":
                A, i , n = VP_o_VF()
                VP = calculo_vp_av(A, i, n)
                print(f"El valor presente es de: {round(VP, 2)}")
            elif tipo_variable == "Valor futuro":
                A, i , n = VP_o_VF()
                VF = calculo_vf_av(A, i, n)
                print(f"El valor futuro es de: {round(VF, 2)}")
            else:
                print("Opción no válida")  
                continue     
        elif tipo_anualidad == "Anualidad anticipada":
            print("Anualidad anticipada")
            tipo_variable = Variable()
            if tipo_variable == "Valor de los pagos":
                tipo_valor = valor_presente_futuro()
                if tipo_valor == "Valor presente":
                    i, n, VP = A_VP()
                    A = calculo_A_aa_vp(i, n, VP)
                    print(f"El valor de los pagos es de: {round(A, 2)}")
                elif tipo_valor == "Valor futuro":
                    i, n, VF = A_VF()
                    A = calculo_A_aa_vf(i, n, VF)
                    print(f"El valor de los pagos es de: {round(A, 2)}")
            elif tipo_variable == "Número de periodos":
                if valor_presente_futuro() == "Valor presente":
                    A, i, VP = n_VP()
                    n = calculo_n_aa_vp(A, i, VP)
                    print(f"El número de periodos es de: {round(n, 2)}")
                elif valor_presente_futuro() == "Valor futuro":
                    A, i, VF = n_VF()
                    n = calculo_n_aa_vf(A, i, VF)
                    print(f"El número de periodos es de: {round(n, 2)}")
            elif tipo_variable == "Valor presente":
                A, i, n = VP_o_VF()
                VP = calculo_vp_aa(A, i, n)
                print(f"El valor presente es de: {round(VP, 2)}")
            elif tipo_variable == "Valor futuro":
                A, i, n = VP_o_VF()
                VF = calculo_vf_aa(A, i, n)
                print(f"El valor futuro es de: {round(VF, 2)}")
            else:
                print("Opción no válida")
                continue
        elif tipo_anualidad == "Anualidad perpetua":
            print("Anualidad perpetua")
            tipo_variable = Variable()
            if tipo_variable == "Valor de los pagos":
                VP, i = A_VP_perpetua()
                A = calculo_A_ap(VP, i)
                print(f"El valor de los pagos es de: {round(A, 2)}")
            elif tipo_variable == "Tasa de interés":
                A, VP = i_VP_perpetua()
                i = calculo_i_ap(A, VP)
                print(f"La tasa de interés es de: {round(i, 6)}%")
            elif tipo_variable == "Valor presente":
                A, i = VP_perpetua()
                VP = calculo_VP_ap(A, i)
                print(f"El valor presente es de: {round(VP, 2)}")
            else:
                print("Opción no válida")
                continue
        elif tipo_anualidad == "Salir":
            print("Gracias por usar el programa.")
            break
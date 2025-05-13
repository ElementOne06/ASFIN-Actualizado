from Temas.Interes_Compuesto import guardar_en_analisis
#Función que imprime el significado de los valores del interés simple
def datos_Isimple ():
    print("""
    Bienvenido estás son las variables del Interés Simple:
    I = Intereses, redito o interés simple 
    i = tasa de intereses 
    C = Capital o valor presente 
    n o t = tiempo transcurrido o plazo 
    M = Monto o valor futuro
    """ )

#Funciones para hacer los procedimientos con las fórmulas
def Is_intereses (C,i,n):
    I = C * i * n
    return (I) 

def Is_capital (i,M,n):
    C = M / ( 1 + (i * n) )
    return (C)

def Is_monto_si (C,I):
    M = C + I
    return (M)

def Is_monto_no (C,i,n):
    M = C * ( 1 + ( i * n) )
    return(M)

def Is_tasa_anual (M,C,n):
    i = ( ( ( M / C ) -1 ) / n )
    return(i)

def Is_nmeses (M,C,i):
    n = ( ( ( M / C ) -1 ) / i )
    return(n)

#Función que dice el programa a teminado solo esta hecha para reducir espacio de código
def salir ():
    print("¡Hasta luego! El programa ha terminado. ")

#Función para reducir espacio que te indica que pusiste una opcion no valida y si quieres salir del programa solo escriba salir
def repite ():
    print("""Opción no valida favor de repetir.
           - Y en el caso de que no quiera continuar porfavor escriba salir """)
    
#Función para reducir espacio que solo te pide que ingreses si o no
def respuesta_no_valida ():
    print("Respuesta no válida. Por favor, ingrese Si o No. ")

#Función para reducir espacio que solo imprime que introduce números válidos
def Nvalidos ():
    print("¡¡Error!!: Porfavor Introduce números válidos. ")

#Función para mostrar el Resultado
def Mostrar_Resultado(Valor_pedido,Resultado):
    print(f"\n >>> {Valor_pedido}: {Resultado}\n ")

#Funciones para convertir a meses los valores
def conversor_n (plazo):
    try:
        tiempo = float(plazo[0])
        formato = (plazo[1]).lower()

        if formato in ["dias","dia","día"]:
            n = tiempo / 30.44
        elif formato in ["semana", "semanas"]:
            n = tiempo / 4.3
        elif formato in ["quincena", "quincenas"]:
            n = tiempo * 0.5
        elif formato in ["mes", "meses"]:
            n = tiempo
        elif formato == ["bimestre", "bimestres"]:
            n = tiempo * 2
        elif formato in ["trimestre", "trimestres"]:
            n = tiempo * 3
        elif formato in ["cuatrimestre", "cuatrimestres"]:
            n = tiempo * 4
        elif formato == ["semestres", "semestre"]:
            n = tiempo * 6
        elif formato == ["años","año"]:
            n = tiempo * 12
        elif formato in ["decada","década","décadas","decadas"]:
            n = tiempo
        else:
            n = tiempo
        return (n)
    except (IndexError,ValueError):
        return(float(plazo[0]))

def conversor_i (tasa_interés):
    try:
        tiempo = float(tasa_interés[0].rstrip("%")) / 100
        formato = (tasa_interés[1]).lower()

        if formato in ["diaria", "diaría"]:
            i = tiempo * 30
        elif formato in ["mensual"]:
            i = tiempo 
        elif formato in ["bimestral"]:
            i = tiempo / 2
        elif formato in ["trimestral"]:
            i = tiempo / 3
        elif formato in ["semestral"]:
            i = tiempo / 6
        elif formato in ["anual"]:
            i = tiempo / 12
        else: 
            i = tiempo
        return(i)
    except (IndexError,ValueError):
        return float(tasa_interés[0])
#Funciones para pedir los valores
def Capital ():
    C = float(input("Introduce el Capital: \n"))
    return(C)

def tasa_interés():
    tasa_interés = (input("Introduce la tasa de interés(indica si es diaria, semanal, mensual, bimestral, trimestral, cuatrimestral, semestral o anual): "
    "Ejemplo 12% mensual \n")).split(" ")
    return(tasa_interés)

def Monto ():
    M = float(input("Introduce el Monto: \n"))
    return(M)

def plazo ():
    plazo = input("Introduce el plazo (indica si es en: días, semanas, quincenas, meses, bimestres, trimestres, cuatrimestres, semestres, años o décadas): \n").split(" ") 
    return(plazo)

def Intereses ():
    I = float(input("Introduce los intereses: \n"))
    return(I)

#Funciones para eficientar a la hora de pedir los valores
def IntereS_I ():
    C = Capital ()
    i = conversor_i(tasa_interés())
    n = conversor_n(plazo())
    return(C,i,n)

def IntereS_C():
    i = conversor_i(tasa_interés())
    M = Monto ()
    n = conversor_n(plazo())
    return(i,M,n)

def Interes_MS():
    C = Capital ()
    I = Intereses ()
    return(C,I)

def Interes_MN():
    C = Capital ()
    i = conversor_i(tasa_interés())
    n = conversor_n(plazo())
    return(C,i,n)

def IntereS_i():
    M = Monto ()
    C = Capital ()
    n = conversor_n(plazo())
    return(M,C,n)

def IntereS_n():
    M = Monto ()
    C = Capital ()
    i = conversor_i(tasa_interés())
    return(M,C,i)

#Función Principal de Interés Simple
def Interes_Simple():
    datos_Isimple ()
    #Lo que desea calcular
    while True:
        opcion = input("Bienvenido al Interés Simple, ¿Qué deseas calcular? ( I , C, i, n, M )// Si quiere terminar el programa solo escriba salir \n").strip()
        Valor_pedido = ""
        Resultado = None
        #Opción si pide los Intereses
        if opcion == "I" :
            try:
                C, i, n = IntereS_I()
                Valor_pedido = "Los Intereses son de"
                Resultado = Is_intereses (C,i,n)
                resultado_data = {"Capital": C, "Tasa de Interés": i, "Tiempo": n, "Intereses": Resultado}
                columna_resaltar = "Intereses"
                guardar_en_analisis("Simple", resultado_data, columna_resaltar)
            except ValueError: 
                Nvalidos()
                continue

        #Opción si pide el Capital
        elif opcion.upper() == "C" :
            try:
                i, M, n = IntereS_C()
                Valor_pedido = "El capital es de"
                Resultado = Is_capital(i,M,n)
                resultado_data = {"Capital": Resultado, "Tasa de Interés": i, "Tiempo": n, "Monto": M}
                columna_resaltar = "Capital"
                guardar_en_analisis("Simple", resultado_data, columna_resaltar)
            except ValueError:
                Nvalidos()
                continue

        #Opción si pide el Monto
        elif opcion.upper() == "M":
            while True:
                intereses = input("¿Usted cuenta con el valor de los Intereses (I)? ").strip().lower()
                Valor_pedido = "El Monto es de"
                if intereses == "si":
                    try: 
                        C,I = Interes_MS()
                        Resultado = Is_monto_si(C,I)
                        resultado_data = {"Capital": C, "Intereses": I, "Monto": Resultado}
                        columna_resaltar = "Monto"
                        guardar_en_analisis("Simple", resultado_data, columna_resaltar)
                        break
                    except ValueError:
                        Nvalidos()
                        continue
                elif intereses == "no":
                    try:
                        C,i,n = Interes_MN()
                        Resultado = Is_monto_no(C,i,n)
                        resultado_data = {"Capital": C, "Tasa de Interés": i, "Tiempo": n, "Monto": Resultado}
                        columna_resaltar = "Monto"
                        guardar_en_analisis("Simple", resultado_data, columna_resaltar)
                        break
                    except ValueError:
                        Nvalidos()
                        continue
                else: 
                    respuesta_no_valida ()
                    continue 
                
        #Opción si pide la tasa de interés anual
        elif opcion == "i":
            try: 
                M,C,n = IntereS_i()
                Valor_pedido = "La tasa de interés anual es de"
                Resultado = Is_tasa_anual(M,C,n)
                resultado_data = {"Capital": C, "Monto": M, "Tiempo": n, "Tasa de Interés": Resultado}
                columna_resaltar = "Tasa de Interés"
                guardar_en_analisis("Simple", resultado_data,columna_resaltar)
            except ValueError:
                Nvalidos()
                continue

        #Opción si pide el plazo de tiempo en meses
        elif opcion.lower() == "n": 
            try:
                M,C,i = IntereS_n()
                Valor_pedido = "El tiempo del plazo fue de"
                Resultado = (f"{Is_nmeses (M,C,i)} meses")
                resultado_data = {"Capital": C, "Monto": M, "Tasa de Interés": n, "Tiempo": Resultado}
                columna_resaltar = "Tiempo"
                guardar_en_analisis("Simple", resultado_data, columna_resaltar)
            except ValueError:
                Nvalidos()
                continue

        #Opción si pide salirse del programa
        elif opcion.lower() == "salir":
            salir () 
            break

        #Opción si no pone ninguna de estas opciones
        else:
            repite()
            continue
        if Resultado is not None:
            Mostrar_Resultado(Valor_pedido,Resultado)
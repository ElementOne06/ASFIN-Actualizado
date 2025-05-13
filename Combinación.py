from Temas.Interes_Simple import Interes_Simple,repite
from Temas.Interes_Compuesto import Interes_Compuesto
from Temas.Anualidades import Anualidades
def Opciones_Intereses():
    while True:
            # Nombre = input ("Introduzca su nombre para el registro: ")
            Tipo_de_interes = input("¿Cuál es la opción que deseas calcular? (simple, compuesto, anualidad o tasa de amortización)" 
                                    "Si quiere terminar el programa escriba >>salir<< \n").lower().strip()

            if Tipo_de_interes == "simple":
                try:
                    Interes_Simple()
                    
                except (IndexError,ValueError):
                    repite()
                    continue
            elif Tipo_de_interes == "compuesto":
                try:
                    Interes_Compuesto()
                    
                except (IndexError,ValueError):
                    repite()
                    continue
            elif Tipo_de_interes == "anualidad":
                try:
                    Anualidades()
                    
                except (IndexError,ValueError):
                    repite()
                    continue
            elif Tipo_de_interes == "salir":
                break
            else:
                repite()
                continue
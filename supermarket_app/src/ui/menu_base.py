import os, time
from supermarket_app.src.utils.utilidades import Utilidades
class MenuBase:
    def __init__(self):
        pass
    
    def limpiar_consola(self):
        """
        Limpia la consola
        """
        util = Utilidades()
        util.limpiar_consola()
        
    def pausa(self, seg=2):
        """
        Pausa la ejecución del programa durante el tiempo indicado
        """
        time.sleep(seg)
        
    def mostrar_encabezado(self, titulo, cantidad_elementos, simbolo="=", es_salto_de_linea=False):
        """
        Muestra un encabezado con el título y el simbolo indicando el nivel de indentación
        """
        if es_salto_de_linea:
            print()
        print(simbolo * cantidad_elementos)
        print(f"\t{titulo}")
        print(simbolo * cantidad_elementos)
        
    def pedir_opcion(self, opciones=None):
        """
        Pide una opción al usuario y valida que sea correcta
        """
        opcion = input("Seleccione una opción: ")
        
        if opciones:
            numeros_opcion_validados = [str(i+1) for i in range(len(opciones))]
            
            if opcion not in numeros_opcion_validados:
                return "Opción no válida"
        return opcion
    
    def continuar(self):
        """
        Muestra un mensaje de continuación y espera a que el usuario pulse ENTER
        """
        input("\nPulsa ENTER para continuar...")
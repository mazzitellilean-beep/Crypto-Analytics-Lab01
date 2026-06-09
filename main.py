import funciones
from tabla_original import tabla_original
    
tabla_activos = tabla_original()

opcion = funciones.menu()

while opcion != 8: 
    funciones.verificacion_menu(opcion, tabla_activos)
    opcion = funciones.menu()

print("Gracias por utilizar el sistema de gestion. Finalizando programa...")

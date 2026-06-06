from mostrar_menu import menu
from generacion_tabla import generacion_tabla
    
tabla_activos = generacion_tabla()

opcion = menu()

while opcion != 8: 
    from validacion_opcion import verificacion_menu
    verificacion_menu(opcion, tabla_activos)
    opcion = menu()

print("Gracias por utilizar el sistema de gestion. Finalizando programa...")

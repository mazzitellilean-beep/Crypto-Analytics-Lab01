from matriz_inicial import generacion_tabla
from Menu import mostrar_menu, menu_principal

def main():
    tabla = generacion_tabla()
    menu_principal(tabla)

main()
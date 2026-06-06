def mostrar(tabla):
    print("\n" + "=" * 100)
    print(f"{'NOMBRE':<25} {'TICKER':<8} {'VALOR USD':>12} {'VOLUMEN':>18} {'METODOLOGÍA':>15} {'UNIDADES':>10} {'PUNTAJE':>8}")
    print("=" * 100)
    for activo in tabla:
        print(f"{activo[0]:<25} {activo[1]:<8} {activo[2]:>12.2f} {activo[3]:>18,} {activo[4]:>15} {activo[5]:>10,} {activo[6]:>8}")
    print("=" * 100)
    salida = input("\nPresione Enter para volver al menú principal...")




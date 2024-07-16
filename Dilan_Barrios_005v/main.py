from funciones import *
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
while True:
    print("""1). Asignar sueldos aleatorios
2). Clasificar sueldos
3). Ver estadísticas.
4). Reporte de sueldos
5). Salir del programa
""")
    op = int(input("Ingrese una opcion: "))
    if op == 1:
        asignar_sueldos_a()
    elif op == 2:
        calificar_sueldos()
    elif op == 3:
        estadisticas_sueldos()
    elif op == 4:
        reporte_de_sueldos()
    elif op == 5:
        print("""Finalizando programa...
Creado por Dilan Barrios
RUT 21.704.342-5""")
        break

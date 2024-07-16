import random
import csv
import math

trabajadores = [
    "Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", 
    "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", 
    "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"
]
sueldos = {}
def asignar_sueldos_a():
    global sueldos
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("Sueldos asignados exitosamente.")
def calificar_sueldos():
    sueldo_menor = []
    sueldo_medio = []
    sueldo_mayor = []
    for trabajador, sueldo in sueldos.items():
        if sueldo < 800000:
            sueldo_menor.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            sueldo_medio.append((trabajador, sueldo))
        else:
            sueldo_mayor.append((trabajador, sueldo))
    print("\nSueldos menores a $800,000")
    print("TOTAL:", len(sueldo_menor))
    for trabajador, sueldo in sueldo_menor:
        print(f"{trabajador} ${sueldo}")
    print("\nSueldos entre $800,000 y $2,000,000")
    print("TOTAL:", len(sueldo_medio))
    for trabajador, sueldo in sueldo_medio:
        print(f"{trabajador} ${sueldo}")
    print("\nSueldos superiores a $2,000,000")
    print("TOTAL:", len(sueldo_mayor))
    for trabajador, sueldo in sueldo_mayor:
        print(f"{trabajador} ${sueldo}")
    print(f"\nTOTAL SUELDOS: $", sum(sueldo for _, sueldo in sueldos.items()))
    print("")
def estadisticas_sueldos():
    sueldos_lista = list(sueldos.values())
    if sueldos_lista:
        sueldo_mas_alto = max(sueldos_lista)
        sueldo_mas_bajo = min(sueldos_lista)
        promedio_sueldos = sum(sueldos_lista) / len(sueldos_lista)
        producto_sueldos = math.prod(sueldos_lista)
        media_geometrica = producto_sueldos ** (1 / len(sueldos_lista))
        print(f"\nSueldo mas alto: ${sueldo_mas_alto}")
        print(f"Sueldo mas bajo: ${sueldo_mas_bajo}")
        print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
        print(f"Media geometrica: ${media_geometrica:.2f}\n")
    else:
        print("Aun no se ha asignado ningun sueldo.")
def reporte_de_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo_base in sueldos.items():
            desc_salud = sueldo_base * 0.07
            desc_afp = sueldo_base * 0.12
            sueldo_liquido = sueldo_base - desc_salud - desc_afp
            writer.writerow([trabajador, sueldo_base, desc_salud, desc_afp, sueldo_liquido])
    print("Reporte de sueldos exportado a 'reporte_sueldos.csv'.")
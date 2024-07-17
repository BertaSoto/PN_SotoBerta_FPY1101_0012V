import random

trabajadores = ["Juan Pérez”, ”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel 
Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldo_bruto = []

def asignar_sueldos(trabajadores):
    print("Sueldos asignados correctamente.")
    for trabajador in trabajadores:
        trabajador['sueldo'] = random.randint(0, 2500001)
        


def main()

while True:
    
    print("Menú:")
    print("1. Asignar sueldos.")
    print("2. Clasificar sueldos.")
    print("3. Estadisticas.")
    print("4. Reporte de sueldos.")
    print("5. Salir")
    
    opcion = input("Elija opción:")
    
    if opcion == 1:
        asignar_sueldos()
    elif opcion == 2:
        clasificar_sueldos()
    elif opcion == 3:
        ver_estadisticas()
    elif opcion == 4:
        reporte_sueldos()
    elif opcion == 5:
        print("Finalizando programa… Desarrollado por Berta Soto RUT 16.712.297-3")
        break
    else:
        print("Opción no válida, intentar nuevamente:")
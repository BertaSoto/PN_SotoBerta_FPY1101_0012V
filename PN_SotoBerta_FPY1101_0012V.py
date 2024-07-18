import random
import statistics
import csv

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldo_bruto = {}

def asignar_sueldos():
    global sueldo_bruto
    sueldo_bruto = {trabajador: random.randint(0, 2500001) for trabajador in trabajadores}
    print("Sueldos asignados correctamente.")

        
def clasificar_sueldos():
    if sueldo_bruto:
        print("\nSueldos menores a $800.000:")
        for trabajador, sueldo in sueldo_bruto.items():
            if sueldo < 800000:
                print(f"{trabajador}: {sueldo}")

        print("\nSueldos entre $800.000 y $2.000.000:")
        for trabajador, sueldo in sueldo_bruto.items():
            if 800000 <= sueldo < 2000000:
                print(f"{trabajador}: {sueldo}")

        print("\nSueldos superiores a $2.000.000:")
        for trabajador, sueldo in sueldo_bruto.items():
            if sueldo >= 2000000:
                print(f"{trabajador}: {sueldo}")
                  
def ver_estadisticas():
    if sueldo_bruto:
        sueldo = list(sueldo_bruto.values())
        max_sueldo = max(sueldo)
        min_sueldo = min(sueldo)
        promedio = sum(sueldo) / len(sueldo)
        media_geometrica = statistics.geometric_mean(sueldo)
        
        print(f"\nEl sueldo mas alto es: {max_sueldo}")
        print(f"El sueldo mas bajo es: {min_sueldo}")
        print(f"El promedio de los sueldos es: {promedio:.1f}")
        print(f"La media geometrica es: {media_geometrica:.2f}")
        
def reporte_sueldos():
    if sueldo_bruto:
        with open('reporte_sueldos.csv', 'w') as file:
            file.write(f"{'Trabajador':<20} {'Sueldo Bruto':<15} {'Descuento Salud':<15} {'Descuento AFP':<15} {'Sueldo Líquido':<15}\n")
            file.write("="*80 + "\n")
            for trabajador, sueldo in sueldo_bruto.items():
                descuento_salud = sueldo * 0.07
                descuento_afp = sueldo * 0.12
                sueldo_liquido = sueldo - descuento_salud - descuento_afp
                file.write(f"{trabajador:<20} {sueldo:<15,.2f} {descuento_salud:<15,.2f} {descuento_afp:<15,.2f} {sueldo_liquido:<15,.2f}\n")
        print("\nReporte de sueldos generado correctamente.") 
    
    
        
def main():
    while True:
        print("\nMenú:")
        print("1. Asignar sueldos.")
        print("2. Clasificar sueldos.")
        print("3. Estadísticas.")
        print("4. Reporte de sueldos.")
        print("5. Salir")

        opcion = input("Elija opción: ")

        if opcion == '1':
            asignar_sueldos()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            print("\nFinalizando programa… \nDesarrollado por Berta Soto \nRUT 16.712.297-3")
            break
        else:
            print("Opción no válida, intentar nuevamente:")
            
            
if __name__ == "__main__":  
    main()
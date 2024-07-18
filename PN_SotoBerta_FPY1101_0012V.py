import random
import statistics

trabajadores = ["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]
sueldo_bruto = {}

def asignar_sueldos():
    global sueldo_bruto
    sueldo_bruto = {trabajador: random.randint(0, 2500001) for trabajador in trabajadores}
    print("Sueldos asignados correctamente.")
        
def clasificar_sueldos():
    if sueldo_bruto:
        
        print("Sueldos menores a $800.000:")
        for trabajador, sueldo in sueldo_bruto.items():
            if sueldo < 800000:
                print(f"{trabajador}: {sueldo}")
                
        print("Sueldos entre $800.000 y $2.000.000")
        for trabajador in trabajadores:
            if 800000 > sueldo < 2000000:
                  print(f"{trabajador}: {sueldo}")
                
        print("Sueldos superiores a $2.000.000:")
        for trabajador in trabajadores:
            if sueldo >= 2000000:
                  print(f"{trabajador}: {sueldo}")
                  
def ver_estadisticas():
    if sueldo_bruto:
        sueldo = list(sueldo_bruto.values())
        max_sueldo = max(sueldo)
        min_sueldo = min(sueldo)
        promedio = sum(sueldo) / len(sueldo)
        media_geometrica = statistics.geometric_mean(sueldo)
        
        print(f"El sueldo mas alto es: {max_sueldo}")
        print(f"El sueldo mas bajo es: {min_sueldo}")
        print(f"El promedio de los sueldos es: {promedio:.1f}")
        print(f"La media geometrica es: {media_geometrica:.2f}")
        
def reporte_sueldos
        
def main():

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
            
            
if __name__ == "__main__":  
    main()
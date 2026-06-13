"TAREA 3: Programacion Tradicional"

def registrar_mascota():
    print("\n--- INGRESA LOS DATOS DE LA MASCOTA ---")
    print() 
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota en anios: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    mascota = {
        "nombre": nombre,
        "especie": especie,
        "edad": edad
    }

    return mascota

"FUNCIONES"
def mostrar_mascota(mascota):
    print("\n--- LA INFORMACION DE LA MASCOTA ES ---")
    print()
    print(f"Nombre  : {mascota['nombre']}")
    print(f"Especie : {mascota['especie']}")
    print(f"Edad    : {mascota['edad']} años")
    print("-" * 30+ "\n") # REALIZA 30 GUIONES PARA SEPARAR LA INFORMACION DE LA MASCOTA DE OTRA INFORMACION QUE SE PUEDA MOSTRAR DESPUES Y SALTA DE LINEA


def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)

"FUNCION DE EJECUCION MAIN"
if __name__ == "__main__":
    main()

# main.py

from mascota import Mascota

print("\n=== SISTEMA DE GESTIÓN DE MASCOTAS ===")

# LISTA para guardar objetos
mascotas = []
especies_permitidas = ["perro", "gato", "ave", "pez"]

# CREACIÓN DE LA PRIMERA MASCOTA

print("\nREGISTRO DE LA MASCOTA #1")

nombre1 = input("Nombre: ")

while True: # CONTROL DE VALIDACIÓN PARA LA ESPECIE
    especie1 = input("Especie (perro, gato, ave, pez): ").lower()
    if especie1 in especies_permitidas:
        break
    print("❌ Error: Solo se permiten perro, gato, ave o pez.")

while True:  # CONTROL DE VALIDACIÓN PARA LA EDAD
    try:
        edad1 = int(input("Edad: "))
        if edad1 < 0:
            print("❌ Edad no negativa")
            continue
        break
    except ValueError:
        print("❌ Número inválido")

mascota1 = Mascota(nombre1, especie1, edad1)
mascotas.append(mascota1)

# CREACIÓN DE LA SEGUNDA MASCOTA

print("\nREGISTRO DE LA MASCOTA #2")

nombre2 = input("Nombre: ")

while True: # CONTROL DE VALIDACIÓN PARA LA ESPECIE
    especie2 = input("Especie (perro, gato, ave, pez): ").lower()
    if especie2 in especies_permitidas:
        break
    print("❌ Error: Solo se permiten perro, gato, ave o pez.")

while True:  # CONTROL DE VALIDACIÓN PARA LA EDAD
    try:
        edad2 = int(input("Edad: "))
        if edad2 < 0:
            print("❌ Edad no negativa")
            continue
        break
    except ValueError:
        print("❌ Número inválido")

mascota2 = Mascota(nombre2, especie2, edad2)
mascotas.append(mascota2)


print("\n=== INFORMACION QUE REGISTRASTE ===")

mascota1.mostrar_informacion()
mascota1.hacer_sonido()
print()

mascota2.mostrar_informacion()
mascota2.hacer_sonido()

print(f"\nTotal de mascotas registradas: {len(mascotas)} \n")


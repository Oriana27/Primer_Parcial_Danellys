# Número de historia clínica (un número entero).
# • Nombre del paciente (una cadena de texto).
# • Edad del paciente (un número entero).
# • Diagnóstico (una cadena de texto).
# • Cantidad de días de internación (un número entero).

pacientes = []

# 2. Cargar pacientes:
# • Permitir al usuario ingresar los datos de los pacientes, almacenando la
# información en una lista anidada (arreglo bidimensional), como se muestra en
# la imagen de arriba. La cantidad de pacientes a ingresar debe ser determinada
# por el usuario.


def cargar_pacientes():
    cant_pacientes = (
        int(input("Ingrese cantidad de pacientes que desea cargar: ")))
    for i in range(cant_pacientes):
        numero_historia_clínica = int(
            input("Número de historia clinica: "))
        nombre_paciente = input("Nombre del paciente: ")
        edad_paciente = int(input("Edad del paciente: "))
        diagnostico = input("Diagnostico: ")
        cantidad_dias_internacion = int(
            input("Cantidad de dias de internación: "))

        datos = [numero_historia_clínica, nombre_paciente,
                 edad_paciente, diagnostico, cantidad_dias_internacion]
        pacientes.append(datos)

        if i < cant_pacientes - 1:
            continuar = input(
                "¿Desea continuar cargando pacientes? (si/no): ").lower()
            if continuar != 'si':
                break

    return pacientes


#  3. Mostrar la lista de pacientes:
# • Imprimir en pantalla todos los datos de los pacientes almacenados en el
# arreglo bidimensional, mostrando cada fila como un paciente.


def mostrar_lista_pacientes(pacientes: list) -> list:
    print("\nMostrando lista de pacientes")
    if not pacientes:
        print("No hay pacientes cargados.")
        return

    for paciente in pacientes:
        print(paciente)


# 4. Búsqueda de pacientes:
# • Implementar una función que, dado el número de historia clínica de un
# paciente, busque en la lista y muestre todos los datos de dicho paciente (o un
# mensaje indicando que no se encontró al paciente).


def buscar_paciente(busqueda_paciente: str) -> str:
    print("\nBuscando paciente")
    busqueda_paciente = int(
        input("Ingrese Número de hitoria clinica que desea encontrar: "))
    for i in range(len(pacientes)):
        if pacientes[i][0] == busqueda_paciente:
            return f"Paciente encontrado: historia clinica: {pacientes[i][0]}, Nombre: {pacientes[i][1]}, Edad: {pacientes[i][2]}, Diagnostico: {pacientes[i][3]}, Dias de internación: {pacientes[i][4]}"
    return f"El Paciente {busqueda_paciente} no fue encontrado en el inventario"


# 5. Ordenamiento de pacientes:
# • Implementar una función que permita ordenar la lista de pacientes por el
# número de Historia Clínica en forma ascendente. Se podrá utilizar cualquier
# algoritmo de ordenamiento.


def ordenar_pacientes(pacientes: list) -> list:
    print("\n Lista de pacientes Ordenada por número de Historia Clinica")
    n = len(pacientes)
    for i in range(n-1):
        for j in range(n - 1 - i):
            if pacientes[j][0] > pacientes[j+1][0]:
                guardado = pacientes[j]
                pacientes[j] = pacientes[j+1]
                pacientes[j+1] = guardado
    return pacientes


# 6. Determinar el paciente con mayor cantidad de días de internación:
# • Implementar una función que calcule e imprima el paciente con más días de
# internación, mostrando sus datos completos

def mas_dias(pacientes: list) -> list:
    mas_dias_inter = pacientes[0]
    for i in range(len(pacientes)):
        if pacientes[i][4] > mas_dias_inter[4]:
            mas_dias_inter = pacientes[i]
    return f"El paceinte con más dias de internación es Nombre: {mas_dias_inter[1]}, Historia Clinica: {mas_dias_inter[0]}, Edad: {mas_dias_inter[2]}, Diagnostico: {mas_dias_inter[3]}, Cantidad dias Internación: {mas_dias_inter[4]}"


# 7. Determinar el paciente con menor cantidad de días de internación:
# • Implementar una función que calcule e imprima el paciente con menos días de
# internación, mostrando sus datos completos.


def menos_dias(pacientes: list) -> list:
    menos_dias_inter = pacientes[0]
    for i in range(len(pacientes)):
        if pacientes[i][4] < menos_dias_inter[4]:
            menos_dias_inter = pacientes[i]
    return f"El paceinte con menos dias de internación es Nombre: {menos_dias_inter[1]}, Historia Clinica: {menos_dias_inter[0]}, Edad: {menos_dias_inter[2]}, Diagnostico: {menos_dias_inter[3]}, Cantidad dias Internación: {menos_dias_inter[4]}"

# 8. Cantidad de pacientes con días de internación mayor a 5 días.
# • Implementar una función que recorra la lista de pacientes y cuente cuántos
# pacientes tienen más de 5 días de internación.


def calcular_cant_mayor(pacientes: list) -> list:
    dias = 5
    mayor = 0
    for i in range(len(pacientes)):
        if pacientes[i][4] > dias:
            mayor += 1
    return f"La cantidad de pacientes con mas de 5 días de internación es {mayor}"

# 9. Promedio de días de internación de todos los pacientes.
# • Implementar una función que calcule el promedio de días de internación de
# todos los pacientes registrados


def promediar_dias(pacientes: list) -> list:
    suma_dias = 0
    cant_pacientes = len(pacientes)
    if cant_pacientes == 0:
        return f"No hay pacientes cargados"
    for i in range(cant_pacientes):
        suma_dias += pacientes[i][4]
    promedio_dias = suma_dias / cant_pacientes
    return f"El promedio de dias es {promedio_dias}"


def ingresar_menu():

    while True:

        print("""Menú:
1. Cargar pacientes
2. Mostrar lista de pacientes
3. Búsqueda de pacientes
4. Ordenar Pacientes por numero de historia clinica
5. Determinar el paciente con menor cantidad de días de internación
6. Determinar el paciente con mayor cantidad de días de internación
7. Cantidad de pacientes con días de internación mayor a 5 días
8. Promedio de días de internación de todos los pacientes
9. Salir del sistema
""")

        menu = int(input("Ingrese opcion deseada (1, 2, 3, 4, 5, 6, 7, 8, 9): "))

        if menu == 1:
            pacientes = cargar_pacientes()
            print(pacientes)
        elif menu == 2:
            lista = mostrar_lista_pacientes(pacientes)
            print(lista)
        elif menu == 3:
            busqueda = buscar_paciente(buscar_paciente)
            print(busqueda)
        elif menu == 4:
            ordenar = ordenar_pacientes(pacientes)
            print(ordenar)
        elif menu == 5:
            menor = menos_dias(pacientes)
            print(menor)
        elif menu == 6:
            mayor_d = mas_dias(pacientes)
            print(mayor_d)
        elif menu == 7:
            calculo = calcular_cant_mayor(pacientes)
            print(calculo)
        elif menu == 8:
            promedio = promediar_dias(pacientes)
            print(promedio)
        elif menu == 9:
            print("Saliendo del sistema. Gracias")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


ingresar_menu()

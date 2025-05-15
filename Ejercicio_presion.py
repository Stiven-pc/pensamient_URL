# Definición de datos
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
niveles_azucar = []
niveles_sal = []
presion_sistolica = []

# Variables para promedios
total_azucar = 0
total_sal = 0
total_presion = 0

# Evaluación diaria
for i in range(len(dias)):
    print(f"\n--- Día: {dias[i]} ---")
    
    # Nivel de azúcar
    azucar = float(input(f"Ingrese el nivel de azúcar (mg/dL) para {dias[i]}: "))
    niveles_azucar.append(azucar)
    print(f"Nivel de azúcar: {azucar} mg/dL")
    if 70 <= azucar <= 140:
        print("Estado: Normal")
    else:
        print("Alerta: Nivel de azúcar fuera de rango")

    # Consumo de sal
    sal = float(input(f"Ingrese el consumo de sal (mg) para {dias[i]}: "))
    niveles_sal.append(sal)
    print(f"Consumo de sal: {sal} mg")
    if sal <= 2300:
        print("Estado: Normal")
    else:
        print("Alerta: Consumo de sal elevado")

    # Presión arterial
    presion = float(input(f"Ingrese la presión sistólica (mmHg) para {dias[i]}: "))
    presion_sistolica.append(presion)
    print(f"Presión sistólica: {presion} mmHg")
    if presion < 120:
        print("Clasificación de presión: Normal")
    elif 120 <= presion <= 129:
        print("Clasificación de presión: Elevada")
    elif 130 <= presion <= 139:
        print("Clasificación de presión: Hipertensión Etapa 1")
    else:
        print("Clasificación de presión: Hipertensión Etapa 2")

    # Acumular para promedios
    total_azucar += azucar
    total_sal += sal
    total_presion += presion

# Cálculo de promedios
promedio_azucar = total_azucar / len(dias)
promedio_sal = total_sal / len(dias)
promedio_presion = total_presion / len(dias)

# Mostrar promedios semanales
print("\n--- Promedios Semanales ---")
print(f"Promedio de azúcar: {promedio_azucar:.2f} mg/dL")
print(f"Promedio de sal: {promedio_sal:.2f} mg")
print(f"Promedio de presión sistólica: {promedio_presion:.2f} mmHg")

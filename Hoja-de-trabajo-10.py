class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad} años, Peso: {self.peso} kg")

    def generar_ficha(self):
        print(" Ficha Médica")
        self.mostrar_datos()


class Perro(Animal):
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    def calcular_dosis(self):
        return self.peso * 0.5

    def generar_ficha(self):
        super().generar_ficha()
        print(f"Raza: {self.raza}")
        print(f"Dosis recomendada: {self.calcular_dosis()} mg\n")


class Gato(Animal):
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    def calcular_dosis(self):
        return self.peso * 0.3

    def generar_ficha(self):
        super().generar_ficha()
        print(f"Color: {self.color}")
        print(f"Dosis recomendada: {self.calcular_dosis()} mg\n")


class Ave(Animal):
    def __init__(self, nombre, edad, peso, especie):
        super().__init__(nombre, edad, peso)
        self.especie = especie

    def calcular_dosis(self):
        return self.peso * 0.1

    def generar_ficha(self):
        super().generar_ficha()
        print(f"Especie: {self.especie}")
        print(f"Dosis recomendada: {self.calcular_dosis()} mg\n")


class Reptil(Animal):
    def __init__(self, nombre, edad, peso, habitat):
        super().__init__(nombre, edad, peso)
        self.habitat = habitat

    def calcular_dosis(self):
        return self.peso * 0.4

    def generar_ficha(self):
        super().generar_ficha()
        print(f"Hábitat: {self.habitat}")
        print(f"Dosis recomendada: {self.calcular_dosis()} mg\n")


class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera):
        super().__init__(nombre, edad, dni)
        self.carrera = carrera

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Carrera: {self.carrera}\n")


class Profesor(Persona):
    def __init__(self, nombre, edad, dni, materia):
        super().__init__(nombre, edad, dni)
        self.materia = materia

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Materia que imparte: {self.materia}\n")


class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, departamento):
        super().__init__(nombre, edad, dni)
        self.departamento = departamento

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Departamento: {self.departamento}\n")


def menu_veterinaria():
    print("\n Clínica Veterinaria")
    print("1. Registrar Perro")
    print("2. Registrar Gato")
    print("3. Registrar Ave")
    print("4. Registrar Reptil")
    opcion = input("Elige una opción: ")

    nombre = input("Nombre del animal: ")
    edad = int(input("Edad del animal (años): "))
    peso = float(input("Peso del animal (kg): "))

    if opcion == "1":
        raza = input("Raza: ")
        animal = Perro(nombre, edad, peso, raza)
    elif opcion == "2":
        color = input("Color: ")
        animal = Gato(nombre, edad, peso, color)
    elif opcion == "3":
        especie = input("Especie: ")
        animal = Ave(nombre, edad, peso, especie)
    elif opcion == "4":
        habitat = input("Hábitat: ")
        animal = Reptil(nombre, edad, peso, habitat)
    else:
        print("Opción no válida")
        return

    animal.generar_ficha()


def menu_personas():
    print("\nSistema de Personas")
    print("1. Registrar Estudiante")
    print("2. Registrar Profesor")
    print("3. Registrar Administrativo")
    opcion = input("Elige una opción: ")

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    dni = input("DNI: ")

    if opcion == "1":
        carrera = input("Carrera: ")
        persona = Estudiante(nombre, edad, dni, carrera)
    elif opcion == "2":
        materia = input("Materia que imparte: ")
        persona = Profesor(nombre, edad, dni, materia)
    elif opcion == "3":
        departamento = input("Departamento: ")
        persona = Administrativo(nombre, edad, dni, departamento)
    else:
        print("Opción no válida")
        return

    persona.mostrar_info()


def menu_principal():
    while True:
        print("\nMenú Principal ")
        print("1. Clínica Veterinaria")
        print("2. Sistema de Personas")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_veterinaria()
        elif opcion == "2":
            menu_personas()
        elif opcion == "3":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

menu_principal()

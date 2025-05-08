print("Ejercicio #1")
from abc import ABC, abstractmethod
import math

class ExperimentoFisico(ABC):
    @abstractmethod
    def realizar_experimento(self):
        pass

class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad=9.81):
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if gravedad == 0:
            raise ValueError("La gravedad no puede ser cero.")
        self.altura = altura
        self.gravedad = gravedad

    def realizar_experimento(self):
        tiempo = math.sqrt(2 * self.altura / self.gravedad)
        return tiempo

def simulacion_caida_libre():
    try:
        altura = float(input("Ingrese la altura desde la que cae el objeto (en metros): "))
        gravedad = float(input("Ingrese el valor de la gravedad (en m/s², por defecto 9.81): ") or 9.81)

        experimento = CaidaLibre(altura, gravedad)
        tiempo = experimento.realizar_experimento()
        print(f"\n El tiempo de caída es de {tiempo:.2f} segundos.")
    except ValueError as e:
        print(" Error:", e)

simulacion_caida_libre()



print("Ejercicio #2")

from abc import ABC, abstractmethod
import math

class OperacionCientifica(ABC):
    @abstractmethod
    def calcular(self):
        pass

class RaizCuadrada(OperacionCientifica):
    def __init__(self, numero):
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        self.numero = numero

    def calcular(self):
        return math.sqrt(self.numero)

class Potencia(OperacionCientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        return math.pow(self.base, self.exponente)

class Logaritmo(OperacionCientifica):
    def __init__(self, numero, base=math.e):
        if numero <= 0:
            raise ValueError("El logaritmo solo se puede calcular de números positivos.")
        self.numero = numero
        self.base = base

    def calcular(self):
        return math.log(self.numero, self.base)

class Factorial(OperacionCientifica):
    def __init__(self, numero):
        if numero < 0 or not isinstance(numero, int):
            raise ValueError("El factorial solo se puede calcular de números enteros no negativos.")
        self.numero = numero

    def calcular(self):
        return math.factorial(self.numero)


def calculadora_cientifica():
    while True:
        print("\n CALCULADORA CIENTÍFICA")
        print("1. Raíz Cuadrada")
        print("2. Potencia")
        print("3. Logaritmo")
        print("4. Factorial")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                num = float(input("Ingrese un número: "))
                resultado = RaizCuadrada(num).calcular()
                print(f" Resultado: {resultado:.2f}")

            elif opcion == "2":
                base = float(input("Ingrese la base: "))
                exponente = float(input("Ingrese el exponente: "))
                resultado = Potencia(base, exponente).calcular()
                print(f" Resultado: {resultado:.2f}")

            elif opcion == "3":
                num = float(input("Ingrese un número: "))
                base_log = input("Ingrese la base del logaritmo (presione Enter para base e): ")
                base_log = float(base_log) if base_log else math.e
                resultado = Logaritmo(num, base_log).calcular()
                print(f" Resultado: {resultado:.4f}")

            elif opcion == "4":
                num = int(input("Ingrese un número entero no negativo: "))
                resultado = Factorial(num).calcular()
                print(f" Resultado: {resultado}")

            elif opcion == "5":
                print(" Saliendo de la calculadora. ¡Hasta luego!")
                break

            else:
                print(" Opción no válida. Intente de nuevo.")

        except ValueError as e:
            print("Error:", e)

calculadora_cientifica()



##1. Tanque de gasolina
def calcular_porcentaje(f):
    try:
        x, y = map(int, f.split('/'))
        if y == 0:
            raise ZeroDivisionError("El denominador (Y) no puede ser cero.")

        if x / y < 0.01:
            return "E"
        elif x / y > 0.99:
            return "F"
        else:
            porcentaje = int(round((x / y) * 100))
            return f"{porcentaje}%"
    except ValueError:
        return "Error: X e Y deben ser números enteros."
    except ZeroDivisionError as e:
        return f"Error: {e}"

while True:
    fraccion = input("Ingrese una fracción en formato X/Y: ")
    resultado = calcular_porcentaje(fraccion)
    print(f"Cantidad de combustible en el tanque: {resultado}")



    continuar = input("¿Desea ingresar otra fracción? (SI/NO): ").strip().upper()
    if continuar != 'SI':
        break

##2. Lista de calificaciones
calificaciones_input = input("Ingrese una lista de calificaciones separadas por comas: ")
calificaciones_lista = calificaciones_input.split(',')

calificaciones_enteros = []

for calificacion_str in calificaciones_lista:
    try:
        calificacion = int(calificacion_str.strip())
        calificaciones_enteros.append(calificacion)
    except ValueError:
        print(f"Error: '{calificacion_str}' no es una calificación válida.")

print("Calificaciones enteras:", calificaciones_enteros)

##3. Circulo
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area = 3.14159 * self.radio ** 2
        return area

radio_ingresado = float(input("Ingrese el radio del círculo: "))
circulo = Circulo(radio_ingresado)

area_calculada = circulo.calcular_area()
print(f"El área del círculo con radio {radio_ingresado} es: {area_calculada:.2f}")

##4. Rectángulo
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        area = self.largo * self.ancho
        return area

largo_ingresado = float(input("Ingrese el largo del rectángulo: "))
ancho_ingresado = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = Rectangulo(largo_ingresado, ancho_ingresado)

area_calculada = rectangulo.calcular_area()
print(f"El área del rectángulo con largo {largo_ingresado} y ancho {ancho_ingresado} es: {area_calculada:.2f}")
##5. Alumno
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
    
    def setAge(self, edad):
        self.edad = edad
    
    def setNota(self, notas):
        self.notas = notas

nombre_alumno = input("Ingrese el nombre del alumno: ")
numero_registro_alumno = input("Ingrese el número de registro del alumno: ")
alumno = Alumno(nombre_alumno, numero_registro_alumno)


edad_alumno = int(input("Ingrese la edad del alumno: "))
alumno.setAge(edad_alumno)


num_notas = int(input("Ingrese el número de notas: "))
notas_alumno = []
for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas_alumno.append(nota)
alumno.setNota(notas_alumno)


print("\nInformación del alumno:")
alumno.display()
##.6. Ejercicio 2 Cuadrantes
class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
        else:
            return "En el origen"
    
    def vector(self, otro_punto):
        vector_resultante = Punto(otro_punto.x - self.x, otro_punto.y - self.y)
        return vector_resultante

x1 = float(input("Ingrese la coordenada X del primer punto: "))
y1 = float(input("Ingrese la coordenada Y del primer punto: "))
punto1 = Punto(x1, y1)

x2 = float(input("Ingrese la coordenada X del segundo punto: "))
y2 = float(input("Ingrese la coordenada Y del segundo punto: "))
punto2 = Punto(x2, y2)


print("Primer punto:", punto1)
print("Cuadrante:", punto1.cuadrante())
print("Segundo punto:", punto2)
print("Cuadrante:", punto2.cuadrante())


vector_resultante = punto1.vector(punto2)
print("Vector entre los dos puntos:", vector_resultante)
##. 7. Modulo con numeros aleatorios, lista y valores en pantalla
import random

def generar_numeros_aleatorios(cantidad):
    numeros = [random.randint(0, 100) for _ in range(cantidad)]
    return numeros

def mostrar_lista(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero, end=" ")
    print()

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

##. 8. Operaciones.py 
def suma(a, b):
    try:
        result = a + b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido"

def resta(a, b):
    try:
        result = a - b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido"

def producto(a, b):
    try:
        result = a * b
        return result
    except TypeError:
        return "Error: Tipo de dato no válido"

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError
        result = a / b
        return result
    except (TypeError, ZeroDivisionError):
        return "Error: No es posible realizar la operación"




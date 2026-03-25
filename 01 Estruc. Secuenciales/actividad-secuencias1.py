import math 
#Actividad 1 
print("Hola mundo!")

#Actividad 2 
print("Frase de bienvenida")
nombre = input("Cual es tu nombre?:")
print(f"Hola, {nombre}!")

#Actividad 3
apellido = input("Cual es tu apellido?:")
edad = input("Cual es tu edad?:")
residencia = input("En que pais vivis?:")

print(f"Hola soy {nombre} {apellido}, tengo {edad} años, y soy de {residencia}")

#Actividd 4
print("Calcular area y perimetro apartir del radio dado")
radio= float(input("Ingresa el radio del circulo:"))

area = int(math.pi * (radio ** 2))
perimetro = int(2 * math.pi * radio)

print(f"El area del circulo es: {area} ")
print(f"El perimetro del circulo es: {perimetro} ")

#Actividad 5
print("Pasar segundos a horas")
segundos = int(input("Ingresa la catidad cantidad segundos que quieras:"))
horas = segundos / 3600
print(f"Esto es lo que equivale los segundos a horas: {horas}hs")

#Actividad 6
print("Mostrar la tabla de multiplicacion de un determinado numero")
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1,11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")

#Actividad 7
print("Mostrar todas las operaciones entre dos numeros")
num1 = float(input("Ingrese el primer número entero (distinto de 0): "))
num2 = float(input("Ingrese el segundo número entero (distinto de 0): "))
if num1 > 0 and num2 > 0 :
  suma = num1 + num2
  resta = num1 - num2
  multiplicacion = num1 * num2
  division = round(num1 / num2,2)
else:
  print("Error: Tienes que elegir un numero por arriba de 0")
  

(f"\nResultados:")
print(f"El resultado de sumar ambos numeros es: {suma}")
print(f"El resultado de restar ambos numeros es: {resta}")
print(f"El resultado de multiplicar ambos numeros es: {multiplicacion}")
print(f"El resultado de dividir ambos numeros es: {division:.2f}")

#Actividad 8 
print("Calcular masa corporal")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg:"))
IMC = peso / (altura ** 2)

print(f"Su indice de masa corporal es el siguiente:{round(IMC)} ")

#Actividad 9
print("Calcular Celcius a Fahrenheit")
celcius = float(input("Ingrese una temperatura en Celcius:"))
fahrenheit = celcius * 1.8 + 32

print(f"La temperatura de Celsius({celcius}) a Fahrenheit es de: {round(fahrenheit)}")

#Actividad 10
print("Promedios entre 3 numeros")
pro1 = int(input("Ingrese el primer numero:"))
pro2 = int(input("Ingrese el segundo numero:"))
pro3 = int(input("Ingrese el tercer numero:"))
promedio = (pro1 + pro2 + pro3) / 3 
print(f"Este es el promedio de los 3 numeros que ingresaste: {promedio}")
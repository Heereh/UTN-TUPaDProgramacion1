#Actividad 1
userEdad = int(input("Ingrese su edad:"))

if (userEdad >= 18):
  print("Usted es mayor de edad")
else:
  print("Usted es menor de edad")

#Activiad 2
print("Aprobacion de materias")

nota = int(input("Ingrese su nota:"))
if nota >= 6:
  print("Usted aprobo!")
else:
  print("Usted desaprobo :(")

#Actividad 3
print("Su numero es par o impar?")
numPar = int(input("Ingrese un numero par"))

if(numPar % 2 == 0):
  print("Ha ingresado un numero par")
else:
  print("Por favor ingrese un numero par")

#Actividad 4
print("Eres un Niño, Adolecente, Adulto?")
userEdad = int(input("Por favor ingrese su edad: "))

if(userEdad < 12):
  print("Usted es un niño/a")
elif userEdad >= 12 and userEdad < 18:
  print("Usted es un adolescente")
elif userEdad >= 18 and userEdad < 30:
  print("Usted es un Adulto/a joven")
else: 
  print("Usted es un adulto/a")

#Actividad  5
password = len(input("Por favor ingrese una contraseña:"))


if(password >= 8 and password <= 14):
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
print("Consumo mensual de energia en Kilovatios")
consumoMensualKwh = int(input("Cuanto consumes de energia(en kWh):"))

if(consumoMensualKwh < 150):
  print(f"Tu consumo de {consumoMensualKwh} kWh es un consumo bajo ")
elif consumoMensualKwh >= 150 and consumoMensualKwh < 300:
  print(f"Tu consumo de {consumoMensualKwh} kWh es un consumo medio ")
elif consumoMensualKwh >= 300 and consumoMensualKwh <= 500:
  print(f"Tu consumo de {consumoMensualKwh} es un consumo alto ")
else:
  print(f"Considere medidas de ahorro energetico {consumoMensualKwh} kWh ")

#Actividad 7
text = input("Escribe una frase o una palabra: ")
vocales = ('a', 'e', 'i', 'o', 'u')

if (text.lower().endswith(vocales)):
  print(text + '!')  
else:
  print(f"Tu palabra '{text}' no termina en vocal")

#Actividad 8

userName = input("Ingrese su nombre: ")
options = int(input("Ingrese un numero del 1 al 3"))


if(options == 1):
  print(userName.upper())
elif options == 2:
  print(userName.lower())
elif options == 3:
  print(userName.title())
else:
  print("No se encontro la opcions")

#Actividad 9
print("Magnitud del terremoto")
magnitud = int(input("Ingrese la escala del terremoto: "))

if(magnitud < 3 ):
  print("Muy leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
  print("Leve (Ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5 :
  print("Moderado (Sentido por personas, pero sin causar daño)")
elif magnitud >= 5 and magnitud < 6:
  print("Fuerte (Causa daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
 print("Muy fuerte (Puede causar daños significativos)")
elif magnitud >= 7:
  print("Extremo (Puede causar graves daños a gran escala)")

#Actividad 10
print("En que estacion del año estas?")
hemisferio = input("En que hemisferio te encuentras norte/sur: ").lower()
mes = int(input("En que mes te encuentras: "))
dia = int(input("En que dia te encuentras?: "))

if  (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
  estacion = "Invierno"
elif (mes == 3 and dia >= 21) or (mes in [4,5]) or (mes == 6 and dia <= 20):
  estacion = "Primavera"
elif (mes == 6 and dia >= 21) or (mes in [7,8]) or (mes == 9 and dia <= 20):
  estacion = "Verano"
elif (mes == 9 and dia >= 21) or (mes in [10,11])  or (mes == 12 and dia <= 20):
  estacion = "Otoño"
else:
  estacion = "Fecha invalida"


if hemisferio == "sur":
    if estacion == "Invierno":
        estacion = "Verano"
    elif estacion == "Verano":
        estacion = "Invierno"
    elif estacion == "Primavera":
        estacion = "Otoño"
    elif estacion == "Otoño":
        estacion = "Primavera"

print("La estación es:", estacion)

#Actividad 1 - “Caja del Kiosco ”
Total_sin_descuentos = 0
Total_con_descuentos = 0
ahorro_total = 0

while True:
  nombre = input("Ingrese su nombre:")
  if(nombre.isalpha() and nombre != ""):
    break
  else:
    print("Error, ingrese un nombre valido.")

while True:
  cantidad_productos = input("Ingrese la cantidad de productos que compro")
  if(cantidad_productos.isdigit()and int(cantidad_productos) > 0):
    cantidad_productos = int(cantidad_productos)
    break
  else:
    print("Error, ingrese una cantidad valida.")
print("Cliente:",nombre)
for i in range(cantidad_productos):
  precio = input(f"ingrese el precio del producto {i+1}")
  while not precio.isdigit():
    print("Error, ingrese un precio valido.")
    precio = input(f"ingrese el precio del producto {i+1}")
  precio = int(precio)
  Total_sin_descuentos += precio
  descuento = input(f"El producto {i+1} tiene descuento? (S/N)")
  while descuento.lower() not in ['s', 'n']:
    print("Error, ingrese S o N.")
    descuento = input(f"El producto {i+1} tiene descuento? (S/N)")
  if descuento.lower() == 's':
    precio_con_descuento = precio * 0.9
    Total_con_descuentos += precio_con_descuento
  else:
    Total_con_descuentos += precio
  print(f"Producto {i+1} - precio: {precio:.2f} - Descuento Aplicado(S/N): {descuento.upper()}")

print("\n")
print("Resumen de compra:")

print(f"Total sin descuentos: ${Total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${Total_con_descuentos:.2f}")
print(f"Ahorro: ${Total_sin_descuentos - Total_con_descuentos:.2f}")
print(f"Promedio por producto: ${(Total_con_descuentos) / cantidad_productos:.2f}")


#Actividad 2 - “Acceso al Campus y Menú Seguro”
usuario = "alumno"
contraseña = "python123"
max_intentos = 3
intentos = 0

while intentos < max_intentos:
  ingreso_usuario = input("Ingresu su usuario:")
  ingrese_contraseña = input("Ingrese su contraseña:")

  if ingreso_usuario == usuario and ingrese_contraseña == contraseña:

    print("Bienvenido al campus virtual!")
    while True:

      print("\nMenu:")
      print("1. Estado de inscripción")
      print("2. Cambiar contraseña")
      print("3.Mensaje motivacional")
      print("4. Salir")
      
      opcion = input("Seleccione una opción:")

      while not opcion.isdigit() or not 1 <= int(opcion) <= 4:
        print("Error, ingrese una opcion valida.")
        opcion = input("Seleccione una opción:")
      
      if opcion == "1":
        print("Su estado de inscripcion es: Inscripto")

      elif(opcion == "2"):
        while True:
          nueva_contraseña = input("Ingrese su nueva contraseña:")
          
          if len(nueva_contraseña) < 6:
            print("Error, la contraseña debe tener al menos 6 caracteres")
            continue

          confirmacion_contraseña = input("Confirme su nueva contraseña:")

          if nueva_contraseña != confirmacion_contraseña:
            print("Error, las contraseñas no coinciden")
            continue
          contraseña = nueva_contraseña
          #Sale del mini bucle del cambio de contraseña y vuelve al principal
          print("Contraseña cambiada exitosamente!")
          break
      elif(opcion == "3"):
        print("¡Sigue adelante! Tu esfuerzo está dando resultados.")
      elif(opcion == "4"):
        print("Gracias por usar el sistema.")
        intentos = max_intentos  # Salir del bucle principal
        break
      else:
        print("Opción no válida.")
  else:
    intentos += 1
    print(f"Credenciales invalidas. Intento {intentos} de {max_intentos}.")
    if intentos >= max_intentos:
      print("Has alcanzado el número máximo de intentos. Acceso bloqueado.")

#Actividad 3 - “Agenda de turnos con nombres(sin listas)”
lunes1 =  ""
lunes2 =  ""
lunes3 =  ""
lunes4 =  ""

martes1 =  ""
martes2 =  ""
martes3 =  ""

while True:
  operador = input("Ingrese el nombre del operador:")
  if operador.isalpha():
    break
  else:
    print("Error, ingrese un nombre valido.")




while True:
  print("\nMenu de turnos:")
  print("1. Reservar turno ")
  print("2. cancelar turno")
  print("3. Ver agenda del dia")
  print("4. Ver resumen general")
  print("5. Salir del sistema")
  opcion = input("Seleccione una opción:")

  if not opcion.isdigit() or not 1 <= int(opcion) <= 5:
    print("Error, ingrese una opcion valida.")
    opcion = input("Seleccione una opción:")

  if opcion == "1":
    #ELEGIR DIA ENTRE LUNES O MARTES
    while True:
      dia = input("Ingrese el dia para reservar un turno (Lunes/Martes): ").lower()
      
      while not dia.isalpha():
        print("Error, ingrese un dia valido.")
        dia = input("Ingrese el dia para reservar un turno (Lunes/Martes): ").lower()

      if dia.lower() == "lunes":

        nombre_paciente = input("Ingrese el nombre del paciente:").lower()
        while not nombre_paciente.isalpha():
          print("Error, ingrese un nombre valido.")
          nombre_paciente = input("Ingrese el nombre del paciente:")

        if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
          print("Error, el paciente ya tiene un turno reservado ese dia.")

        elif lunes1 == "":
          lunes1 = nombre_paciente
          print("Guardado en el primer turno del lunes.")
        elif lunes2 == "":
          lunes2 = nombre_paciente
          print("Guardado en el segundo turno del lunes.")
        elif lunes3 == "":
          lunes3 = nombre_paciente
          print("Guardado en el tercer turno del lunes.")
        elif lunes4 == "":
          lunes4 = nombre_paciente
          print("Guardado en el cuarto turno del lunes.")
        else:
          print("Error, no hay turnos disponibles para el lunes.")
        break
      elif dia.lower() == "martes":
        nombre_paciente = input("Ingrese el nombre del paciente:").lower()

        while not nombre_paciente.isalpha():
          print("Error, ingrese un nombre valido.")
          nombre_paciente = input("Ingrese el nombre del paciente:").lower()

        if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
          print("Error, el paciente ya tiene un turno reservado ese dia.")
        elif martes1 == "":
          martes1 = nombre_paciente
          print("Guardado en el primer turno del martes.")
        elif martes2 == "":
          martes2 = nombre_paciente
          print("Guardado en el segundo turno del martes.")
        elif martes3 == "":
          martes3 = nombre_paciente
          print("Guardado en el tercer turno del martes.")
        else:
          print("Error, no hay turnos disponibles para el martes.")
      else:
        print("Error, ingrese un dia valido.")
        break
  elif opcion == "2":
    #Cancelar turno
    while True:
      dia_cancelar = input("Ingrese el dia para cancelar un turno (Lunes/Martes): ")
      nombre_paciente_cancelar = input("Ingrese el nombre del paciente para cancelar el turno:").lower()
      
      while not nombre_paciente_cancelar.isalpha():
          print("Error, ingrese un nombre valido.")
          nombre_paciente_cancelar = input("Ingrese el nombre del paciente:").lower()
      
      if dia_cancelar.lower() == "lunes":
        if nombre_paciente_cancelar == lunes1:
          lunes1 = ""
          print("Turno del lunes cancelado para", nombre_paciente_cancelar)
        elif nombre_paciente_cancelar == lunes2:
          lunes2 = ""
          print("Turno del lunes cancelado para", nombre_paciente_cancelar)
        elif nombre_paciente_cancelar == lunes3:
          lunes3 = ""
          print("Turno del lunes cancelado para", nombre_paciente_cancelar)
        elif nombre_paciente_cancelar == lunes4:
          lunes4 = ""
          print("Turno del lunes cancelado para", nombre_paciente_cancelar)
        else:
          print("Error, no se encontró un turno para ese paciente el lunes.")
        break
      elif dia_cancelar.lower()== "martes":
        if nombre_paciente_cancelar == martes1:
          martes1 = ""
          print("Turno del martes cancelado para", nombre_paciente_cancelar)
        elif nombre_paciente_cancelar == martes2:
          martes2 = ""
          print("Turno del martes cancelado para", nombre_paciente_cancelar)
        elif nombre_paciente_cancelar == martes3:
          martes3 = ""
          print("Turno del martes cancelado para", nombre_paciente_cancelar)
        else:
          print("Error, no se encontró un turno para ese paciente el martes.")
      else:
        print("Error, ingrese un dia valido.")
      
  elif opcion == "3":
    #Ver agenda del dia
    while True:
      dia_agenda = input("Ingrese el dia para ver la agenda (Lunes/Martes):")

      while not dia_agenda.isalpha():
        print("Error, ingrese un dia valido.")
        dia_agenda = input("Ingrese el dia para ver la agenda (Lunes/Martes):")

      if dia_agenda.lower() == "lunes":
        print("Agenda del lunes:")
        print("Turno 1:", lunes1 if lunes1 != "" else "Disponible")
        print("Turno 2:", lunes2 if lunes2 != "" else "Disponible")
        print("Turno 3:", lunes3 if lunes3 != "" else "Disponible")
        print("Turno 4:", lunes4 if lunes4 != "" else "Disponible")
        break
      elif dia_agenda.lower() == "martes":
        print("Agenda del martes:")
        print("Turno 1:", martes1 if martes1 != "" else "Disponible")
        print("Turno 2:", martes2 if martes2 != "" else "Disponible")
        print("Turno 3:", martes3 if martes3 != "" else "Disponible")
        break
      else:
        print("Error, ingrese un dia valido.")
  elif opcion == "4":
    #Ver resumen general
    #Turnos ocupados y disponibles para cada dia
    #Dia con mas turnos(o empate)
    ocup_lunes=0
    ocup_martes=0
    print("Resumen general:")
    if lunes1 !="": ocup_lunes += 1
    if lunes2 !="": ocup_lunes += 1
    if lunes3 !="": ocup_lunes += 1
    if lunes4 !="": ocup_lunes += 1

    if martes1 !="": ocup_martes += 1
    if martes2 !="": ocup_martes += 1
    if martes3 !="": ocup_martes += 1
    
    print("\n--- RESUMEN ---")
    print("Lunes: ocupados =", ocup_lunes, "| libres =", 4 - ocup_lunes)
    print("Martes: ocupados =", ocup_martes, "| libres =", 3 - ocup_martes)
    if ocup_lunes > ocup_martes:
      print("El dia con mas turnos ocupados es: Lunes")
    elif ocup_martes > ocup_lunes:
      print("El dia con mas turnos ocupados es: Martes")
    else:
      print("Ambos dias tienen la misma cantidad de turnos ocupados.")
  elif opcion == "5":
    print("Cerrando el sistema.")
    break

#Actividad 4 - "Escape Room: La Bóveda"
energia =100
tiempo =12
cerraduras_abiertas=0
alarma = False
codigo_parcial=""
intentos = 0 

while True:
  nombre_agente = input("Ingrese su nombre:")
  if nombre_agente.isalpha() and nombre_agente != "":
    break
  else:
    print("Error, ingrese un nombre valido.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
  print("\n--- Menu ---")
  print("1.Forzar cerradura")
  print("2.Hackear panel")
  print("3.Descansar")

  opcion = input("Seleccione una opcion:")
  while not opcion.isdigit() or not 1 <= int(opcion) <= 3:
    print("Error, ingrese una opcion valida.")
    opcion = input("Seleccione una opcion:")
  if opcion == "1":
    energia -= 20
    tiempo -= 2
    intentos += 1
    ##Anti-spam de la opcion 1
    if intentos >= 3:
      print("la cerradura se trabó!")
      alarma = True
      break
    
    #Si la energia esta por debajo de 40, hay riesgo de alarma
    if energia < 40:
      print("Energia baja, riesgo de activar la alarma!")
      #Pedir un numero 1-3(Validado), si elige 3 => alarma activada
      while True:
        decision = input("Elige un numero del 1 al 3 para intentar forzar la cerradura sin activar la alarma:")
        if decision.isdigit() and 1 <= int(decision) <= 3:
          break
        else:
          print("Error, ingrese un numero valido.")
          if decision == "3":
            alarma = True
            print("¡Alarma activada!")
          else:
            print("¡Cerradura forzada con éxito!")
            cerraduras_abiertas += 1
    elif energia >= 40:
      print("¡Cerradura forzada con éxito!")
      cerraduras_abiertas += 1
  elif opcion == "2":
    energia -= 10
    tiempo -= 3
    intentos = 0 #Reinicia el contador de intentos para forzar cerradura

    for i in range(4):
      codigo_parcial += "A"
      print(f"Hackeando panel... Progreso: {len(codigo_parcial)*0.25}%")
      if len(codigo_parcial) >= 8 and cerraduras_abiertas > 0:
        print("Codigo completo! Se abrio una cerradura!")
        cerraduras_abiertas += 1
        codigo_parcial= ""  #Se reinicia el codigo
  elif opcion == "3":
    energia += 15 # Max energia = 100
    if energia > 100:
      energia = 100
    tiempo -= 1
    intentos = 0 #Reinicia el contador de intentos para forzar cerradura
    if alarma == True:
      energia -= 10
      print("Alarma activada! perdiste 10 de energia!")
  print(f"Estado actual - Energia: {energia}, Tiempo: {tiempo} horas, Cerraduras restantes: {cerraduras_abiertas}, Alarma: {'Activada' if alarma else 'Desactivada'}")
  if cerraduras_abiertas == 3:
    print("Victoria! Has abierto 3 cerraduras y escapaste!")
    break
  if energia <= 0 or tiempo <= 0:
    print("Has perdido! No te quedo energia o se acabo el tiempo.")
    break
  if alarma:
    print("Has perdido! La alarma se activo.")
    break

#Ejercicio 5  — “Escape Room:"La Arena del Gladiador"  
vida_gladiador= 100
vida_enemigo = 100
pociones = 3
daño_base= 15
daño_base_enemigo = 12
turno_gladiador = True

while True:
  gladiador = input("Ingrese el nombre de su gladiador:")
  if gladiador.isalpha() and gladiador != "":
    break
  else:
    print("Error, ingrese un nombre valido.")

print("\n --- BIENVENIDO A LA ARENA ---  ")
print(f"Nombre del gladiador: {gladiador}")
print("\n --- INICIO DEL COMBATE ---")

while vida_gladiador > 0 and vida_enemigo > 0:
  print(f"{gladiador} - Vida: {vida_gladiador}, Pociones: {pociones}")
  print(f"Enemigo - Vida: {vida_enemigo}")

  if turno_gladiador:
  #Turno del jugador
    print("\n--- Menu de acciones ---")
    print("1. Ataque pesado")
    print("2. Rafaga veloz")
    print("3.Curar")

    opcion = input("Seleccione una opcion:")
    while not opcion.isdigit() or not 1 <= int(opcion) <= 3:
      print("Error, ingrese una opcion valida.")
      opcion = input("Seleccione una opcion:")
  
    if opcion == "1":
      if vida_enemigo < 20:
        daño_critico = daño_base * 1.5
        vida_enemigo -= daño_critico
        print(f"\n¡Atacaste al enemigo por {daño_critico} de daño!")
        turno_gladiador = False
      else:
        vida_enemigo -= daño_base
        print(f"\n¡Atacaste al enemigo por {daño_base} de daño!")
        turno_gladiador = False

    elif opcion == "2":
      for i in range(3):
        daño_rapido = 5
        vida_enemigo -= daño_rapido
        print(f"Golpe conectado por {daño_rapido} de daño!")
      turno_gladiador = False

    elif opcion == "3":
      if pociones > 0:
        vida_gladiador += 30
        if vida_gladiador > 100:
          vida_gladiador = 100
        print(f"¡Te curaste por 30 puntos de vida! Vida actual: {vida_gladiador}")
        pociones -= 1
        turno_gladiador = False

      else:
        #Si el jugador intenta curarse sin pociones, pierde un turno y recibe daño del enemigo
        print("No te quedan pociones!")
        turno_gladiador = False
  else:
    print("\n--- Turno del enemigo ---")
    if vida_enemigo > 0:
      vida_gladiador -= daño_base_enemigo
      print(f"¡El enemigo te atacó por {daño_base_enemigo} de daño!")
      turno_gladiador = True

if vida_gladiador > 0 and vida_enemigo <= 0:
  print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
elif vida_gladiador <= 0 and vida_enemigo > 0:
  print("DERROTA. Has caído en combate.")


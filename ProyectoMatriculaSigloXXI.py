#Trabajo realizado por:
#Sebastian Araya Zumbado
#Raúl Sayed Martínez Arce
#Mario Molina Medal


#Sobre la información para matricular en la Universidad
def guardarDatos():
    #Guardar datos "virtual"
    datos = open ("virtual.txt", "w")
    for i in range (20):
        suma = 0
        for j in range (10):
            if suma < 9:
                b = str (virtual [i][j]) + ", "
            else:
                b = str (virtual [i][j]) + "\n"
            suma += 1
            datos.write (b)
    datos.close()

    #Guardar datos "presencial"
    file = open ("presencial.txt", "w")
    for i in range (20):
        suma = 0
        for j in range (25):
            if suma < 24:
                b = str (presencial [i][j]) + ", "
            else:
                b = str (presencial [i][j]) + "\n"
            suma += 1
            file.write (b)
    file.close()

#Sobre la información de la matricula
def informacion ():
    print ("***********************")
    print ("\nPara la Universidad Siglo XX, es muy importante que usted conozca sobre la información de matricula y descuentos.")
    print ("A continuación, le mostramos la información solicitada")
    print ("\nLa cantidad mínima de materias a matricular es de 2 y la máxima de 6.") 
    print ("Cada materia tiene un valor de 120000 CRC y la matricula tiene un valor de 70000 CRC")
    print ("Si matricula 4 o más materias se le aplicará algún descuento, ¡Ver información detallada de los descuentos en la opción 2!\n")
    print ("***********************")
    
#Sobre los descuentos que aplican según las materias a matricular
def descuento ():
    print ("***********************")
    print ("\nLa Universidad Siglo XX, le muestra el detalle de donde se aplican los descuentos")
    print ("\ni. Si matricula 3 o menos materias no existe descuento.")
    print ("ii. Si matricula 4 ó 5 materias tiene un descuento por materia de 10% (no aplica a la matrícula).")
    print ("iii. Si matricula 6 materias, tiene un descuento por materia de 15% y por matrícula del 5%.\n")
    print ("***********************") 

#Proceso de matricula
def matricula ():
    print ("***********************")

# Solicitar datos personales y definir las variables que almacenarán la información
# personal del estudiante
    nombre = input("Digíte el nombre de la persona a matricular: ")
    apellido1 = input ("Digíte el primer apellido: ")
    apellido2 = input ("Digíte el segundo apellido: ")
    numtelefono = input("Digite el numero de telefono: ")

#Creamos un "WHILE" para ver si el correo está bien digitado.
    arrobas = 0
    while arrobas != 1:    
        correo = input ("Digíte el correo electronico: ")
        for i in correo:
            if i == "@":
                arrobas = arrobas + 1
        if arrobas != 1:
            print ("Ingresó mal su correo, intentelo de nuevo")
#Definir si el estudio será virtual o presencial
    tipo = 0
    modalidad = ""
    while tipo != 1 and tipo != 2:
        tipo = int (input ("\nModalidad: \n1.Virtual \n2.Presencial\n\nElija la modalidad que desee: "))
        if tipo == 1:
            modalidad = ("Virtual")
            print (nombre + " su modalidad de estudio será VIRTUAL")
        elif tipo == 2:
            modalidad = ("Presencial")
            print (nombre + " su modalidad de estudio será PRESENCIAL")
        else:
            print ("***********************")
            print ("Esa opción no es correcta.")
#Variables para calcular costos        
    matricula = 70000
    costoMateria = 120000
    cantidadMaterias = int(input("\nCantidad de materias a matricular: "))
#Se creo un WHILE, para limitar la matricula de materias de 2 a 6
    while cantidadMaterias <= 1 or cantidadMaterias >= 7:
        print ("La cantidad de materias que dígitó no es correcta")
        cantidadMaterias = int(input("\nCantidad de materias a matricular: "))
#Cursos a matricular:
    print ("\nLista de cursos a matricular: ")
    print ("C1 - C2 - C3 - C4 - C5 - C6 - C7 - C8 - C9 - C10 - C11 - C12 - C13 - C14 - C15 - C16 - C17 - C18 - C19 - C20")
    print ("\nCuales cursos desea llevar: ")
    cursos = []
    for i in range (cantidadMaterias):
        curso = 1
        while curso != 0:
            curso = int (input ("Curso a matricular: C"))
            if curso <= 20 and curso >= 0:
                cursos.append (curso)
                curso = curso - 1
                if tipo == 1:
                    if virtual [curso][0] == 0:
                        virtual [curso].append (1)
                        virtual [curso].pop (0)
                        #print ("Actualización\n\n\n\n", virtual)
                        curso = 0
                    else:
                        print ("Cupo lleno para este curso en la modalidad VIRTUAL")
                        print ("Inicie de nuevo el proceso de matricula")
                        menu ()
                else:
                    if presencial [curso][0] == 0:
                        presencial [curso].append (1)
                        presencial [curso].pop (0)
                        #print ("Actualización\n\n\n\n", presencial)
                        curso = 0
                    else:
                        print ("Cupo lleno para este curso en la modalidad PRESENCIAL")
                        print ("Inicie de nuevo el proceso de matricula")
                        menu ()
            else:
                print ("Valor incorrecto")

#Matricula de 2 o 3 materias     
    pago = 0 
    if cantidadMaterias == 2 or cantidadMaterias == 3:
        print ("No aplica descuento para esta cantidad de materias")
        montomateria = matricula + (costoMateria * cantidadMaterias) 
        print ("El monto total a pagar es de: ", montomateria, "CRC")
        print()
        print()
        print ("¡Muchas gracias", nombre, "por matricular con la Universidad Fidélitas Siglo XX!")
        print ("\n***********************")
        pago += montomateria
        
#Matricula de 4 o 5 materias
    elif cantidadMaterias == 4 or cantidadMaterias == 5:
        print ("Tiene un descuento por materia de 10% (No aplica a la matrícula)")
        monto4or5materia = costoMateria * cantidadMaterias
        descuento = monto4or5materia * (10 / 100)
        montoTotal = monto4or5materia - descuento
        montoFinal = montoTotal + matricula
        print ("El monto total a pagar es de: ", montoFinal, "CRC")
        print()
        print()
        print ("¡Muchas gracias", nombre, "por matricular con la Universidad Fidélitas Siglo XX!")
        print ("\n***********************")
        pago += montoFinal
        
#Matricula de 6 materias
    elif cantidadMaterias == 6:
        print ("Tiene un descuento por materia de 15% y por matrícula del 5%")
        monto6materia = costoMateria * cantidadMaterias
        descuentoMaterias = monto6materia * (15 / 100)
        descuentoMatricula = matricula * (5/100)
        montoTotal = (monto6materia - descuentoMaterias) + (matricula - descuentoMatricula)
        print ("El monto total a pagar es de: ", montoTotal, "CRC")
        print()
        print()
        print ("¡Muchas gracias", nombre, "por matricular con la Universidad Fidélitas Siglo XX!")
        print ("\n***********************")
        pago += montoTotal
                    
#Se guardan los datos personales del cliente en un solo archivo plano txt. llamado "miarchivo"
#y en otro archivo plano txt. con el nombre de la persona        
    n = 0
    for i in range (2):
        if n == 0:            
            archivo = open("miarchivo.txt","a")
            n += 1
        else:
            archivo = open (nombre + " " + apellido1 + " " + apellido2 + ".txt", "a")
        for i in range (1):
            archivo.write("Nombre: " + nombre + "\n")
            archivo.write("Primer apellido: " + apellido1 + "\n")
            archivo.write("Segundo apellido: " + apellido2 + "\n")
            archivo.write("Número de teléfono: " + numtelefono + "\n")
            archivo.write("Correo: " + correo + "\n")
            archivo.write("Modalidad: " + modalidad + "\n")
            archivo.write("Cantidad de materias matriculadas: " + str (cantidadMaterias) + "\n")
            for i in range (len (cursos)):
                archivo.write("Curso Matriculado: C" + str (cursos[i]) + "\n")
            archivo.write("Monto total: " + str (pago) + "\n")
            archivo.write("************************\n")
            archivo.close()
    guardarDatos()
        
def congelamiento ():
    print ("***********************")
    print ("Proceso de congelamiento de uno o varios cursos\n")
    n = input ("Digíte el nombre con el que matriculo: ")
    a = input ("Digíte el primer apellido con el que matriculo: ")
    a2 = input ("Digíte el segundo apellido con el que matriculo: ")
    for i in range (1):
        if os.path.exists(n + " " + a +  " " + a2 + ".txt"):
            print ()
        else:
            print ("\nNo hay registro de matrícula con este nombre\n")
            print ("***********************")
            menu ()
    tipo = 0
    cantidad = 1
    while cantidad != 0:
        cantidad = int (input ("Cuantos cursos desea congelar: "))
        if cantidad >= 1 and cantidad <= 6:        
            while tipo != 1 and tipo != 2:
                tipo = int (input ("Modalidad: \n1.Virtual \n2.Presencial\n\nElija una opción: "))
                if tipo == 1:
                    congelar = 0
                    for i in range (cantidad):
                        curso = int (input ("Elija el curso que desea congelar: C"))
                        curso = curso - 1
                        if virtual [curso][9] == 1:
                            virtual [curso].append (0)
                            virtual [curso].pop (9)
                            congelar += 1
                        else:
                            print ("\nEste curso no tiene matricula")
                            print ("***********************")
                    print ("\nLa cantidad de cursos que usted congeló, fue de:", congelar, "\n")
                    cantidad = 0
                elif tipo == 2:
                    congelar = 0
                    for i in range (cantidad):                        
                        curso = int (input ("Elija el curso que desea congelar: C"))
                        curso = curso - 1
                        if presencial [curso][24] == 1:
                            presencial [curso].append (0)
                            presencial [curso].pop (24)
                            congelar += 1
                        else:
                            print ("\nEste curso no tiene matricula")
                            print ("***********************")
                    print ("\nLa cantidad de cursos que usted congeló, fue de:", congelar, "\n")
                    cantidad = 0
                else:
                   print ("\nValor incorrecto\n")
        else:
            print ("\nNo se puede congelar esa cantidad de cursos\n")
            cantidad = 1
    print ("***********************")
    guardarDatos()
    
def estadistica ():
    print ("***********************")
    print ("\nEstadísticas sobre el comportamiento de los cursos:\n")
    opcion = 1
    while opcion != 0:
        print ("1. El porcentaje de ocupación general.")
        print ("2. El porcentaje de ocupación presencial.")
        print ("3. El porcentaje de ocupación virtual.")
        print ("4. El porcentaje de ocupación de todo el cuatrimestre.")
        print ("0. Devolverse al menú principal.")
        opcion = int (input ("\nElija una opción: "))

        if opcion == 1:
            maxima = 700
            suma = 0
            for i in range (20):
                for x in range (10):
                   suma += virtual [i][x]
            for i in range (20):
                for x in range (25):
                    suma += presencial [i][x]
            total = (suma / maxima) * 100
            print ("***********************")
            print ("\nEl porcentaje de ocupación general es: %", round (total, 3), "\n")
            print ("***********************")
            
        elif opcion == 2:
            maxima = 500
            suma = 0
            for i in range (20):
                for x in range (25):
                    suma += presencial [i][x]
            total = (suma / maxima) * 100
            print ("***********************")
            print ("\nEl porcentaje de ocupación presencial es: %", round (total, 3), "\n")
            print ("***********************")
        elif opcion == 3:
            maxima = 200
            suma = 0
            for i in range (20):
                for x in range (10):
                   suma += virtual [i][x]
            total = (suma / maxima) * 100
            print ("***********************")
            print ("\nEl porcentaje de ocupación general es: %", round (total, 3), "\n")
            print ("***********************")
        elif opcion == 4:
            maxima = 700
            suma = 0
            for i in range (20):
                for x in range (10):
                   suma += virtual [i][x]
            for i in range (20):
                for x in range (25):
                    suma += presencial [i][x]
            total = (suma / maxima) * 100
            print ("***********************")
            print ("\nEl porcentaje de ocupación de todo el cuatrimestre es: %", round (total, 3), "\n")
            print ("***********************")
        elif opcion == 0:
            print ()
        else:
            print ("***********************")
            print ("\nOpción incorrecta\n")
            print ("***********************\n")
            
    print ("***********************")

#Cargar archivos virtual y presencial
def modo(virtual):
    if os.path.exists("virtual.txt"):
        virtual = []
        archivo = open("virtual.txt","r")
        contenido = archivo.read()
        archivo.close()
        suma = 0
        for i in contenido.split("\n"):
            if i == "":
                break
            virtual.append([])
            for x in i.split(","):
                virtual[suma].append(int(x))
            suma = suma + 1
        return virtual
    else:
        return virtual
    
def mod(presencial):
    if os.path.exists("presencial.txt"):
        presencial = []
        file = open("presencial.txt","r")
        contenido = file.read()
        file.close()
        suma = 0
        for i in contenido.split("\n"):
            if i == "":
                break
            presencial.append([])
            for x in i.split(","):
                presencial[suma].append(int(x))
            suma = suma + 1
        return presencial
    else:
        return presencial
    
#*************************Aquí inicia el programa*************************#
import os

#Cargar información de contactos y matricula
if os.path.exists("miarchivo.txt"):
    archivo = open ("miarchivo.txt","r")
    copiar = archivo.read()
    lista = copiar.split ("\n")
    nombres = lista
    archivo.close()

#Arreglo multidimensionales para las matriculas
virtual = []
for i in range (20):
    virtual.append ([0] * 10)

presencial = []
for i in range (20):
    presencial.append ([0] * 25)

#Arreglos para modalidades de matricula
virtual = modo(virtual)
presencial = mod(presencial)

# Saludo inicial departe de la Universidad
print ("Bienvenido a la Universidad Fidélitas Siglo XX")
print ("Para nosotros es un honor que nos visite")
name = input ("\nIndiquenos cuál es su nombre: ")
print ("***********************")

# Se crea un menú para facilitar el proceso de matrícula.
def menu ():
    opcion = 1
    while opcion != 0:
        print ("\nMenú informativo y de matricula")
        print ("\n1. Conozca sobre la matricula.")
        print ("2. Conozca sobre los descuentos.")
        print ("3. Proceso de matricula.")
        print ("4. Proceso de congelamiento de materias.")
        print ("5. Conozca sobre las estadísticas en el comportamiento de los cursos.")
        print ("0. Salir.")
        opcion = int (input ("\nSeleccione una opción: "))

        if opcion == 1:
            informacion ()
        elif opcion == 2:
            descuento ()
        elif opcion == 3:
            matricula ()
        elif opcion == 4:
            congelamiento ()
        elif opcion == 5:
            estadistica ()
        elif opcion >= 6 or opcion < 0:
            print ("\nValor incorrecto, intente de nuevo\n")
        else:
            print ("¡Muchas gracias", name, "la Universidad Fidélitas Siglo XX, le desea un feliz día")

menu ()

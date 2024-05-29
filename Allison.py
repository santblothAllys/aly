#Inicialización de variables
rut_alumno_ingresado = 0
rut_alumno_consulta = 0
nota_alta = 0
nota_baja = 0
try:
    while True:
        opcion = 0  # Reiniciar la variable opcion
        while opcion != 1 and opcion != 2:
            print('Bienvenido a la escuela')
            print('---------MENU---------')
            print('1) Menú alumnos')
            print('2) Menú profesores')
            opcion = int(input('Ingrese su opción\n'))
            if opcion != 1 and opcion != 2:
                print('Opción inválida')
        match opcion:
            case 1:#Opcion de alumnos
                opcion_alumnos = 0  # Reiniciar la opción para el menú de alumnos
                while opcion_alumnos != 2:
                    print('----Menú alumnos----')
                    print('1) Ver mis notas (Por RUT)')
                    print('2) Salir')
                    opcion_alumnos = int(input('Ingrese su opción\n'))
                    match opcion_alumnos:
                        case 1:
                            rut_alumno_consulta = int(input('Ingrese su RUT\n'))                
                            if rut_alumno_consulta == rut_alumno_ingresado:
                                print('Su nota más alta es:', nota_alta)
                                print('Su nota más baja es:', nota_baja)
                            else:
                                print('Su RUT no tiene datos')
                        case 2:
                            print('Adiós Alumno')
                            break
                        case 3:
                            print ('Opcion oculta')
                            break
            case 2:#Opcion de profesores
                opcion_profesores = 0  # Reiniciar la opción para el menú de profesores
                while opcion_profesores != 3:
                    print('----Menú profesores----')
                    print('1) Ingresar notas para 1 alumno (Por RUT)')
                    print('2) Ver cantidad de notas ingresadas')
                    print('3) Salir')
                    opcion_profesores = int(input('Ingrese su opción\n'))
                    match opcion_profesores:
                        case 1:
                            rut_alumno_ingresado = int(input('Ingrese el RUT de alumno a ingresar\n'))
                            cantidad_notas = int(input('Ingrese cantidad de notas a ingresar\n'))
                            for contador in range(cantidad_notas):
                                print(f'INGRESE NOTA {contador+1}')
                                nota_recorrido = float(input('Ingresar nota (1.0 al 7.0)\n'))
                                if contador == 0:
                                    nota_alta = nota_recorrido
                                    nota_baja = nota_recorrido
                                else:
                                    if nota_recorrido > nota_alta:
                                        nota_alta = nota_recorrido
                                    if nota_recorrido < nota_baja:
                                        nota_baja = nota_recorrido
                        case 2:
                            print('Su cantidad de notas ingresadas es:', cantidad_notas)
                        case 3:
                            print('Adiós Profesor')
                            break
except ValueError:
    print('Ha ocurrido un error de tipo de dato, se cerrará el programa.')

                        

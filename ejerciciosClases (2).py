notas_alumnos = []

print("Bienvenido al sistema de Notas de la Escuela Alemana")
notas_ingresar = int(input('Usted está ingresando notas, ingrese cuantas registrará (Mayor a 0)\n'))
while(notas_ingresar <= 0):
    print('Valor erróneo.')
    notas_ingresar = int(input('Usted está ingresando notas, ingrese cuantas registrará (Mayor a 0)\n'))
for contador in range(notas_ingresar):
    nota_temporal = float(input(f'Ingrese la nota número {contador+1} (1.0 y 7.0)\n'))
    while(nota_temporal < 1.0 or nota_temporal > 7.0):
        print('Nota debe ser entre 1.0 y 7.0')
        nota_temporal = float(input(f'Ingrese la nota número {contador+1} (1.0 y 7.0)\n'))
    notas_alumnos.append(nota_temporal)
print(notas_alumnos)
notas_alumnos.remove(notas_alumnos[0])
print(f'Listado removido indice 0 {notas_alumnos}')
print(len(notas_alumnos))
notas_alumnos.remove(notas_alumnos[len(notas_alumnos)-1])
print(notas_alumnos)

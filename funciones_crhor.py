from funciones_gmeds import *


def arregloHoras(horaInicio, horaFin):
    arreglo = []
    horaInicio = horaInicio.replace(":", ".")
    horaFin = horaFin.replace(":", ".")
    horaInicio = float(horaInicio)
    horaFin = float(horaFin)
    arreglo.append(horaInicio)
    while horaInicio < horaFin:
        horaInicio += 0.5
        arreglo.append(horaInicio)

    for i in range(0, len(arreglo)):
        if arreglo[i] % 1 == 0:
            arreglo[i] = str(int(arreglo[i])) + ":00"
        else:
            arreglo[i] = str(int(arreglo[i])) + ":30"
    return arreglo


def obtenerParametros(data):
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)
    rut = data[0:pos_caracter[0]]
    dia = data[pos_caracter[0]+1:pos_caracter[1]]
    horaInicio = data[pos_caracter[1]+1:pos_caracter[2]]
    horarioFin = data[pos_caracter[2]+1:]

    return rut, dia, horaInicio, horarioFin


def obtenerParametrosEditar(data):
    cont = 0
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            cont += 1
        if cont == 4:
            antiguo = data[0:i]
            nuevo = data[i+1:]
            break

    for i in range(0, len(nuevo)):
        if nuevo[i] == '-':
            pos_caracter.append(i)
    dia_nuevo = nuevo[:pos_caracter[0]]
    horaInicio_nuevo = nuevo[pos_caracter[0]+1:pos_caracter[1]]
    horaFin_nuevo = nuevo[pos_caracter[1]+1:]

    return antiguo, dia_nuevo, horaInicio_nuevo, horaFin_nuevo


def buscarIdHorario(id_medico, dia, horaInicio, horaFin):
    archivo_csv = 'horarios.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == id_medico and fila[2] == dia and fila[3] == horaInicio and fila[4] == horaFin:
                return fila[0]
        return 0


def creacionHorario(data):
    archivo_csv = 'horarios.csv'
    id_medico = 0
    rut, dia, horaInicio, horaFin = obtenerParametros(data)
    horas = arregloHoras(horaInicio, horaFin)
    if doctor_existe(rut):
        id_medico = obtenerIdMedico(rut)

        for i in range(0, len(horas)-1):
            print("inicio ", horas[i], "fin ", horas[i+1])
            horaInicio = horas[i]
            horaFin = horas[i+1]
            if buscarIdHorario(id_medico, dia, horaInicio, horaFin) != 0:
                print("horario ya existe, no se puede crear")
                return False
            id = obtener_ultimo_id(archivo_csv) + 1
            with open(archivo_csv, 'a', newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter='|')
                csv_writer.writerow([id, id_medico, dia, horaInicio, horaFin])
                print("se creo horario")

        return True

    else:
        print("no existe doctor, no se crea horario")
        return False


def eliminarHorario(data):
    archivo_csv = 'horarios.csv'
    rut, dia, horaInicio, horaFin = obtenerParametros(data)
    id_medico = obtenerIdMedico(rut)
    horarios = arregloHoras(horaInicio, horaFin)

    cont = 0
    filas_a_mantener = []
    for i in range(0, len(horarios)-1):
        horaInicio = horarios[i]
        horaFin = horarios[i+1]
        id_horario = buscarIdHorario(id_medico, dia, horaInicio, horaFin)

        if id_horario != 0:
            with open(archivo_csv, 'r') as archivo:
                csv_reader = csv.reader(archivo, delimiter='|')
                horario_encontrado = False
                for fila in csv_reader:
                    if len(fila) > 1:
                        if fila[0] == id_horario:
                            horario_encontrado = True
                        else:
                            filas_a_mantener.append(fila)

            if horario_encontrado:
                with open(archivo_csv, 'w', newline='') as archivo:
                    csv_writer = csv.writer(archivo, delimiter='|')
                    csv_writer.writerows(filas_a_mantener)
                    cont += 1
                print("Se elimino horario")
            else:
                print("No se encontro horario")

        filas_a_mantener = []

    if cont == len(horarios)-1:
        return True
    else:
        return False


def editarHorario(data):
    data_antigua, dia_nuevo, horaInicio_nuevo, horaFin_nuevo = obtenerParametrosEditar(
        data)

    rut, dia_antiguo, horaInicio_antiguo, horaFin_antiguo = obtenerParametros(
        data_antigua)

    id_medico = obtenerIdMedico(rut)
    data_nueva = rut + "-" + dia_nuevo + "-" + \
        horaInicio_nuevo + "-" + horaFin_nuevo

    print("Data antiguo: ", data_antigua)
    print("Data nuevo: ", data_nueva)
    if id_medico != 0:
        if eliminarHorario(data_antigua):
            if creacionHorario(data_nueva):
                print("Se edito horario")
                return True
            else:
                print("No se edito horario, no se pudo crear horario")
                return False
        else:
            print("No se edito horario, no se encontro horario")
            return False
    else:
        print("No se encontro médico")
        return False


# data = "1000-lunes-10:00-12:00"
# data1 = "1000-lunes-10:00-12:00-martes-11:00-12:00"
# creacionHorario(data)
# eliminarHorario(data)
# editarHorario(data1)

# obtenerParametrosEditar(data1)


# arreglo = arregloHoras("10:00", "12:00")
# print(arreglo)

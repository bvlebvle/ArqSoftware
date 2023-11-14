from funciones_gmeds import *
from funciones_crhor import *


def obtenerParametros(data):
    # nombreP-apellidoP-nombreM-ApellidoM-especialidad-dia-mes-hora
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)

    rutP = data[0:pos_caracter[0]]
    nombreP = data[pos_caracter[0]+1:pos_caracter[1]]
    apellidoP = data[pos_caracter[1]+1:pos_caracter[2]]
    rutM = data[pos_caracter[2]+1:pos_caracter[3]]
    dia = data[pos_caracter[3]+1:pos_caracter[4]]
    mes = data[pos_caracter[4]+1:pos_caracter[5]]
    hora = data[pos_caracter[5]+1:]
    return rutP, nombreP, apellidoP, rutM, dia, mes, hora


def obtenerParametrosEditar(data):

    cont = 0
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)
    rutP = data[0:pos_caracter[0]]
    rutM = data[pos_caracter[0]+1:pos_caracter[1]]
    dia_antiguo = data[pos_caracter[1]+1:pos_caracter[2]]
    mes_antiguo = data[pos_caracter[2]+1:pos_caracter[3]]
    hora_antiguo = data[pos_caracter[3]+1:pos_caracter[4]]
    dia_nuevo = data[pos_caracter[4]+1:pos_caracter[5]]
    mes_nuevo = data[pos_caracter[5]+1:pos_caracter[6]]
    hora_nuevo = data[pos_caracter[6]+1:]

    return rutP, rutM, dia_antiguo, mes_antiguo, hora_antiguo, dia_nuevo, mes_nuevo, hora_nuevo


def obtenerParametrosEliminar(data):
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)

    rutP = data[0:pos_caracter[0]]
    rutM = data[pos_caracter[0]+1:pos_caracter[1]]
    dia = data[pos_caracter[1]+1:pos_caracter[2]]
    mes = data[pos_caracter[2]+1:pos_caracter[3]]
    hora = data[pos_caracter[3]+1:]
    return rutP, rutM, dia, mes, hora


def obtenerIdCita(rutP, id_medico, dia, mes, hora):
    archivo_csv = './DB/citas.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == rutP and fila[4] == id_medico and fila[5] == dia and fila[6] == mes and fila[7] == hora:
                return fila[0]
        return 0


def crearCita(parametros):
    archivo_csv = './DB/citas.csv'
    rutP, nombreP, apellidoP, rutM, dia, mes, hora = obtenerParametros(
        parametros)
    id_medico = 0

    if doctor_existe(rutM):
        id_medico = obtenerIdMedico(rutM)

    # buscar cita
    if obtenerIdCita(rutP, id_medico, dia, mes, hora) != 0:
        print("cita ya existe, no se puede crear")
        return False
    else:
        id = obtener_ultimo_id(archivo_csv) + 1
        with open(archivo_csv, 'a', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerow(
                [id, rutP, nombreP, apellidoP, id_medico, dia, mes, hora])
            print("se creo cita")
            return True


def eliminarCita(parametros):
    archivo_csv = './DB/citas.csv'
    rutP, rutM, dia, mes, hora = obtenerParametrosEliminar(parametros)
    id_medico = obtenerIdMedico(rutM)
    id_cita = obtenerIdCita(rutP, id_medico, dia, mes, hora)

    if id_cita != 0:
        filas_a_mantener = []
        with open(archivo_csv, 'r') as archivo:
            csv_reader = csv.reader(archivo, delimiter='|')
            cita_encontrada = False
            for fila in csv_reader:
                if len(fila) > 2:
                    if fila[0] == id_cita:
                        cita_encontrada = True
                    else:
                        filas_a_mantener.append(fila)

        if cita_encontrada:
            with open(archivo_csv, 'w', newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter='|')
                csv_writer.writerows(filas_a_mantener)
            print("Se elimino cita")
            return True
        else:
            print("No se encontro cita")
            return False
    else:
        print("No se encontro cita")
        return False


def editarCita(parametros):
    archivo_csv = './DB/citas.csv'
    rutP, rutM, dia_antiguo, mes_antiguo, hora_antiguo, dia_nuevo, mes_nuevo, hora_nuevo = obtenerParametrosEditar(
        parametros)
    id_medico = 0

    if doctor_existe(rutM):
        id_medico = obtenerIdMedico(rutM)

    # buscar cita
    if obtenerIdCita(rutP, id_medico, dia_antiguo, mes_antiguo, hora_antiguo) == 0:
        # ==0 es porque no existe
        print("cita no existe, no se puede editar")
        return False
    else:
        id = obtenerIdCita(rutP, id_medico, dia_antiguo,
                           mes_antiguo, hora_antiguo)
        with open(archivo_csv, 'r', newline='') as archivo:
            csv_reader = csv.reader(archivo, delimiter='|')
            lineas = list(csv_reader)
            for fila in lineas:
                if len(fila) > 2 and fila[1] == rutP and fila[4] == id_medico and fila[5] == dia_antiguo and fila[6] == mes_antiguo and fila[7] == hora_antiguo:
                    fila[5] = dia_nuevo
                    fila[6] = mes_nuevo
                    fila[7] = hora_nuevo

            # Abre el archivo de nuevo en modo escritura y escribe las líneas editadas
            with open(archivo_csv, 'w', newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter='|')
                csv_writer.writerows(lineas)
                print("Se editó la cita")
                return True


parametros = "1100-Juan Luis-Perez Gonzalez-1000-23-18-13:00"
eliminar = "1100-1000-23-08-13:00"
# print(obtenerParametros(parametros))
crearCita(parametros)
eliminarCita(eliminar)
# parametros_editar = "1100-1000-23-08-13:00-30-10-14:00"
# print(obtenerParametrosEditar(parametros_editar))
# editarCita(parametros_editar)
# print(obtenerParametrosEliminar(eliminar))


# id , medico_id, paciente_id, dia, mes, hora, estado, monto

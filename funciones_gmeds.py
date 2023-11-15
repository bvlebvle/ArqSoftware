import csv


def doctor_existe(rut):
    archivo_csv = './DB/medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:

            if len(fila) > 2 and fila[1] == rut:
                return True
    return False


def obtenerIdMedico(rut):
    archivo_csv = './DB/medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == rut:
                return fila[0]
    return 0


def obtenerParametros(parametros):
    pos_caracter = []
    for i in range(0, len(parametros)):
        if parametros[i] == '-':
            pos_caracter.append(i)

    rut = parametros[0:pos_caracter[0]]
    nombre = parametros[pos_caracter[0]+1:pos_caracter[1]].upper()
    apellido = parametros[pos_caracter[1]+1:pos_caracter[2]].upper()
    especialidad = parametros[pos_caracter[2]+1:].upper()
    return rut, nombre, apellido, especialidad


def obtener_ultimo_id(archivo_csv):
    # archivo_csv = 'horarios.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 0:
                ultimo_id = fila[0]

        if ultimo_id == "id":
            return 0
        else:
            return int(ultimo_id)


def crearMedico(parametros):
    archivo_csv = './DB/medicos.csv'
    rut, nombre, apellido, especialidad = obtenerParametros(parametros)
    ultimo_id = obtener_ultimo_id(archivo_csv)

    # Verificar si el médico ya existe
    if doctor_existe(rut):
        return False
    else:
        # Agregar el médico al archivo CSV
        nuevo_id = ultimo_id + 1
        with open(archivo_csv, 'a', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerow(
                [nuevo_id, rut, nombre, apellido, especialidad])

            print(f"Se ha agregado al médico {nombre} {apellido} al archivo.")
            return True


def eliminarMedico(rut):
    archivo_csv = './DB/medicos.csv'

    id = obtenerIdMedico(rut)

    if doctor_existe(rut):
        filas_a_mantener = []
        with open(archivo_csv, 'r') as archivo:
            csv_reader = csv.reader(archivo, delimiter='|')
            medico_encontrado = False
            for fila in csv_reader:
                # verifica si hay algo en la fila
                if len(fila) > 2:
                    if fila[0] == id:
                        medico_encontrado = True
                    else:
                        filas_a_mantener.append(fila)

        if medico_encontrado:
            with open(archivo_csv, 'w', newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter='|')
                csv_writer.writerows(filas_a_mantener)
            print(f"El médico ha sido eliminado del archivo.")
            return True
        else:
            print(f"El médico no existe en el archivo.")
            return False
    else:
        print(f"El médico no existe en el archivo.")
        return False


def editarMedico(parametros):
    rut, nombre, apellido, especialidad = obtenerParametros(parametros)

    if doctor_existe(rut):
        eliminarMedico(rut)
        crearMedico(parametros)
        print(f"El médico {nombre} {apellido} ha sido editado.")
        return True
    else:
        print(f"El médico {nombre} {apellido} no existe en el archivo.")
        return False


parametros = "123456789-Juan-Perez-Traumatologia"
crearMedico(parametros)

import csv
def verificar_y_agregar_columna_box(archivo_medicos):
    filas_modificadas = []
    columna_box_existe = False

    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        encabezado = next(csv_reader)  # Obtener el encabezado

        if 'box' in encabezado:
            columna_box_existe = True
            filas_modificadas.append(encabezado)
        else:
            encabezado.append('box')
            filas_modificadas.append(encabezado)

        for fila in csv_reader:
            if not columna_box_existe:
                fila.append('')  # Agrega un campo vacío para 'box'
            filas_modificadas.append(fila)

    if not columna_box_existe:
        with open(archivo_medicos, 'w', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerows(filas_modificadas)
        return True

    return False

def asignar_sala(parametros, archivo_medicos='./DB/medicos.csv'):
    parametros = parametros.split('-')
    rut = parametros[0]
    sala_id = parametros[1]

    nueva_columna_agregada = verificar_y_agregar_columna_box(archivo_medicos)
    cambios_realizados = False

    filas_modificadas = []
    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == rut:
                if len(fila) < 6 or nueva_columna_agregada:  # Asume que 'box' es la sexta columna
                    fila.append(sala_id)  # Agrega 'box' si no existe
                else:
                    fila[5] = sala_id  # Actualiza 'box' si ya existe
                cambios_realizados = True
            filas_modificadas.append(fila)

    if cambios_realizados:
        with open(archivo_medicos, 'w', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerows(filas_modificadas)

    return cambios_realizados



def obtener_ultimo_id(archivo_csv):
    ultimo_id = 0
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila and fila[0].isdigit():
                id_actual = int(fila[0])
                if id_actual > ultimo_id:
                    ultimo_id = id_actual
    return ultimo_id

def crear_sala(parametro, archivo_csv='./DB/salas_atencion.csv'):
    parametro = parametro.split('-')
    numero_sala = parametro[0]
    piso = parametro[1]
    ultimo_id = obtener_ultimo_id(archivo_csv)
    nuevo_id = ultimo_id + 1
    nueva_sala = [nuevo_id, numero_sala, piso]
    print ("la nueva sala es: ",nueva_sala)
    with open(archivo_csv, 'a', newline='') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerow(nueva_sala)
    return True

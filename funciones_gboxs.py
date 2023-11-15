import csv

def verificar_y_agregar_columna_box(archivo_medicos='./DB/medicos.csv'):
    filas_modificadas = []
    columna_existente = False
    
    # Leer el contenido existente y verificar la presencia de la columna "box"
    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        encabezados = next(csv_reader)  # Asumiendo que la primera fila son encabezados
        if 'box' in encabezados:
            columna_existente = True
            return columna_existente  # No es necesario hacer más si la columna ya existe
        else:
            encabezados.append('box')
            filas_modificadas.append(encabezados)  # Agregar los encabezados actualizados

        for fila in csv_reader:
            fila.append('')  # Agregar un valor vacío para la nueva columna "box"
            filas_modificadas.append(fila)

    # Escribir los datos de nuevo, incluyendo la nueva columna si fue necesaria
    with open(archivo_medicos, 'w', newline='') as archivo:
        csv_writer = csv.writer(archivo, delimiter='|')
        csv_writer.writerows(filas_modificadas)
    
    return not columna_existente  

def asignar_sala(parametros, archivo_medicos='./DB/medicos.csv'):
    # Primero, verificar y agregar la columna "box" si no existe
    parametros = parametros.split('-')
    rut = parametros[0]
    sala_id = parametros[1]
    print("el rut es: ",rut," y la sala es: ",sala_id)
    nueva_columna_agregada = verificar_y_agregar_columna_box(archivo_medicos)
    print ("la nueva columna fue agregada: ",nueva_columna_agregada)
    filas_modificadas = []
    cambios_realizados = False
    
    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == rut:
                if nueva_columna_agregada or ('box' in fila):
                    # Asumiendo que la última columna es 'box'
                    fila[-1] = sala_id
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

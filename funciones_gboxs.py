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
    parametros = parametros.split('-')
    rut = parametros[0] + "-" + parametros[1]
    sala_id = parametros[2]

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

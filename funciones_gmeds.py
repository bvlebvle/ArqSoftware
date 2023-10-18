import csv
def doctor_existe(nombre, apellido, especialidad):
    archivo_csv = 'medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            
            if len(fila) > 2 and fila[1] == nombre and fila[2] == apellido and fila[3] == especialidad:
                return True
    return False

def obtenerIdMedico(nombre, apellido, especialidad):
    archivo_csv = 'medicos.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == nombre and fila[2] == apellido and fila[3] == especialidad:
                return fila[0]
    return 0
    
def obtenerParametros(parametros):
    pos_caracter = []
    for i in range(0, len(parametros)):
        if parametros[i] == '-':
            pos_caracter.append(i)
    
    nombre = parametros[0:pos_caracter[0]]
    apellido = parametros[pos_caracter[0]+1:pos_caracter[1]]
    especialidad = parametros[pos_caracter[1]+1:]
    return nombre, apellido, especialidad

def dataEditarMedico(parametros):
    cont = 0; 
    for i in range(0, len(parametros)):
        if parametros[i] == '-':
            cont += 1
        if cont == 3:
            antiguo = parametros[0:i]
            nuevo = parametros[i+1:]
            break
    
    return antiguo, nuevo
			
def obtener_ultimo_id(archivo_csv):
    #archivo_csv = 'horarios.csv'
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
    archivo_csv = 'medicos.csv'
    nombre, apellido, especialidad = obtenerParametros(parametros)
    ultimo_id = obtener_ultimo_id(archivo_csv)
    
    # Verificar si el médico ya existe
    if doctor_existe(nombre, apellido, especialidad):
        #print(f"El médico {nombre} {apellido} ya existe en el archivo.")
        return False
    else:
        # Agregar el médico al archivo CSV
        nuevo_id = ultimo_id + 1
        with open(archivo_csv, 'a', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerow([nuevo_id, nombre, apellido, especialidad])
            
            #print(f"Se ha agregado al médico {nombre} {apellido} al archivo.")
            return True
            
            
def eliminarMedico(parametros):
    archivo_csv = 'medicos.csv'
    nombre, apellido, especialidad = obtenerParametros(parametros)
    id = obtenerIdMedico(nombre, apellido, especialidad)
    
    if doctor_existe(nombre, apellido, especialidad):
        filas_a_mantener = []
        with open(archivo_csv, 'r') as archivo:
            csv_reader = csv.reader(archivo, delimiter='|')
            medico_encontrado = False
            for fila in csv_reader:
                #verifica si hay algo en la fila
                if len(fila) > 2: 
                    if fila[0] == id:
                        medico_encontrado = True
                    else:
                        filas_a_mantener.append(fila)

        if medico_encontrado:
            with open(archivo_csv, 'w', newline='') as archivo:
                csv_writer = csv.writer(archivo, delimiter='|')
                csv_writer.writerows(filas_a_mantener)
            #print(f"El médico {nombre} {apellido} ha sido eliminado del archivo.")
            return True
        else:
            #print(f"El médico {nombre} {apellido} no existe en el archivo.")
            return False
    else:
        #print(f"El médico {nombre} {apellido} no existe en el archivo.")
        return False

def editarMedico(parametros): 
    parametros_antiguos, parametros_nuevos = dataEditarMedico(parametros)
    nombre_antiguo, apellido_antiguo, especialidad_antiguo = obtenerParametros(parametros_antiguos)   
    
    if doctor_existe(nombre_antiguo, apellido_antiguo, especialidad_antiguo):
        eliminarMedico(parametros_antiguos)
        crearMedico(parametros_nuevos)
        print(f"El médico {nombre_antiguo} {apellido_antiguo} ha sido editado.")
        return True
    else:
        print(f"El médico {nombre_antiguo} {apellido_antiguo} no existe en el archivo.")
        return False


data = "paula-nunez-general"
data2 = "martin-saavedra-general"
data3 = "valentina-diaz-general"

crearMedico(data)
crearMedico(data2)
crearMedico(data3)
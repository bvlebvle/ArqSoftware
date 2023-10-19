from funciones_gmeds import *
from funciones_crhor import *

def obtenerParametros(data):
    #nombreP-apellidoP-nombreM-ApellidoM-especialidad-dia-mes-hora
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            pos_caracter.append(i)
    nombreP = data[0:pos_caracter[0]]
    apellidoP = data[pos_caracter[0]+1:pos_caracter[1]]
    nombreM = data[pos_caracter[1]+1:pos_caracter[2]]
    apellidoM = data[pos_caracter[2]+1:pos_caracter[3]]
    especialidad = data[pos_caracter[3]+1:pos_caracter[4]]
    dia = data[pos_caracter[4]+1:pos_caracter[5]]
    mes = data[pos_caracter[5]+1:pos_caracter[6]]
    hora = data[pos_caracter[6]+1:]
    return nombreP, apellidoP, nombreM, apellidoM, especialidad, dia, mes, hora

def obtenerParametrosEditar(data):
    #nombreP-apellidoP-nombreM-ApellidoM-especialidad-dia-mes-hora-diaNuevo-mesNuevo-horaNueva
    cont = 0; 
    pos_caracter = []
    for i in range(0, len(data)):
        if data[i] == '-':
            cont += 1
        if cont == 8:
            antiguo = data[0:i]
            nuevo = data[i+1:]
            break
    
    for i in range (0, len(nuevo)):
        if nuevo[i] == '-':
            pos_caracter.append(i)
    dia_nuevo = nuevo[:pos_caracter[0]]
    mes_nuevo = nuevo[pos_caracter[0]+1:pos_caracter[1]]
    hora_nuevo = nuevo[pos_caracter[1]+1:]
    
    return antiguo, dia_nuevo, mes_nuevo, hora_nuevo


def obtenerIdCita(id_medico,nombreP, apellidoP, dia, mes, hora):
    archivo_csv = 'citas.csv'
    with open(archivo_csv, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if len(fila) > 2 and fila[1] == id_medico and fila[2] == nombreP and fila[3] == apellidoP and fila[4] == dia and fila[5] == mes and fila[6] == hora:
                return fila[0]
        return 0 

       
def crearCita(parametros): 
    archivo_csv = 'citas.csv'
    nombreP, apellidoP, nombreM, apellidoM, especialidad, dia,mes,hora = obtenerParametros(parametros)
    id_medico = 0
    
    if doctor_existe(nombreM, apellidoM, especialidad):
        id_medico = obtenerIdMedico(nombreM, apellidoM, especialidad)
    
    #buscar cita
    if obtenerIdCita(id_medico,nombreP, apellidoP, dia, mes, hora) != 0:
        print("cita ya existe, no se puede crear")
        return False
    else: 
        id = obtener_ultimo_id(archivo_csv) + 1
        with open(archivo_csv, 'a', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerow([id, id_medico, nombreP, apellidoP, dia, mes, hora])
            print("se creo cita")
            return True
        
        
def eliminarCita(parametros):
    archivo_csv = 'citas.csv'
    nombreP, apellidoP, nombreM, apellidoM, especialidad, dia,mes,hora = obtenerParametros(parametros)
    id_medico = 0
    
    if doctor_existe(nombreM, apellidoM, especialidad):
        id_medico = obtenerIdMedico(nombreM, apellidoM, especialidad)
    
    #buscar cita
    if obtenerIdCita(id_medico,nombreP, apellidoP, dia, mes, hora) == 0:
        #==0 es porque no existe
        print("cita no existe, no se puede eliminar")
    else: 
        id = obtenerIdCita(id_medico,nombreP, apellidoP, dia, mes, hora)
        with open(archivo_csv, 'r') as archivo:
            csv_reader = csv.reader(archivo, delimiter='|')
            lineas = list(csv_reader)
            lineas.pop(int(id))
        with open(archivo_csv, 'w', newline='') as archivo:
            csv_writer = csv.writer(archivo, delimiter='|')
            csv_writer.writerows(lineas)
            print("se elimino cita")
    
    
def editarCita(parametros):
    archivo_csv = 'citas.csv'
    antiguo, dia_nuevo, mes_nuevo, hora_nuevo = obtenerParametrosEditar(parametros)
    nombreP, apellidoP, nombreM, apellidoM, especialidad, dia,mes,hora = obtenerParametros(antiguo)
    if doctor_existe(nombreM, apellidoM, especialidad):
        id_medico = obtenerIdMedico(nombreM, apellidoM, especialidad)
    #buscar cita
    if obtenerIdCita(id_medico,nombreP, apellidoP, dia, mes, hora) == 0:
        #==0 es porque no existe
        print("cita no existe, no se puede editar")
    else: 
        eliminarCita(antiguo)
        crearCita(nombreP+"-"+apellidoP+"-"+nombreM+"-"+apellidoM+"-"+especialidad+"-"+dia_nuevo+"-"+mes_nuevo+"-"+hora_nuevo)

    

parametros = "Juan Luis-Perez Gonzalez-martin-saavedra-general-23-08-13:00"
#print(obtenerParametros(parametros))
crearCita(parametros)
#eliminarCita(parametros)
parametros_editar = "Juan Luis-Perez Gonzalez-martin-saavedra-general-23-08-13:00-25-10-14:00"   
#print(obtenerParametrosEditar(parametros_editar))
editarCita(parametros_editar)


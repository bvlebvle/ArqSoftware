import csv

def obtenerIDMedico(rut, archivo_medicos='./DB/medicos.csv'):
    with open(archivo_medicos, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        for fila in csv_reader:
            if fila[1] == rut:
                return fila[0]  # Retorna el ID del médico
    return None  # Retorna None si no encuentra el RUT

def bloquearHoras(parametros, archivo_horarios='./DB/horarios.csv'):
    divido = parametros.split("-")
    rut = divido[0]
    dia = divido[1]
    horaInicio = divido[2]
    print
    id_medico = obtenerIDMedico(rut)
    if id_medico is None:
        print("No existe medico")
        return False

    with open(archivo_horarios, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        horarios = list(csv_reader)
        
    for horario in horarios:
        if horario[0] == id_medico and horario[1] == dia and horario[2] == horaInicio:
            if horario[3] == 'False':
                return False
            else:
                horario[3] = 'False'
                with open(archivo_horarios, 'w', newline='') as archivo_actualizado:
                    csv_writer = csv.writer(archivo_actualizado, delimiter='|')
                    csv_writer.writerows(horarios)
                return True
    
    return "Primero debe agregar bloque"
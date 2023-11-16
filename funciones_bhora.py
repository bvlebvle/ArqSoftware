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
        print("Médico no encontrado.")
        return f"Medico no encontrado"

    with open(archivo_horarios, 'r') as archivo:
        csv_reader = csv.reader(archivo, delimiter='|')
        horarios = list(csv_reader)
        
    for horario in horarios:
        if horario[1] == id_medico and horario[2] == dia and horario[3] == horaInicio:
            if horario[3] == 'False':
                return "Este bloque ya está bloqueado"
            else:
                horario[5] = 'False'
                with open(archivo_horarios, 'w', newline='') as archivo_actualizado:
                    csv_writer = csv.writer(archivo_actualizado, delimiter='|')
                    csv_writer.writerows(horarios)
                return "Bloqueado correctamente"
    
    return "Primero debe agregar bloque"
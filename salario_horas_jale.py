print("este es un programa en python")
mensaje_entrada = "Ingresa la hora de entrada del dia"
mensaje_salida = "Introduce la hora de salida"
mensaje_minutos = "introduce sus minutos"
i = 0
semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
def todo_cero():
    minutos_total = 0
    minutos_porcentaje = 0
    hora_salida = 0
    horas_total = 0
    hora_total_dia = 0

while True:
    
    dia_semana = semana[i]
    if dia_semana == 'domingo':
        print("Domingo no se trabaja, es pecado mortal!")
        break
    todo_cero()
    hora_entrada = input(f"{mensaje_entrada} {dia_semana.title()}: ")
    minutos_entrada = input(f"{mensaje_minutos}: ")
    hora_entrada = int(hora_entrada)
    minutos_entrada = int(minutos_entrada)
    print("\n")
    print(f"La hora es: {hora_entrada}:{minutos_entrada}")

    hora_salida = input(f"{mensaje_salida}: ")
    minutos_salida = input(f"{mensaje_minutos}: ")
    hora_salida = int(hora_salida)
    minutos_salida = int(minutos_salida)
    print("\n")
    print(f"La hora es: {hora_salida}:{minutos_salida}")

    minutos_total = -minutos_entrada + minutos_salida
    minutos_porcentaje = minutos_total * 100 / 60
    minutos_porcentaje = minutos_porcentaje / 100
    
    if hora_salida == 12:
        lonche = 0
    else:
        hora_salida = hora_salida + 12
        lonche = .5
        
    horas_total = hora_salida - hora_entrada

    hora_total_dia = horas_total + minutos_porcentaje - lonche

    print("\n")
    print(f"el total de ese dia es: {hora_total_dia}")
    i = i + 1

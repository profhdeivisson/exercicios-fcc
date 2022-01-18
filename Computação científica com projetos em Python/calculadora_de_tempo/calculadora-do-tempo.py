from datetime import datetime, timedelta, time, date

def add_time(horario_inicial, duracao, diaDaSemana=""):
    DAYS = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    ]
    
    if horario_inicial[-2:] == "AM": 
        horario_inicial = horario_inicial[:-2]
    elif horario_inicial[-2:] == "PM" and horario_inicial[:2] == "12": 
        horario_inicial = horario_inicial[:-2]
    else:
        hora = horario_inicial.split(":")
        if(len(hora[0]) == 2):
            horario_inicial = str(int(horario_inicial[:2]) + 12) + horario_inicial[2:5]
        else:
            horario_inicial = str(int(horario_inicial[:1]) + 12) + horario_inicial[1:5]

    d = duracao.split(":")
    dHoras = d[0]
    dMinutos = d[1]
    h = horario_inicial.split(":")
    hHoras = h[0]
    hMinutos = h[1]
    horario_final = timedelta(hours=int(hHoras) + int(dHoras), minutes=int(hMinutos) + int(dMinutos))
    if(len(str(horario_final).split()) == 1):
        horaDividida = str(horario_final).split(":")
        qtdDias = horaDividida[0].split()
        for dia in range(int(qtdDias[0])):
            DAYS.append(DAYS[dia])
        horaFormatada = time(hour=int(horaDividida[0]), minute=int(horaDividida[1])).strftime("%I:%M %p")
        if(int(horaFormatada[0:2]) < 10):
            horaFormatada = horaFormatada[1:]
        if(diaDaSemana != ""):
            return horaFormatada[0:]+", "+diaDaSemana.title()
        else:
            return horaFormatada[0:]
    elif(len(str(horario_final).split()) == 3):
        horaDividida = str(horario_final).split(',')
        horaFormatada = time(hour=int(horaDividida[1][1]), minute=int(horaDividida[1][3:5])).strftime("%I:%M %p")
        if(int(horaFormatada[0:2]) < 10):
            horaFormatada = horaFormatada[1:]
        if(horaDividida[0] == '1 day'):
            if(diaDaSemana != ""):
                qtdDias = horaDividida[0].split()
                for dia in range(int(qtdDias[0])):
                    DAYS.append(DAYS[dia])
                return horaFormatada[0:] + ", " + DAYS[DAYS.index(diaDaSemana.title()) + int(qtdDias[0])] + " (next day)"
            else:
                return horaFormatada[0:] + " (next day)"
        elif(int(horaDividida[0][0]) > 1):
            qtdDias = horaDividida[0].split()
            for dia in range(int(qtdDias[0])):
                DAYS.append(DAYS[dia])
            if(diaDaSemana != ""):
                return horaFormatada[0:]+", " + DAYS[DAYS.index(diaDaSemana.title()) + int(qtdDias[0])] + " (" + qtdDias[0] + " days later)"
            else:
                return horaFormatada[0:]+" (" + qtdDias[0] + " days later)"

print(add_time("8:16 PM", "466:02"))
print(add_time("11:35 PM", "1:32"))
print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
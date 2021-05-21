# format_duration(1), "1 second"
# format_duration(62), "1 minute and 2 seconds"
# format_duration(3662), "1 hour, 1 minute and 2 seconds"

# import datetime

def plural(n, word):
    if n == 1:
        return '%d %s' % (n, word)
    return '%d %ss' % (n, word)

def format_duration(seconds):
    if seconds == 0: # nas outras soluções eu não havia pensando nisso, agora o 'agora' é suportado
        return "now"
    
    # variáveis de unidades do tempo
    oneMinute = 60
    oneHour = 60 * oneMinute
    oneDay = 24 * oneHour
    oneYear = 365 * oneDay

    # unidades do tempo e seus valores chave, 1 para segundo, pois ele é a referência na escala
    timeUnits = (
        (oneYear, 'year'),
        (oneDay, 'day'),
        (oneHour, 'hour'),
        (oneMinute, 'minute'),
        (1, 'second')
    )

    resultado = []

    # formatação e uso das ferramentas criadas anteriormente
    for unit in timeUnits:
        timeUnit, word = unit
        if seconds >= timeUnit:
            n = int(seconds / timeUnit)
            resultado.append(plural(n, word))
            seconds -= n * timeUnit
    return ' and'.join(', '.join(resultado).rsplit(',', 1))


    # primeira solução, não deu certo nos testes mais complexos
    # ---------------------------------------------------------
    # final = f"{str(datetime.timedelta(seconds=seconds))[0]} hours, {str(datetime.timedelta(seconds=seconds))[3:4]} minutes and {str(datetime.timedelta(seconds=seconds))[6:7]} seconds"

    # if int(str(datetime.timedelta(seconds=seconds))[0]) == 0:
    #     if int(str(datetime.timedelta(seconds=seconds))[3:4]) > 1 and int(str(datetime.timedelta(seconds=seconds))[6:7]) > 1:
    #         return f"{str(datetime.timedelta(seconds=seconds))[3:4]} minutes and {str(datetime.timedelta(seconds=seconds))[6:7]} seconds"
    #     elif int(str(datetime.timedelta(seconds=seconds))[3:4]) == 1 and int(str(datetime.timedelta(seconds=seconds))[3:4]) > 1:
    #         return f"{str(datetime.timedelta(seconds=seconds))[3:4]} minute and {str(datetime.timedelta(seconds=seconds))[6:7]} seconds"
    #     elif int(str(datetime.timedelta(seconds=seconds))[3:4]) > 1 and int(str(datetime.timedelta(seconds=seconds))[3:4]) == 1:
    #         return f"{str(datetime.timedelta(seconds=seconds))[3:4]} minutes and {str(datetime.timedelta(seconds=seconds))[6:7]} second"
    #     elif int(str(datetime.timedelta(seconds=seconds))[3:4]) == 1 and int(str(datetime.timedelta(seconds=seconds))[3:4]) == 1:
    #         return f"{str(datetime.timedelta(seconds=seconds))[3:4]} minute and {str(datetime.timedelta(seconds=seconds))[6:7]} second"
    # elif int(str(datetime.timedelta(seconds=seconds))[0]) == 0 and int(str(datetime.timedelta(seconds=seconds))[3:4]) == 0:
    #     if int(str(datetime.timedelta(seconds=seconds))[6:7]) > 1:
    #         return f"{int(str(datetime.timedelta(seconds=seconds))[6:7]) > 1} seconds"
    #     else:
    #         return f"{int(str(datetime.timedelta(seconds=seconds))[6:7]) > 1} second"

    # segunda solução, também não serve para valores complexos
    # -------------------------------------------------------- 
    # hoursVal = f"{str(datetime.timedelta(seconds=seconds))[0]} hours" if int(str(datetime.timedelta(seconds=seconds))[0]) > 1 else f""
    # hoursVal = f"{str(datetime.timedelta(seconds=seconds))[0]} hour" if int(str(datetime.timedelta(seconds=seconds))[0]) == 1 else f""
    # minutesVal = f"{str(datetime.timedelta(seconds=seconds))[3:4]} minutes" if int(str(datetime.timedelta(seconds=seconds))[3:4]) > 1 else f""
    # minutesVal = f"{str(datetime.timedelta(seconds=seconds))[3:4]} minute" if int(str(datetime.timedelta(seconds=seconds))[3:4]) == 1 else f""
    # secondsVal = f"{str(datetime.timedelta(seconds=seconds))[6:7]} seconds" if int(str(datetime.timedelta(seconds=seconds))[6:7]) > 1 else f""
    # secondsVal = f"{str(datetime.timedelta(seconds=seconds))[6:7]} second" if int(str(datetime.timedelta(seconds=seconds))[6:7]) == 1 else f""

    # return hoursVal, minutesVal, secondsVal

print(format_duration(1))
print(format_duration(62))

# 0:00:01
# 0123456
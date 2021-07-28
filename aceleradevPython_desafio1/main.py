from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666',
     'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097',
     'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097',
     'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788',
     'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788',
     'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099',
     'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697',
     'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099',
     'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697',
     'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097',
     'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788',
     'end': 1564627800, 'start': 1564626000}
]


def calculo_ligacao(inicio, fim):
    hora_inicio = datetime.fromtimestamp(inicio).hour  # Hora do inicio da ligação
    seg_inicio = datetime.fromtimestamp(inicio).second  # Segundos do inicio da ligação
    min_inicio = datetime.fromtimestamp(inicio).minute  # Minutos do inicio da ligação
    minutos_inicio = hora_inicio*60 + min_inicio

    hora_fim = datetime.fromtimestamp(fim).hour  # Recebe a hora do final da ligação
    seg_fim = datetime.fromtimestamp(fim).second  # Recebe o segundo do final da ligação
    min_fim = datetime.fromtimestamp(fim).minute  # Minutos do final da ligação
    minutos_fim = hora_fim*60 + min_fim

    minutos = minutos_fim - minutos_inicio # Minutos totais da ligação
    if seg_fim < seg_inicio:
        # Testa pela quantidade de segundos se foi um minuto completo
        minutos = minutos - 1

    # Calculando o valor da fatura
    LIMITE_DIURNO = 1320  # Equivale ao horario 22*60, serve para a taxa
    LIMITE_NOTURNO = 360  # Equivale ao horario 6*60, serve para a taxa
    if hora_inicio >= 6 and hora_inicio <= 22:
        if hora_fim > 22 and hora_fim < 6:
            # Calcula taxas diurnas
            minutos_diurno = LIMITE_DIURNO - minutos_inicio
            valor = 0.36 + 0.09*minutos_diurno + 0.36
        valor = 0.36 + 0.09*minutos
    elif ((hora_inicio > 22 and hora_inicio <= 23) or
          (hora_inicio >= 0 and hora_inicio < 6)):
        if hora_fim >= 6 and hora_fim <= 22:
            # Calcular taxas noturnas
            minutos_noturno = LIMITE_NOTURNO - minutos_inicio
            valor = 0.36 + 0.09 * minutos_noturno + 0.36
        valor = 0.36
    valor_total = round(valor, 2)
    return valor_total


def classify_by_phone_number(records):
    fatura = []
    fatura_aux = {}
    for i in range(len(records)):
        contador = 0
        if not fatura:  # Verifica se está vazio
            valor = calculo_ligacao(records[0]['start'], records[0]['end'])
            fatura_aux['source'] = records[0]['source']
            fatura_aux['total'] = valor
            fatura.append(fatura_aux.copy())
        else:
            for j in range(len(fatura)):
                if fatura[j]['source'] == records[i]['source']:
                    valor = calculo_ligacao(records[i]['start'],
                                            records[i]['end'])
                    fatura[j]['total'] = round(fatura[j]['total'] + valor, 2)
                else:
                    contador = contador + 1  # Vai servir no próximo if
            if contador == len(fatura):
                # Se entrou aqui significa que não foi adicionado antes
                valor = calculo_ligacao(records[i]['start'], records[i]['end'])
                fatura_aux['source'] = records[i]['source']
                fatura_aux['total'] = valor
                fatura.append(fatura_aux.copy())
        fatura_aux.clear()
    return sorted(fatura, key=lambda i: i['total'],
                  reverse=True)
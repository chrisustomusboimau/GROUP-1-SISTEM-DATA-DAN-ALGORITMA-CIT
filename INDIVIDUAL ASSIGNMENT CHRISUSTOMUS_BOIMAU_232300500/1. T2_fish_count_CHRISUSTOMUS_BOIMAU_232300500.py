"""
T2 - FISH COUNT

NAMA = CHRISUSTOMUS BOIMAU
NIM  = 232300500
"""

import random

def cek_sensor_rusak(data):
    jam_rusak = "tidak ada"
    for i in range(len(data)):
        if data[i][1] == -1:
            jam_rusak = i
    return jam_rusak

def sensor_ikan():
    data = []
    for i in range(24):
        data.append([f'{str(i).zfill(2)}.00',random.randint(0,100)])

    sensor_rusak = random.randint(1,22)
    data[sensor_rusak][1] = -1

    jam_sensor_rusak = cek_sensor_rusak(data)

    print(f"data sensor : \n\n {data}")
    print(f"\nsensor rusak pada jam {f'{str(jam_sensor_rusak).zfill(2)}.00'}\n")

    data[jam_sensor_rusak][1] = (data[jam_sensor_rusak-1][1]+data[jam_sensor_rusak+1][1])//2

    print(f"data sensor terbaru : \n\n{data}")
    return data

def jam_jumlah_ikan_paling_banyak(data):
    max = data[0][1]
    hour = 0
    for i in range(len(data)-1):
        if data[i][1] > max:
            max = data[i][1]
            hour = i
    return hour

def jam_jumlah_ikan_paling_sedikit(data):
    min = data[0][1]
    hour = 0
    for i in range(len(data)-1):
        if data[i][1] < min:
            max = data[i][1]
            hour = i
    return hour

data = sensor_ikan()
jam_ikan_terbanyak = jam_jumlah_ikan_paling_banyak(data)
print(f"\njam dimana ikan paling banyak lewat ada di jam {data[jam_ikan_terbanyak][0]} dengan jumlah {data[jam_ikan_terbanyak][1]}")

jam_ikan_terdikit = jam_jumlah_ikan_paling_sedikit(data)
print(f"\njam dimana ikan paling sedikit lewat di jam {data[jam_ikan_terdikit][0]} dengan jumlah {data[jam_ikan_terdikit][1]}")
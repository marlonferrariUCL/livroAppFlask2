import requests

def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def loadDados():
    dados = requests.get('https://raw.githubusercontent.com/grovina/assisnet/master/casmurro.txt').text
    indice = {}
    for cap in range(1, 149):
        rom_cap_inicio = int_to_Roman(cap)
        rom_cap_fim = int_to_Roman(cap + 1)
        #print(rom_cap_inicio + '>>' + rom_cap_fim)
        if cap == 1:
            capitulo = dados.split('\n' + rom_cap_inicio)[0].split('\n' + rom_cap_fim)[0]
        else:
            capitulo = dados.split('\n' + rom_cap_inicio)[1].split('\n' + rom_cap_fim)[0]
        indice['CAP: ' + rom_cap_inicio + ' >> ' + capitulo.replace('\n', '').replace('\r', '')[0:20].split('.')[0]] = \
            capitulo.replace('\n', '<br>').replace('\r', '')
    return indice
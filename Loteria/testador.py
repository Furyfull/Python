import json

din = {'11': 6, '12': 12, '13': 30, '14': 2000, '15': 500000}
base = json.load(open('ultimos_14_jogos.txt', 'r'))
jogos = json.load(open('ww.txt', 'r'))
total = 0
gasto = 0
for resultado in base:
    ganho = 0
    for jogo in jogos:
        soma = sum(resultado.count(jogo[x]) for x in range(0, 15))
        if soma >= 11:
            ganho += din[f'{soma}']
    print(ganho)
    total += ganho
    gasto += 408*12
print('ganhou', total, 'gastou', gasto, 'em', len(base), 'semanas')

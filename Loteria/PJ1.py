import random
import json


def cartela(numb, jog, numeros):
    assert isinstance(numb, dict)
    lst = []
    resposta = []
    for i in numb:
        lst.extend(int(i) for x in range(numb[i]))
    print(lst)
    # usar o Theme Draculo VSCode
    quant_de_numeros = numeros
    jogos = jog

    for jogo in range(1, jogos + 1):
        while True:
            rnd = random.sample(lst, quant_de_numeros)
            # set gets unique elements
            if len(rnd) == len(set(rnd)):
                break

        rnd.sort()
        resposta += [rnd]
        print(resposta)


# ss = json.load(open('numeros_da_lotofacil.json', 'r'))
ss = "4rr"
cartela(ss, 3, 15)

import random
numb = {"1": 2, "2": 5, "5": 3, '4': 5}
lst = []
for i in numb:
    lst.extend(int(i) for x in range(numb[i]))
print(lst)
# usar o Theme Draculo VSCode
quant_de_numeros = 3
jogos = 3

for jogo in range(1, jogos+1):
    while True:
        rnd = random.sample(lst, quant_de_numeros)
        # set gets unique elements
        if len(rnd) == len(set(rnd)):
            break
    print(rnd)

testes

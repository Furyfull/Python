import random
numb = {"1": 2, "2": 5, "5": 3, '4': 5}
lst = []
for i in numb:
    # print(numb[i])
    lst.extend(int(i) for x in range(numb[i]))
print(lst)
jogo = 3
while True:
    rnd = random.sample(lst, jogo)
    # set gets unique elements
    if len(rnd) == len(set(rnd)):
        break
print(rnd)


import random
import os
import time

deck = {'A': 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


def hand_value(cards):
    value = sum(deck[card] for card in cards)
    for _ in range(cards.count("A")):
        if value <= 11:
            value += 10
        else:
            break
    return value


def dealer_action(mao):
    os.system("cls")
    mao.remove('??')
    # print("Dealer:", mao, hand_value(mao))
    time.sleep(1)
    while True:
        if hand_value(mao) >= 17:
            break
        else:
            print("Dealer:", mao, hand_value(mao))
            mao += random.choices(list(deck.keys()), k=1)
            time.sleep(1)
    return mao


def player_action(mao, mesa):
    while hand_value(mao) < 21:
        com = input("Fica (f) ou Para (p)? ")
        com.islower()
        if com == 'f':
            os.system("cls")
            mao += random.choices(list(deck.keys()), k=1)
            print("Dealer:", mesa, "\nMinha :", mao, hand_value(mao))
        elif com == 'p':
            print('Parei')
            time.sleep(1)

            break
    return mao


while True:
    # Inicio do Jogo
    hand = random.choices(list(deck.keys()), k=2)
    dealer = random.choices(list(deck.keys()), k=1) + ["??"]
    print("Dealer:", dealer, "\nMinha :", hand, hand_value(hand))

    # ações
    hand = player_action(hand, dealer)
    time.sleep(1.5)
    dealer = dealer_action(dealer)

    # Resultado
    print("Dealer:", dealer, hand_value(dealer), "\nMinha :", hand, hand_value(hand))
    if hand_value(hand) == 21:
        print("!!!!! BLACKJACK !!!!!")
    elif (hand_value(dealer) < hand_value(hand) < 21) or hand_value(dealer) > 21:
        print("Parabéns Você Ganhou !!!")
    elif hand_value(dealer) == hand_value(hand):
        print("Quase, Jogo Resultou Em Empate")
    else:
        print("#####   Você Perdeu   #####")
    input("")

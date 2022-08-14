def bank(card):
    print('*' * len(card[:-4]) + card[-4:])
bank(card=input("Введите номер карты:"))

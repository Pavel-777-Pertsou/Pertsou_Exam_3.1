slovo = str(input("VVedite slovo: "))
x = len(slovo)
i = 0
x = x - 1
k = 0
while x - i >= i:
    if slovo[x - i] == slovo[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("Слово не является палиндромом")
else:
  print("Слово палиндром")


#Метод решения №2
def palindrom(text):
    text = text.replace(' ', '').lower()
    if text == text[::-1]:
        return 'Палиндром'
    else:
        return 'Не палиндром'


def main():
    while True:
        slovo = input("Vvedite slovo: ")
        print(palindrom(slovo))


main()
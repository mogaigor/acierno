#ciao
lista = []
def aggiunta():
    x = input("scegli cosa aggiungere alla lista: ")
    lista.append(x)
def elimina():
    x = int(input("inserisci il prodotto da rimuovere: "))
    lista.pop(x - 1)
def visualizza():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
def conta():
    print("nella lista ci sono ",len(lista)," elementi.")
def svuota():
    lista.clear()

while True:
    comando = int(input("scegli un opzione tra quelle definite sopra: "))
    if comando == 1:
        aggiunta()
    elif comando == 2:
        elimina()
    elif comando == 3:
        visualizza()
    elif comando == 4:
        conta()
    elif comando == 5:
        svuota()
    elif comando == 6:
        break
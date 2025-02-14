inventario = {

    0 : {"nome": "Il PC di ...", "quantità": 1, "prezzo": 3999},
    1 : {"nome": "Nintendo Switch 2", "quantità": 10, "prezzo": 449},
    2 : {"nome": "GTA VI", "quantità": 3, "prezzo": 100}
}
def aggiunta():
    len(inventario) + 1
    nome = input("inserisci il nome: ")
    quantita = int(input("inserisci la quantita: "))
    prezzo = int(input("inserisci il prezzo: "))
    inventario[len(inventario)] = {"nome": nome,"quantita": quantita,"prezzo": prezzo}
def mod_quan():
    mod_invent = int(input("scegli che studente modificare attraverso il suo indice: "))
    a = int(input("cosa vuoi mettere? "))
    classe[mod_invent].update({"quantità":a})
def mod_prez():
    mod_invent = int(input("scegli che studente modificare attraverso il suo indice: "))
    a = int(input("cosa vuoi mettere? "))
    classe[mod_invent].update({"prezzo":a})
def elimina():
    inventario.pop(int(input("inserisci il prodotto da rimuovere: ")))
    len(inventario) - 1
def visualizza():
    print(inventario)

while True:
    comando = int(input("scegli un opzione tra quelle definite sopra: "))
    if comando == 1:
        aggiunta()
    elif comando == 2:
        mod_quan()
    elif comando == 3:
        mod_prez()
    elif comando == 4:
        elimina()
    elif comando == 5:
        visualizza()
    elif comando == 6:
        break
lista_spesa=[]
def aggiungi_elemento():
    messaggio=input("aggiungi: ")
    lista_spesa.append(messaggio)

def visualizza():
    for i in range(len(lista_spesa)):
        print(f"{i + 1}. {lista_spesa[i]}")


def elimina_elemento():
    valore = int(input("inserisci l'elemento da eliminare: "))
    lista_spesa.pop(valore-1)
    print("oggetto eliminato correttamente")

def messaggi():
    print("premere 1 per aggiungere alla lista")
    print("premere 2 per visualizzare la lista")
    print("premere 3 per eliminare un elemento della lista")
    print("premere 4 per pulire la lista")
    print("premere 5 per visualizzare quanti elementi ci sono nella lista")
    print("premi 0 per uscire")

def conta():
    print(len(lista_spesa))

def svuota_lista():
    lista_spesa.clear()




while True:
    messaggi()
    messaggio1= int(input("menù: "))
    if messaggio1 ==0:
        break
    elif messaggio1 == 1:
        aggiungi_elemento()
    elif messaggio1 == 2:
        visualizza()
    elif messaggio1 == 3:
        elimina_elemento()
    elif messaggio1 == 4:
        svuota_lista()
    elif messaggio1 == 5:
        conta()
    else:
        print("nessun valore indicato")
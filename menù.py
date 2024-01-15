from prettytable import PrettyTable



#menù iniziale
def main_menu():#(connessionedb)

    while True:
        print("\nBenvenuto\n\n--nome impianto--\n\n")
        print("1. Tutte le piste")
        print("2. Piste aperte")
        print("\n3. Esci")

        scelta = input("\nSeleziona un'opzione:\n-  ")

    ''' if scelta == "1":
            #
        elif scelta == "2":
            #
        elif scelta == "3":
            break
        else:
            print("\n--Scelta non valida.--\n")'''
    
#stampa risultato scelta 2
def visualizza_tutte_piste():

    #info dal db
    query= ...
    result = session.run(query)
    
    #creazione tabella e aggiunta risultati
    table = PrettyTable()
    table.field_names = ["Nome Pista", "Difficoltà", "Lunghezza"]

    for record in result:
        table.add_row([record["Nome"], record["Difficolta"], record["Lunghezza"]])

    #Visualizzazione
    print(table)
    input(print("\n1. Indietro\n-"))

    if input == "1":
        main_menu()
    else:
        print("\n--Scelta non valida--\n")


def visual_piste_aperte():
    

    


if __name__ == "__main__":
    main_menu()

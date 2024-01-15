from prettytable import PrettyTable
from neo4j import GraphDatabase
from colorama import Fore, Style



# Menù iniziale
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
    
# Stampa risultato scelta 2
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

#Aperto = Verde \ Chiuso = Rosso
def colora_stato(stato):
    if stato.lower() == 'aperto':
        return f"{Fore.GREEN}{stato}{Style.RESET_ALL}"
    elif stato.lower() == 'chiuso':
        return f"{Fore.RED}{stato}{Style.RESET_ALL}"
    else:
        return stato
    
# Stampa risultato scelta 3
def visual_piste_aperte():

    '''
    #info dal db
    query =
    result = session.run(query)
    '''

    #creazione tabella e aggiunta risultati
    table = PrettyTable()
    table.field_names = ["Nome Pista", "Difficoltà", "Stato"]

    for record in result:
         table.add_row([record["Nome"], record["Difficolta"], colora_stato(record["Stato"])])

    #Visualizzazione
    print(table)
    input(print("\n1. Indietro\n-"))

    if input == "1":
        main_menu()
    else:
        print("\n--Scelta non valida--\n")





if __name__ == "__main__":
    main_menu()

from Funzioni import Neo4jConnection, visualizza_piste, visualizza_punti, visualizza_impianti, calcola_percorso

from prettytable import PrettyTable
from colorama import Fore, Style


uri = "neo4j+s://f47961c0.databases.neo4j.io"
username = "neo4j"
password = "ZIm0yRYzEYFfUuC7pfJDqwfaQxaLVNl3FAL1oE5vfGA"

# Menù iniziale
def main_menu():

    while True:
        print("\nBenvenuto\n\n--nome impianto--\n\n")
        print("- 1. Tutte le piste")
        print("- 2. Piste aperte")
        print("- 3. Calcola percorso")
        print("\n- 4. Esci")

        scelta = input("\nSeleziona un'opzione:\n-  ")

        if scelta == "1":
            visualizza_piste(connection=connection)
        elif scelta == "2":
            visualizza_piste(connection=connection, aperte=True)
        elif scelta == "3":
            calcola_percorso(connection=connection)
        elif scelta == "4":
            break
        else:
            print("\n--Scelta non valida.--\n")



if __name__ == "__main__":
    with Neo4jConnection(uri, username, password) as connection:
        main_menu(connection)

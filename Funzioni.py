from neo4j import GraphDatabase
from prettytable import PrettyTable
from colorama import Fore

uri = "neo4j+s://f47961c0.databases.neo4j.io"
username = "neo4j"
password = "ZIm0yRYzEYFfUuC7pfJDqwfaQxaLVNl3FAL1oE5vfGA"

class Neo4jConnection:
    def __init__(self, uri, username, password):
        self._uri = uri
        self._username = username
        self._password = password
        self._driver = None

    def __enter__(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._username, self._password))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._driver is not None:
            self._driver.close()

    def run_query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            return list(result)

def visualizza_piste(connection, aperte=False):
    query = "MATCH ()-[r:PISTA]->() "
    if aperte:
        query += "WHERE r.aperta = true "
    query += "RETURN r"

    piste = connection.run_query(query)

    table = PrettyTable()
    table.title = 'PISTE'
    table.field_names = ["Nome", "Lunghezza", "Difficoltà", "Stato"]

    for pista in piste:
        nome = pista['r'].get('nome', 'N/A')
        lunghezza = pista['r'].get('lunghezza', 'N/A')
        difficolta = pista['r'].get('difficoltà', 'N/A')
        aperta = pista['r'].get('aperta', False)
        stato = Fore.GREEN + 'Aperta' + Fore.RESET if aperta else Fore.RED + 'Chiusa' + Fore.RESET
        colore = 'Blu' if difficolta == 1 else ('Rossa' if difficolta == 2 else 'Nera')

        table.add_row([nome, lunghezza, colore, stato])

    print(table)

def visualizza_punti(connection):
    lista_punti = []
    query = "MATCH (n) RETURN n"
    punti = connection.run_query(query)
    table_punti = PrettyTable()
    table_punti.title = 'PUNTI DISPONIBILI'
    table_punti.field_names = ["Idx", "Nome", "Tipologia"]

    for idx, punto in enumerate(punti, start=1):
        nome = punto['n'].get('nome', 'N/A')
        tipo = punto['n'].get('tipo', 'N/A')
        table_punti.add_row([idx, nome, tipo])
        lista_punti.append(nome)

    print(table_punti)
    return lista_punti

def visualizza_impianti(connection):
    query = "MATCH ()-[r:IMPIANTO]->() RETURN r"
    impianti = connection.run_query(query)
    print("Tutti gli impianti:")
    for impianto in impianti:
        nome = impianto['r'].get('nome', 'N/A')
        print(f"Nome: {nome}")


def calcola_percorso(connection):
    lista_punti = visualizza_punti(connection)
    while True:
        try:
            indice_partenza = int(input("\nInserisci il numero del punto di partenza:\n-  "))
            indice_arrivo = int(input("\nInserisci il numero del punto di arrivo:\n-  "))
            if 1 <= indice_partenza <= len(lista_punti) and 1 <= indice_arrivo <= len(lista_punti):
                break
            else:
                print("Inserisci indici validi.")
        except ValueError:
            print("Inserisci numeri validi.")

    punto_partenza = lista_punti[indice_partenza - 1]
    punto_arrivo = lista_punti[indice_arrivo - 1]

    query = (
        f"MATCH path = shortestPath((n1:Punto {{nome: '{punto_partenza}'}})-[*]->(n2:Punto {{nome: '{punto_arrivo}'}})) "
        "RETURN path"
    )
    percorsi = connection.run_query(query)

    for record in percorsi:
        path = record['path']
        print(f"\nPercorso:")
        for i in range(len(path.nodes) - 1):
            nodo_partenza = path.nodes[i]
            nodo_arrivo = path.nodes[i + 1]
            relazione = path.relationships[i]
            print(f"  - Da: {nodo_partenza['nome']}, A: {nodo_arrivo['nome']}, Pista: {relazione['nome']}")
        print()








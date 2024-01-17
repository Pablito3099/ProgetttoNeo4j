from neo4j import GraphDatabase

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
    for pista in piste:
        nome = pista['r'].get('nome', 'N/A')
        lunghezza = pista['r'].get('lunghezza', 'N/A')
        difficolta = pista['r'].get('difficoltà', 'N/A')
        colore = 'Blu' if difficolta == 1 else ('Rossa' if difficolta == 2 else 'Nera')
        print(f"Nome: {nome}, Lunghezza: {lunghezza}, Difficoltà: {colore}")

def visualizza_punti(connection):
    lista_punti = []
    query = "MATCH (n) RETURN n"
    punti = connection.run_query(query)
    for punto in punti:
        nome = punto['n'].get('nome', 'N/A')
        tipo = punto['n'].get('tipo', 'N/A')
        print(f"Nome: {nome}, Tipo: {tipo}")
        lista_punti.append(nome)
    return lista_punti

def visualizza_impianti(connection):
    query = "MATCH ()-[r:IMPIANTO]->() RETURN r"
    impianti = connection.run_query(query)
    for impianto in impianti:
        nome = impianto['r'].get('nome', 'N/A')
        print(f"Nome: {nome}")

def calcola_percorso(connection):
    lista_punti = visualizza_punti(connection)
    print("Punti disponibili:")
    for idx, nome in enumerate(lista_punti, start=1):
        print(f"{idx}. Nome: {nome}")
    while True:
        try:
            indice_partenza = int(input("Inserisci il numero del punto di partenza: "))
            indice_arrivo = int(input("Inserisci il numero del punto di arrivo: "))
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
        print(f"Percorso:")
        for i in range(len(path.nodes) - 1):
            nodo_partenza = path.nodes[i]
            nodo_arrivo = path.nodes[i + 1]
            relazione = path.relationships[i]
            print(f"  - Da: {nodo_partenza['nome']}, A: {nodo_arrivo['nome']}, Pista: {relazione['nome']}")
        print()

# Utilizzo della classe Neo4jConnection
with Neo4jConnection(uri, username, password) as connection:
    visualizza_piste(connection)
    visualizza_piste(connection, aperte=True)
    visualizza_punti(connection)
    visualizza_impianti(connection)
    calcola_percorso(connection)







from neo4j import GraphDatabase

# Configura la connessione al database Neo4j
uri = "neo4j+s://f47961c0.databases.neo4j.io"  # Sostituisci con il tuo URI
username = "neo4j"
password = "ZIm0yRYzEYFfUuC7pfJDqwfaQxaLVNl3FAL1oE5vfGA"

# Crea una classe per la gestione delle transazioni e della connessione
def visualizza_piste(query, connection):
    relationships = connection.run_query(query)
    # Stampa le proprietà delle relazioni
    for relationship in relationships:
        properties = relationship['r']
        nome = properties.get('nome', 'N/A')
        lunghezza = properties.get('lunghezza', 'N/A')
        difficolta = properties.get('difficoltà', 'N/A')
        print(f"Nome: {nome}, Lunghezza: {lunghezza}, Difficoltà: {difficolta}")

def visualizza_punti(query, connection):
    pass

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

# Utilizza la classe Neo4jConnection
with Neo4jConnection(uri, username, password) as connection:
    # Esempio di query per recuperare tutte le relazioni di tipo PISTA
    query = "MATCH ()-[r:PISTA]->() RETURN r"
    query2 = "MATCH (n) RETURN n"
    visualizza_piste(query=query, connection=connection)





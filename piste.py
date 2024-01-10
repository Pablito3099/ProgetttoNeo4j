from neo4j import GraphDatabase

class SkiApp:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def get_all_pistes_by_difficulty(self):
        with self._driver.session() as session:
            result = session.run("MATCH (p:Piste) RETURN p ORDER BY p.difficulty")
            return [record["p"] for record in result]

    def get_open_pistes(self):
        with self._driver.session() as session:
            result = session.run("MATCH (p:Piste {status: 'open'}) RETURN p")
            return [record["p"] for record in result]

    def find_shortest_path(self, start_piste, end_piste):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (start:Piste {name: $start}) "
                "MATCH (end:Piste {name: $end}) "
                "MATCH path = shortestPath((start)-[:CONNECTED_TO*]-(end)) "
                "RETURN path",
                start=start_piste,
                end=end_piste
            )
            return result.single()["path"]

    def find_easiest_path(self, start_piste, end_piste):
        # Implement logic to find the easiest path based on your criteria
        pass

# Esempio di utilizzo
uri = "bolt://localhost:7687"  # Modifica con il tuo URI Neo4j
user = "your_username"
password = "your_password"

app = SkiApp(uri, user, password)

# Ottieni tutte le piste in ordine di difficoltà
all_pistes_by_difficulty = app.get_all_pistes_by_difficulty()
print("Piste in ordine di difficoltà:")
for piste in all_pistes_by_difficulty:
    print(piste["name"], "-", piste["difficulty"])

# Ottieni solo le piste aperte
open_pistes = app.get_open_pistes()
print("\nPiste aperte:")
for piste in open_pistes:
    print(piste["name"])

# Trova il percorso più breve tra due punti
start_piste = "PisteA"
end_piste = "PisteB"
shortest_path = app.find_shortest_path(start_piste, end_piste)
print("\nPercorso più breve da", start_piste, "a", end_piste, ":", shortest_path)

# Trova il percorso più facile tra due punti
# Implementa la logica per trovare il percorso più facile

app.close()


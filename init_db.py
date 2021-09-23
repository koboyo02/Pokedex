import sqlite3

connection = sqlite3.connect("database.db")

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO pokedex (title, description, type, number) VALUES (?, ?, ?, ?)",
            ("Bulbizarre", "Il a une étrange graine plantée sur son dos. Elle grandit avec lui depuis la naissance.", "Plante/Poison", "001")
            )

cur.execute("INSERT INTO pokedex (title, description, type, number) VALUES (?, ?, ?, ?)",
            ("Herbizarre", "Son bulbe dorsal devient si gros qu'il ne peut plus se tenir sur ses membres postérieurs.", "Plante/Poison", "002")
            )

cur.execute("INSERT INTO pokedex (title, description, type, number) VALUES (?, ?, ?, ?)",
            ("Florizarre", "Sa plante mûrit en absorbant les rayons du soleil. Il migre souvent vers les endroits ensoleillés.", "Plante/Poison", "003")
            )

connection.commit()
connection.close()
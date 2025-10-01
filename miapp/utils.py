import csv
import os

def leer_clientes():
    """Lee los clientes desde clientes.csv y devuelve lista de diccionarios."""
    if not os.path.exists("clientes.csv"):
        return []
    try:
        with open("clientes.csv", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except Exception as e:
        print(f"Error leyendo clientes.csv: {e}")
        return []
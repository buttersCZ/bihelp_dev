import os
import logging
PATH = "db/bigquery"

def check_folder()-> bool:
    "Kontrola, zda-li jsme ve správné složce"
    if not os.path.exists(PATH):
        raise ValueError(f"Složka'{PATH}' neexistuje")
    return True


def get_sql_folders() -> list:
    "Získá všechny podsložky z db/bigquery, seřadí je abecedně"

    sub_dir = os.listdir(PATH)
    sub_dir.sort()

    return sub_dir
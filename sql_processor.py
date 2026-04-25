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

def process_sql_dir(dir, replacements) -> str:
    batch = ""
    for item in os.listdir(os.path.join(PATH, dir)):
        if item.endswith(".sql"):
            file_path = os.path.join(PATH, dir, item)
            with open(file_path, "r") as f:
                content = f.read()
                for rep in replacements:
                    content = content.replace(rep["from"],rep["to"])
                batch += f"--{file_path}/\n"+content
    return batch
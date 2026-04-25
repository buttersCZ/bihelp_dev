import logging
import os
import subprocess  

SQL_FILE_NAME = "batch_dev.sql"
BATCH_FILE_NAME = "deployment"


def generate_sql_file(batch: str):
    "Zápis do jednoho file"
    with open(SQL_FILE_NAME,"w") as f:
        f.write(batch)


def generate_batch_file(os_name: str):
    "Generování dávkového souboru"
    if os_name=="nt":
        run_dev_str="""
        @echo off
        echo Spouštím BigQuery dotazy...
        bq query --use_legacy_sql=false < batch_dev.sql
        pause
        """ 
        file_name = BATCH_FILE_NAME+".bat"
        with open(file_name, "w") as f:
            f.write(run_dev_str)
            logging.info(f"Soubor {file_name} vytvořen")
    else:
        run_dev_str="""
        #!/bin/bash
        echo \"Spouštím BigQuery dotazy...\"
        bq query --use_legacy_sql=false < batch_dev.sql
        """
        file_name = BATCH_FILE_NAME+".sh"
        with open(file_name, "w") as f:
            f.write(run_dev_str)
            os.chmod(file_name,0o755)
            logging.info(f"Soubor {file_name} vytvořen")
    pass
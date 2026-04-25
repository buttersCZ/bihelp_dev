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
        echo Log: %date% %time% >> run_dev.log

        REM Spusť BigQuery
        bq query --use_legacy_sql=false < batch_dev.sql >> run_dev.log 2>&1

        if %errorlevel% equ 0 (
            echo ✓ Dotazy byly úspěšně spuštěny >> run_dev.log
        ) else (
            echo ✗ Chyba při spuštění dotazů >> run_dev.log
        )

        echo.
        echo Stiskni libovolnou klávesu...
        pause
        """ 
        file_name = BATCH_FILE_NAME+".bat"
        with open(file_name, "w") as f:
            f.write(run_dev_str)
            logging.info(f"Soubor {file_name} vytvořen")
    else:
        run_dev_str="""
        #!/bin/bash
        echo "Spouštím BigQuery dotazy..."
        echo "Log: $(date)" >> run_dev.log

        # Spusť BigQuery
        bq query --use_legacy_sql=false < batch_dev.sql >> run_dev.log 2>&1

        if [ $? -eq 0 ]; then
            echo "✓ Dotazy byly úspěšně spuštěny" >> run_dev.log
        else
            echo "✗ Chyba při spuštění dotazů" >> run_dev.log
        fi

        echo ""
        echo "Log uložen v: run_dev.log"
        read -p "Stiskni Enter pro ukončení..."
        """
        file_name = BATCH_FILE_NAME+".sh"
        with open(file_name, "w") as f:
            f.write(run_dev_str)
            os.chmod(file_name,0o755)
            logging.info(f"Soubor {file_name} vytvořen")
    pass
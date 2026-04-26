
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
        
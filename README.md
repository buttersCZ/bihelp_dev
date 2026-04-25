# bihelp - BigQuery Deployment Tool

Nástroj pro automatizovaný deployment SQL scriptů do BigQuery s podporou nahrazování prostředí (dev/prod).

## Instalace

### Z .whl balíčku

```bash
pip install bihelp_development-1.0.0-py3-none-any.whl
```

### Ověření instalace

```bash
bihelp --help
```

## Použití

### 1. Inicializace konfigurace (poprvé)

```bash
bihelp --settings
```

Vytvoří šablonu `config.yaml`, kterou si upravíš podle svého prostředí.

### 2. Úprava config.yaml

Otevři `config.yaml` a nastav:
- `project`: BigQuery projekt
- `replacements`: Co se má nahradit (dev_project → prod_project)

Příklad:
```yaml
environments:
  dev:
    project: muj-dev-projekt
    replacements:
      - from: prod_project.core
        to: dev_project.core_dev
```

### 3. Spuštění deployment

```bash
bihelp --env dev
```

Vytvoří:
- `batch_dev.sql` - Všechny SQL dotazy dohromady
- `run_dev.sh` (Linux) nebo `run_dev.bat` (Windows) - Spustitelný skript

### 4. Spuštění skriptu v BigQuery

```bash
# Linux/Mac
./run_dev.sh

# Windows
run_dev.bat
```

## Struktura projektů

```
db/bigquery/
  01-create/
    *.sql
  02-insert/
    *.sql
  ...
```

Složky se zpracovávají abecedně.

## Požadavky

- Python 3.8+
- BigQuery CLI (`bq`) nainstalovaný a autorizovaný
- YAML config soubor

## Autorství

David Macák

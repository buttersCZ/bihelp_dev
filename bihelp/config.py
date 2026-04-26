
import logging
import yaml
import subprocess
import os

def load_config(path="config.yaml"):
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.error(f"Soubor '{path}' nenalezen!")
        raise ValueError(f"config.yaml neexistuje. Spusť nejdřív:\n  bihelp --settings")
    except yaml.YAMLError as e:
        logging.error(f"YAML je poškozený: {e}")
        raise ValueError(f"Soubor config má špatný formát: {e}")

def get_env(config, env_name):

    envs = config.get("environments", {})

    if env_name not in envs:
        raise ValueError(f"Environment '{env_name}' not found")
    return envs[env_name]

def check_bq_cli():
    """Kontrola, zda je bq CLI dostupný"""
    try:
        subprocess.run(["bq", "help"], capture_output=True, timeout=2)
        logging.info("✓ BigQuery CLI nalezen")
        return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        logging.warning("⚠️ BigQuery CLI se nepovedlo ověřit. Ujisti se, že je nainstalovaný.")
        return False  # Ne raise - jen varování
    
def create_config_template():
    "Vytvoří šablonu pro config.yaml"
    template = """project_root: .

environments:
  dev:
    project: tvuj-dev-projekt
    replacements:
      - from: prod_project.core
        to: bqtesting-494319.test_dataset

  prod:
    project: prod-projekt
    replacements: []
"""    
    if os.path.exists("config.yaml"):
        logging.warning("config.yaml již existuje")
        return

    with open("config.yaml", "w") as f:
        f.write(template)

    logging.info("config vytvořen")
from config import load_config, get_env,check_bq_cli,create_config_template
import argparse
import logging
import os

from sql_processor import check_folder, get_sql_folders,process_sql_dir
from create_batch import generate_batch_file,generate_sql_file

def main():

    ## Set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', 
        handlers=[logging.StreamHandler()]
    )

    console_handler = logging.getLogger().handlers[0]
    console_handler.setLevel(logging.INFO)


    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="prod", help="Environment")
    parser.add_argument("--settings", action="store_true", help="Vytvoří šablonu config.yaml")
    args = parser.parse_args()

    if args.settings:
        create_config_template()
        return

    check_bq_cli()

    # Load config and environment
    config = load_config()
    env = get_env(config, args.env)

    # Extract environment variables
    replacements = env.get("replacements", [])
    project = env.get("project")

    if check_folder():
        batch = ""
        sub_dir = get_sql_folders()
        for dir in sub_dir:
            batch += process_sql_dir(dir, replacements) +"\n\n"

    if batch:
        generate_sql_file(batch)
        generate_batch_file(os.name)


if __name__ == "__main__":
    main()
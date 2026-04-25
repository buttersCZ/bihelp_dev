from config import load_config, get_env
import argparse
import logging

from sql_processor import check_folder, get_sql_folders,process_sql_dir
from create_batch import generate_batch_file

def main():

    ## Set up logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', 
        handlers=[logging.FileHandler("done/{time}app.log"),
                  logging.StreamHandler()],

    )

    file_handler = logging.getLogger().handlers[0]
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.getLogger().handlers[1]
    console_handler.setLevel(logging.INFO)

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", default="prod", help="Environment")
    args = parser.parse_args()

    # Load config and environment
    config = load_config()
    env = get_env(config, args.env)

    # Extract environment variables
    replacements = env.get("replacements", [])
    project = env.get("project")

    if check_folder():
        batch = ""
        logging.info("Jsme ve spravne slozce")
        sub_dir = get_sql_folders()
        for dir in sub_dir:
            logging.info(f"Jsme v dir {dir}")
            batch += process_sql_dir(dir, replacements) +"\n\n"

    if batch:
        generate_batch_file(batch)

if __name__ == "__main__":
    main()
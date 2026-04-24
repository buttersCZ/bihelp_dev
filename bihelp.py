from config import load_config, get_env
import argparse
import logging


def main():
    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument("--env",help="Environment")

    args = parser.parse_args()

    config = load_config()
    env = get_env(config, args.env)

    replacements = env.get("replacements", [])
    project = env.get("project")

    logging.info(f"Project: {project}")
    logging.info(f"Replacements: {replacements}")   


if __name__ == "__main__":
    main()
from config import load_config, get_env


config = load_config()
env = get_env(config, args.env)

replacements = env.get("replacements", [])
project = env.get("project")
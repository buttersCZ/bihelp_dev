
import yaml


def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def get_env(config, env_name):
    envs = config.get("environments", {})
    
    if env_name not in envs:
        raise ValueError(f"Environment '{env_name}' not found")

    return envs[env_name]
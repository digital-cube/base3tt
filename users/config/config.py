import base

base.config.load_from_yaml('config/config.yaml')
TORTOISE_ORM = base.config.tortoise_config()

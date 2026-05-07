import yaml


class Environment:

    def __init__(self):
        with open("config/config.yaml") as file:
            self.config = yaml.safe_load(file)

    def get(self, key):
        return self.config.get(key)


env = Environment()
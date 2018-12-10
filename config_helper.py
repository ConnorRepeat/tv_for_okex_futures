import os

import toml


def get_local_config():
    pwd = os.path.split(os.path.realpath(__file__))[0]
    with open(pwd + '/config.toml') as f:
        return toml.load(f)


class LocalConfig:
    def __init__(self):
        self.cfg = get_local_config()

    def get_cfg(self):
        return self.cfg

    def get_env(self):
        return self.cfg.get("app").get("env")

    def get_app_config(self):
        return self.cfg.get("app")

    def get_exchange_auth(self, exchange_name):
        return self.cfg.get("exchange_auth").get(exchange_name)

diamond = LocalConfig()

if __name__ == '__main__':
    pass
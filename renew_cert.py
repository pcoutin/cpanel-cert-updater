import acme_tiny
import config
from cpanelapi import client
from pprint import pprint


CLIENT = client.Client(
    config.USER,
    config.CPANEL_HOST,
    password=config.PASSWORD,
    cpanel=True
)

def main():
    crt = acme_tiny.get_crt(config.ACCOUNT_KEY, config.CSR, config.ACMEDIR)
    ssl_args = {'cert': crt}

    def try_read(key, setting):
        if hasattr(config, setting):
            with open(getattr(config, setting), 'r') as f:
                ssl_args[key] = f.read()

    try_read('key', 'SERVER_KEY')
    try_read('cabundle', 'CABUNDLE')


    return CLIENT.uapi('SSL', 'install_ssl', **ssl_args)

if __name__ == "__main__":
    pprint(main())

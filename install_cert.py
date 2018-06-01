#!/usr/bin/env python

import sys
from cpanelconf import USER, HOST, CPANEL_HOST, PASSWORD
from cpanelapi import client


def install_ssl(cert_path, key_path=None, cabundle_path=None):
    c = client.Client(USER, CPANEL_HOST, password=PASSWORD, cpanel=True)
    ssl_args = {}

    def try_read(fp, k):
        if fp != None:
            with open(fp, 'r') as f:
                ssl_args[k] = f.read()

    try_read(cert_path, 'cert')
    try_read(key_path, 'key')
    try_read(cabundle_path, 'cabundle')

    ret = c.uapi('SSL', 'install_ssl', **ssl_args)

    sys.stdout.buffer.write(str(ret))


def main(argv):
    return install_ssl(*argv)


if __name__ == '__main__':
    main(sys.argv[1:])

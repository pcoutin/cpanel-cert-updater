#!/usr/bin/env python

import sys
import pprint
from cpanelconf import USER, HOST, CPANEL_HOST, PASSWORD
from cpanelapi import client


CLIENT = client.Client(USER, CPANEL_HOST, password=PASSWORD, cpanel=True)


def print_res(res):
    pprint.pprint(res)


def install_ssl(cert_path, key_path=None, cabundle_path=None):
    ssl_args = {}

    def try_read(fp, k):
        if fp != None:
            with open(fp, 'r') as f:
                ssl_args[k] = f.read()

    try_read(cert_path, 'cert')
    try_read(key_path, 'key')
    try_read(cabundle_path, 'cabundle')

    return CLIENT.uapi('SSL', 'install_ssl', **ssl_args)


def main(argv):
    res = install_ssl(*argv)
    print_res(res)


if __name__ == '__main__':
    main(sys.argv[1:])

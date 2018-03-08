#!/usr/bin/env python

import sys
from cpanelconf import USER, HOST, PASSWORD
from cpanelapi import client


def install_ssl(cert_path, key_path, cabundle_path):
    c = client.Client(USER, HOST, password=PASSWORD, cpanel=True)
    with open(cert_path, 'r') as cert_file, \
         open(key_path, 'r') as key_file, \
         open(cabundle_path, 'r') as cabundle_file:
        cert = cert_file.read()
        key = key_file.read()
        cabundle = cabundle_file.read()
        ret = c.uapi('SSL', 'install_ssl', domain=HOST, cert=cert,
                     key=key, cabundle=cabundle)
        print(ret)


def main(argv):
    return install_ssl(argv[0], argv[1], argv[2])


if __name__ == '__main__':
    main(sys.argv[1:])

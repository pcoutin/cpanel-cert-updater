cpanel-cert-updater
===================

This is a small script for setting TLS/SSL certificates in CPanel. It is meant
for automatically renewing Let's Encrypt certificates with GoDaddy shared
hosting.

A cpanelconf.py with contents like the following is needed:

```
import socket

USER = 'your_cpanel_user'
PASSWORD = 'cpanel_password'
HOST = 'yourwebsite.com'
CPANEL_HOST = socket.getfqdn()
```

It is possible to connect to CPanel through https://yourwebsite.com:2083, but
it just redirects to the corresponding virtual host, and can have certificate
validation problems. The FQDN of the virtual host can be found by SSHing into
the shell account, and running `hostname -f`, or as above.

If you have already installed a certificate with the same private key and CA
bundle, you can probably just pass the certificate.

```
pipenv run python install_cert.py path/to/signed.crt path/to/domain.key path/to/intermediate.pem
pipenv run python install_cert.py path/to/signed.crt
```

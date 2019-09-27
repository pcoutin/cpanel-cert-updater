cpanel-cert-updater
===================

note: potential vulns in old dependencies

Should just use acme.sh

Automatically renews free Let's Encrypt certificates for GoDaddy shared
hosting.  Should work with other CPanel hosts as well.

It uses [acme-tiny](https://github.com/diafygi/acme-tiny).

## How to automate Let's Encrypt TLS/HTTPS/X.509 certificate renewal for cPanel

TODO

  * delete previous installed certificate
  * wildcard certificate?
  * use docker, alpine, PyInstaller to automate bundling and deploying of a
    single executable

First, log in (not to CPanel but to GoDaddy) and make sure SSH support is
enabled. You may need to disable it and enable it again.

SSH in and install miniconda3 in ~/miniconda3. The version of Python in
the GoDaddy shell is ancient, as is OpenSSL.

You don't have to use pipenv, you can just run the following:

```
. ~/miniconda3/bin/activate
pip install acme_tiny git+https://github.com/pcoutin/python-cpanelapi
```

A config.py with contents like the following is needed:

```
import socket

USER = 'your_cpanel_user'
PASSWORD = 'cpanel_password'
HOST = 'yoursite.com'
CPANEL_HOST = socket.getfqdn()

ACCOUNT_KEY = 'account.key'
CSR = 'domain.csr'
ACMEDIR = str(Path.home()) + '/public_html/.well-known/acme-challenge/'
SERVER_KEY = 'domain.key'
```

It is possible to connect to CPanel through https://yoursite.com:2083, but
it had certificate validation problems. The FullyQualifiedDomainName of the
virtual host can be found by SSHing into the shell account and running
`hostname -f`, or as above with `socket.getfqdn()`.

```
openssl genrsa 4096 > account.key
openssl genrsa 4096 > domain.key
openssl req -new -sha256 -key domain.key -subj "/" -reqexts SAN -config <(cat /etc/ssl/openssl.cnf <(printf "[SAN]\nsubjectAltName=DNS:yoursite.com,DNS:www.yoursite.com")) > domain.csr


./renew_cert.sh
```

It's unnecessary to send the domain.key (your private key for TLS) after the
first time setting/renewing the certificate, so you can unset `SERVER_KEY`.

Then you can run `renew_cert.sh` in a crontab.

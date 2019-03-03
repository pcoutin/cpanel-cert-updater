cpanel-cert-updater
===================

Automatically renews Let's Encrypt certificates for GoDaddy shared hosting.
Should work with other CPanel hosts as well.

It uses [acme-tiny](https://github.com/diafygi/acme-tiny).

## How to get free Let's Encrypt TLS/HTTPS/X.509 certificates in GoDaddy

(and how to max out your file count limit by installing miniconda3 - might
be better to use OpenBSD's acme-client compiled statically with LibreSSL)

TODO
  - write better instructions
  - look into removing old certificates from cpanel
  - make sure updates to dependencies didn't break anything
  - don't try to set a certificate after failure

First, log in (not to CPanel but to GoDaddy) and make sure SSH support is
enabled. You may need to disable it and enable it again.

SSH in and install miniconda3 in your home directory. The version of Python in
the GoDaddy shell is ancient, as is OpenSSL.

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

You won't need to send the domain.key (your private key for TLS) after the
first time setting/renewing the certificate, so you can unset `SERVER_KEY`.

Then you can run `renew_cert.sh` in a crontab.

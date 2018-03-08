cpanel-cert-updater
===================

Written to automate updating Let's Encrypt certificates for a GoDaddy shared
hosting account.

Run `pipenv install` to install the dependencies.

A cpanelconf.py with contents like the following is needed:

```
USER = 'your_cpanel_user'
PASSWORD = 'cpanel_password'
HOST = 'yourwebsite.com'
```

Then run it, passing the paths to the certificate, private key, and
[CA bundle](https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem).

```
pipenv run python install_cert.py path/to/signed.crt path/to/domain.key path/to/intermediate.pem
```

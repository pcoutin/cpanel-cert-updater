#!/bin/sh

export LANG=en_US.UTF-8

. ~/miniconda3/bin/activate
cd ~/cpanel-cert-updater
python3 renew_cert.py

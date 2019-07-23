#!/usr/bin/env bash
apt update
apt full-upgrade
apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv nginx
pip install flask
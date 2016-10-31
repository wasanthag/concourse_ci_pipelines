#!/bin/sh

set -e -u -x

#easy_install-2.7 -Z /opt/acicobra-1.3_2h-py2.7.egg
#easy_install-2.7 -Z /opt/acimodel-1.3_2h-py2.7.egg
sleep 10
python github-code/api.py &
sleep 10
#curl http://localhost:5000/health
python github-code/unit-test.py

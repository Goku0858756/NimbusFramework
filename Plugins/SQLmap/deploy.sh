#!/usr/bin/env bash

CURR="`pwd`"
virtualenv --python=/usr/local/bin/python2.7 sqlmap
unzip sqlmap
cd sqlmap
source bin/activate
python sqlmap.py -hh

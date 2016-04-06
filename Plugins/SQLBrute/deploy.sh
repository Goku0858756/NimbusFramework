#!/usr/bin/env bash

CURR="`pwd`"
# echo $CURR
virtualenv --python=/usr/local/bin/python2.7 sqlbrute
cp $CURR/sqlbrute.py $CURR/sqlbrute/
cd sqlbrute/
source bin/activate
python2 sqlbrute.py -h

# check current dir
# create virtual env with python2.7
# git clone repository
# controller.py instantiation
# send args MultiThreaded

#git=https://github.com/GDSSecurity/SQLBrute.git
#git clone $git

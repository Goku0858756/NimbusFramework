#!/usr/bin/env bash

CURR="`pwd`"
FULL_DB_PATH=$CURR$DB

function stop {
    PID="`cat $CURR/mongodb.pid`"
    kill $PID
}

stop
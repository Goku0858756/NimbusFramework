#!/usr/bin/env bash

CURR="`pwd`"
DB="/data/db"
FULL_DB_PATH=$CURR$DB

# COLORS
RED="\033[1m"
RED_BACK="\033[41m"
GREEN="\033[70m"
GREEN_BACK="\033[42m"
YELLOW="\033[93m"
YELLOW_BACK="\033[103m"
BLUE="\033[34m"
BLUE_BACK="\033[106m"
END="\033[0m"

if [[ $# -eq 0 ]] ; then
    echo 'No arguments supplied'
    exit 1
fi


function start {
  echo "*** Starting MongoDB server"
  echo "$@"
  mongod --pidfilepath $CURR/mongodb.pid --quiet &
  exit 1
}
function cleanstop {
#    mongod --shutdown
    echo "Atlast, update without going offline"
    exit 1
}
function stop {
  echo "^^^ Stopping MongoDB server"
  # PID="`cat $CURR/mongodb.pid`"
  # kill $PID
  echo "PID is `pgrep mongod`"
  kill "`pgrep mongod`"
  exit 1
}
function status {
#    echo "Status MongoDB"



    if [[ "`pgrep mongod`" > /dev/null ]] ; then
        echo -e "$GREEN_BACK$RED[ UP ]$END MongoDB is running at PID `pgrep mongod`"
    else
        echo -e "$RED_BACK[ DOWN ]$END It seems MongoDB Server is currently not running"
    fi
    exit 1
}


function pid {
#  PID="`cat $CURR/mongodb.pid`"
#  echo $PID
#  exit 1
    echo "`pgrep mongod`"
    exit 1
}

case "$1" in
        start)
            start
            ;;
        stop)
            stop
            ;;
        cleanstop)
            cleanstop
            ;;
        status)
            status
            ;;
        restart)
            stop
            start
            ;;
        pid)
            pid
            ;;
        *)
            echo $"Usage: $ex0 < start | stop | restart | status | pid >"
            exit 1
esac
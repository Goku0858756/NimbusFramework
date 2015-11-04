#!/usr/bin/env bash

CURR="`pwd`"
DB="/data/db"
FULL_DB_PATH=$CURR$DB

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
    echo "Status MongoDB"

#    MPID = "`pgrep mongod`"
#    if  [[ $MPID -gt 1 ]] ; then
#        echo "MongoDB is gt 1"
#    elif [[ $MPID -eq 1 ]] ; then
#        echo "MongoDB is eq 1"
#    elif [[ "`pgrep mongod`" > /dev/null ]] ; then
#        echo "Unexpected outcome"
#    else
#
#        echo "I dont know what to do"
#    fi
    if [[ "`pgrep mongod`" > /dev/null ]] ; then
        echo "MongoDB is running at PID `pgrep mongod`"
    else
        echo "It seems MongoDB Server is currently not running"
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
#function restart {
#
#}
#function backup {
#
#}
#function database {
#
#}

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
            echo $"Usage: $0 {start|stop|restart|status|pid}"
            exit 1
esac
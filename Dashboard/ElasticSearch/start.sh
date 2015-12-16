#!/usr/bin/env bash

# Current Folder
CURR="`pwd`"

# Forlder Elastic Search
SEARCH_DIR="ElasticSearch"

# Directory /bin folder
BIN="bin"

function start {
    echo "Start Function"
    echo "$CURR/$SEARCH_DIR/$BIN"
    bin/elasticsearch --pidfile $CURR/search.pid


}
function stop {
    echo "Stop Function"
}
function status {
    echo "Status Function"
}
function pid {
    echo "Create PID file"
}
case "$1" in
        start)
            start
            ;;
        stop)
            stop
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
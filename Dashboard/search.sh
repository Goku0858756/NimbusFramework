#!/usr/bin/env bash

# RUNNING IT AS A SERVICE ON LINUX
# https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-service.html

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

# Current Folder
CURR="`pwd`"

# Forlder Elastic Search
SEARCH_DIR="ElasticSearch"

# Directory /bin folder
BIN="bin"

if [[ $# -eq 0 ]] ; then
    echo 'No arguments supplied'
    exit 1
fi


function start {
    echo "Starting the Search Engine. One moment please "
    $CURR/Dashboard/$SEARCH_DIR/bin/elasticsearch -d --pidfile $CURR/Dashboard/search.pid
    sleep 3
    echo -e "$GREEN_BACK$RED[ STARTING ]$END Search Engine is now running at PID `cat $CURR/Dashboard/search.pid`"

}
function stop {
    echo -e "$RED_BACK[ STOPPING ]$END Shutting down the Search Engine. One moment please"
    # echo "PID is `cat search.pid`"
#    echo "WHERE AM I? `pwd`"
    kill "`cat $CURR/Dashboard/search.pid`"
    exit 1
}
function status {
    echo "Temporarily Not Working"
#    if [[ "`pgrep elastic`" > /dev/null ]] ; then
#        echo -e "$GREEN_BACK$RED[ UP ]$END Search Engine is running at PID `cat search.pid`"
#    else
#        echo -e "$RED_BACK[ DOWN ]$END It seems Search Engine is currently not running"
#    fi
#    exit 1
}
function pid {
#    echo "WHERE AM I? `pwd`"
    echo "PID is `cat $CURR/Dashboard/search.pid`"
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
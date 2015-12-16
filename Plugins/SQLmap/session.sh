#!/usr/bin/env bash

CURR="`pwd`"
BIN="$CURR/sqlmap"
FILE="sqlmap.py"
ARGUMENTS=$@
#echo $@
echo $ARGUMENTS
echo $#

# Call SQLmap

function start {
    python $BIN/$FILE
}
function status {
    echo "STATUS"
}
function shell {
    echo "SHELL"
}
function argss {
    echo "ARGS"
    echo $@
}
case "$1" in
        start)
            start
            ;;
        status)
            status
            ;;
        shell)
            shell
            ;;
        argss)
            argss
            ;;
        *)
            echo $"Usage: $ex0 < start | status | shell >"
            exit 1
esac
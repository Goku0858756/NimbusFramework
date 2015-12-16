#!/usr/bin/env bash

# INSTAL SCRIPT for Elastic Search
function start {
    echo "Start Function"
}
function stop {
    echo "Stop Function"
}
function status {
    echo "Status Function"
}
function install {
    echo "Install Function"
}
function download {
  wget $URL -P $CURR
}
function unpack {
  # Note that if your tarball already contains a directory name you want to change, add the --strip-components=1 option
  tar -xf $CURR/$FILE --directory mongodb --strip-components=1
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
        install)
            install
            ;;
        *)
            echo $"Usage: $ex0 < start | stop | restart | status | pid >"
            exit 1
esac
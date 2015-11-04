#!/usr/bin/env bash



spin[0]="-"
spin[1]="\\"
spin[2]="|"
spin[3]="/"



CURR="`pwd`"
DB="/data/db"
FULL_DB_PATH=$CURR$DB

function start {
  echo -n "[copying] ${spin[0]}"
  while ["mongod --pidfilepath $CURR/mongodb.pid &"]
  do
    for i in "${spin[@]}"
    do
          echo -ne "\b$i"
          sleep 0.1
    done
  done
}

start
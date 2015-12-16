#!/usr/bin/env bash

function download {
    wget https://github.com/sqlmapproject/sqlmap.git
}
function clone {
#    git clone https://github.com/sqlmapproject/sqlmap.git
    git clone https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
}
function update {
    python sqlmap.py --update
}

# clone
# install
# update
# download
# version
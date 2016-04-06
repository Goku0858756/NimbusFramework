#!/usr/bin/env bash

#tmux new-session Nimbus-Framework
#tmux attach-session Nimbus-Framework
#tmux
#tmux rename-session -t Nimbus
#python nimbus.py
#tmux new-window
tmux start-server
tmux new-session -d -s Nimbus -n Core

tmux new-window -t Nimbus:1 -n Framework
tmux new-window -t Nimbus:2 -n Database
#tmux new-window -t Nimbus:3 -n Web

tmux send-keys -t Nimbus:1 'cd ~/virNimbus/; source bin/activate; python nimbus.py; clear' C-m
tmux send-keys -t Nimbus:2 'mongod; clear' C-m
#tmux send-keys -t Nimbus:3 'cd ~/virNimbus/; source bin/activate; cd Web; python controller.py; clear' C-m


tmux select-window -t Nimbus:1

tmux attach-session -d -t Nimbus

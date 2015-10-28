#!/bin/bash
FRAMEWORK = "Nimbus"


OS="`uname`"
case $OS in
 'Linux')
   OS='Linux'
   alias ls='ls --color=auto'
   ;;
 'FreeBSD')
   OS='FreeBSD'
   alias ls='ls -G'
   ;;
 'WindowsNT')
   OS='Windows'
   ;;
 'Darwin')
   OS='Mac'
   ;;
 'SunOS')
   OS='Solaris'
   ;;
 'AIX') ;;
 *) ;;
esac
echo " [*] [operating-system]: $OS"
NODENAME="`uname -n`"
echo " [*] [node-name] Node Name: $NODENAME"
KERNEL_VERSION="`uname -r`"
echo " [*] [kernel-version]: $KERNEL_VERSION"
MACHINE="`uname -m`"
echo " [*] [machine-name]: $MACHINE"
PROCESSOR="`uname -p`"
echo " [*] [processor-type]: $PROCESSOR"
SYSTEM="`uname -v`"
echo " [*] [system-complete]: $SYSTEM"

# if [[ "$OSTYPE" == "linux-gnu" ]]; then
#         # ...
# elif [[ "$OSTYPE" == "darwin"* ]]; then
#         # Mac OSX
# elif [[ "$OSTYPE" == "cygwin" ]]; then
#         # POSIX compatibility layer and Linux environment emulation for Windows
# elif [[ "$OSTYPE" == "msys" ]]; then
#         # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
# elif [[ "$OSTYPE" == "win32" ]]; then
#         # I'm not sure this can happen.
# elif [[ "$OSTYPE" == "freebsd"* ]]; then
#         # ...
# else
#         # Unknown.
# fi


function PATH_CURR {
 # Find the Current Path
 CURR="`pwd`"
 echo " [*] [current-path]: $CURR"
}
PATH_CURR

function PATH_HOME {
 HOME="~/ | ls -lah"
}
PATH_HOME


# $VAR get directory Framework
# TEST: echo $VAR

# Get newest Mongo

# Unzip Mongo

# Create /data/db/

# Check user chmod

# Backup /data/db
# tar -cZf /var/my-backup.tgz /home/me/

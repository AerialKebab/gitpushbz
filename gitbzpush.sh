#!/bin/bash

#"Usage: gitbz.sh <remote name> <bugnumber> <comment options> <statusupdate>"


#env -i git push "$1"
bugnumber="$2"
commentopt="$3"
statusupdate=" "



commitmessage=$(env -i git log -1 --pretty=%B)
export commitmessage
export bugnumber


env -i git push "$1"

if [ $# -eq 4 ]
  then 
    statusupdate=$4
fi
if [ $# -gt 4 ]
  then 
    echo "Too many arguments. Usage: ./gitbzpush.sh <remote name> <bugnumber> <comment options>"
    exit 1
fi
export commentopt
export statusupdate
#export PATH=$PATH:~/scripts
python /usr/local/bin/gitpushbugzilla.py 

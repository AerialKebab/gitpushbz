#!/usr/bin/env python

from __future__ import print_function
import bs4
import time
import pprint
import bugzilla
import os



URL = "http://172.16.146.233/bugzilla/xmlrpc.cgi"

#"Usage: gitbz.sh <remote name> <bugnumber> <comment options> <statusupdate>"

bugnumber=str(os.environ["bugnumber"])
numericalbug=""
for s in bugnumber:
  if s.isdigit():
    numericalbug+=s

bzapi = bugzilla.Bugzilla(URL)
bug =  bzapi.getbug(numericalbug)


if ( "-lc" in str(os.environ["commentopt"])): #if the command is -lc (last commit) 
  nc = os.environ["commitmessage"]
elif ( "-nc" in str(os.environ["commentopt"])): #if the command is new comment
  print("Comment:")
  nc = str(raw_input())
else:
  print("ERROR: No valid flag for comment submitted. Exiting.")
  exit()

newstatus=bug.status
if not (os.environ["statusupdate"].isspace()): #if there is a 4 parameter in the argument: if the status needs to be changed
  if( "-v" in str(os.environ["statusupdate"]) ): #verified
    newstatus = "VERIFIED"
  elif("-r" in str(os.environ["statusupdate"]) ): #resolved
    newstatus = "RESOLVED"
  elif("-u" in  str(os.environ["statusupdate"]) ): #unconfirmed
    newstatus = "UNCONFIRMED"
  else:
    print("ERROR: No valid flag for statusupdate submitted. Exiting.")
    exit()



if not bzapi.logged_in:
  print("This update requires cached login credentials for %s" % URL)
  bzapi.interactive_login()

print("Updating...")

update = bzapi.build_update(status=newstatus, comment = nc)
bzapi.update_bugs([bug.id], update)

#update = bzapi.build_update(comment=nc)
#bzapi.update_bugs([bug.id], update)

print("Updated.")
#print( os.environ["commentopt"])





# gitpushbz

Gitpushbz is a small integrated script that allows users to push to a repository and update a bugzilla entry at the same time.

1. Setup
First, move both the gitpushbz.sh and gitpushbugzilla.py into your a random folder.
Then, type:

sudo ln -s /full/path/to/your/gitpushbz.sh /usr/local/bin/gitpushbz

Make the file executable:

chmod +x /full/path/to/your/gitpushbz.sh

Then, move the gitpushbugzilla.py into your /usr/local/bin folder, and then make the file executable as well 

chmod +x /full/path/to/your/gitpushbugzilla.py

You're set. 

2. Usage

The command line usage for gitpushbz is:

gitpushbz <remote name> <bugnumber> <comment options> <statusupdate>"

With everything with spaces in between. For example, if I wanted to submit a bug entry to bug824, and NOT update the status, I would type:

gitpushbz master bug824 -nc
                        -lc 
                        
Where the program will use git to push the staged files to the master repository, access bug824 online through XMLRPC (prompting you to login if you're not) and create a new comment (-nc).  If you want to use the comment from the latest commit, you would use (-lc). 

As for the status updates, there are only three available flags for the updates, and they MUST be at the end of the command line. It will change to -v (Verified), -u (unconfirmed), and -r (resolved). For example, if I wanted to update bug824 and use the comment from my latest commit AND change the bugstatus to verified on bugzilla, I would enter:

gitpushbz master bug824 -lc -v






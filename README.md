# SqlQueryCompletionNotification
Little Python script that notifies you when your long taking query is finally done.  

Wrote this script for a project I was working for, one of the tables contained a couple of billion records on a small server. Needless to say it could take a while when complex queries would finish. This allowed me to work on other stuff without constantly checking whether the queries were finished.

## Installation
No need for installation, just download the script, make sure `sqlalchemy`-package is installed and ready to go.

## Run
You can either run it from command line be executing: `python sql_query_notify.py <connection_string>`. 
Or replace the connection string in the script.


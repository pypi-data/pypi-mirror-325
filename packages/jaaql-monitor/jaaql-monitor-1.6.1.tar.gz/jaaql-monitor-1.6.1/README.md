# Usage
JAAQL Monitor can be called as such

    jaaql_monitor.exe creds_file
    
Where creds_file is a file of the format

    jaaql_url
    username
    password

And as an example

    jaaql.io
    superjaaql
    passw0rd

Then it will accept input over standard input. Scripts can be separated via \p and \g. \p Will print everything in the standard input so far (since the last \g) and \g will submit everything in the standard input so far to jaaql (since the last \g). So \p\g will print and submit to jaaql. Any errors which we receive will be output on stdin and stderr

# Building
To build you will need to have a python environment (3.8) setup locally. Building will produce a windows executable (the latest executable is in the repo if you require it). If you are on linux you can create an executable as well but you need to install python to do that so you might as well just use the python script. To build please run the commands below

    ./build.bat

# Running locally
Please install requirements.txt. Using python 3.11
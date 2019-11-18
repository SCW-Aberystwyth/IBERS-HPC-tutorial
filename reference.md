---
layout: reference
root: .
---

# SFTP

If you want to use SFTP from the command line instead of with Filezilla then these commands might be helpful.

SFTP takes the argument of the username followed by an `@` symbol and then the hostname. Optionally you can specify what directory to start in by putting a `:` symbol after this and adding the directory name. The command below will start in `/home/s.jane.doe/data`, if no directory is specified then sftp defaults to your home directory.

## Running SFTP

~~~
sftp s.jane.doe@sunbird.swansea.ac.uk:/home/s.jane.doe/data
~~~
{: .bash}

~~~
s.jane.doe@sunbird.swansea.ac.uk's password:
Connected to sunbird.swansea.ac.uk.
Changing to: /home/s.jane.doe/data
sftp> ls
~~~
{: .output}

## SFTP commands ##

| command | Purpose |
| --- | --- |
| ls  | list files |
| pwd | curret directory on server |
| !pwd | current directory on local system |
| get | copy a file from the server |
| put | copy a file to the server |
| lcd | change local directory |
| cd | change remote directory |

# Useful Links

* Slurm Environment Variables - https://www.glue.umd.edu/hpcc/help/slurmenv.html

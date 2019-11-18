---
title: "Filesystems and Storage"
author: "Colin Sauze, Ed Bennett, Jarno Rantaharju"
teaching: 15
exercises: 30
questions:
 - "Where can I store my data?"
 - "What is the difference between scratch and home filestore?"
objectives:
 - "Understand the difference between home and scratch directories"
 - "Understand how to copy files between your computer and your Supercomputing Wales home/scratch directories"
keypoints:
 - "Scratch and home are per site."
 - "Scratch is faster and has no quotas, but short-term. home is slower and has quotas, but is long-term."
---


# Filesystems and Storage

## What is a filesystem?
Storage on most compute systems is not what and where you think they are! Physical disks are bundled together into a virtual volume; this virtual volume may represent one filesystem, or may be divided up, or partitioned, into multiple filesystems. And your directories then reside within one of these fileystems. Filesystems are accessed over the network through mount points.

There are multiple storage/filesystems options available for you to do your work. The most common are:

* home: where you land when you first login. 50 GB per user. Slower access, backed up (Cardiff only). Used to store your work long term. 
* project: shared between all users of a project. Same filesystem as home. 
* scratch: temporary working space. Faster access, not backed up. Larger quota, but old files might get deleted. DON'T STORE RESULTS HERE!


Here's a synopsis of filesystems on Hawk in Cardiff:

|Name|Path|Default Quota|Disk Size|Backed Up|
|------|---|----|-----|---|-----|
|Home|/home/user.name|50GB|420TB|Yes|
|Project|/home/scwXXXX|Negotiable|420TB (same disk as home)|Yes|
|Scratch|/scratch/user.name|20TB + 10million files|692TB|No|


and on Sunbird in Swansea:


|Name|Path|Default Quota|Disk Size|Backed Up|
|------|---|----|-----|---|-----|
|Home|/home/user.name|100GB|231TB|No|
|Project|/home/scwXXXX|Negotiable|231TB (same disk as home)|No|
|Scratch|/scratch/user.name|20TB + 10million files|808TB|No|


**Important!! Ensure that you don't store anything longer than necessary on scratch, this can negatively affect other people’s jobs on the system.**


# Accessing your filestore

## How much quota do I have left on my home directory?

Login to a head node (e.g. `sunbird.swansea.ac.uk` or `hawklogin.cf.ac.uk`) and run the ```myquota``` command. This will tell you how much space is left in your home directory.

~~~
$ myquota
~~~
{: .bash}

~~~
HOME DIRECTORY a.cos
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
    /lustrehome   48.4G    100G    110G       -  206182  220000  230000       -

SCRATCH DIRECTORY a.cos
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
       /scratch  63.29G  19.56T  20.06T       -  313075  9851800 10101800       -

~~~
{: .output}

## Group Filestore

If you have multiple collaborators working on a particular project and
would like to share common software or data across the project, then
it will be convenient for you to use a shared filestore. These can be
created on `/home` (for long-term use, e.g. software) or on `/scratch`
(for short-term data). If you would like one setup for you, you can
raise a support ticket or speak to one of your local RSEs.

## How much scratch have I used?

The ```df``` command tells you how much disk space is left. The ```-h``` argument makes the output easier to read, it gives human readable units like M, G and T for Megabyte, Gigabyte and Terrabyte instead of just giving output in bytes. By default df will give us the free space on all the drives on a system, but we can just ask for the scratch drive by adding ```/scratch``` as an argument after the ```-h```.

~~~
$ df -h /scratch
~~~
{: .bash}

~~~
Filesystem                                Size  Used Avail Use% Mounted on
172.2.1.51@o2ib:172.2.1.52@o2ib:/scratch  692T   57T  635T   9% /scratch
~~~
{: .output}

## Copying data from your PC to Supercomputing Wales

You can copy files to/from your Supercomputing Wales home and scratch drives using the secure copy protocol (SCP) or secure file transfer protocol (SFTP) and connecting to Sunbird or Hawk. 

### Copying data using Filezilla

Filezilla is a graphical SCP/SFTP client available for Windows, Mac and Linux. You can download it from [Filezilla download](https://filezilla-project.org/download.php?type=client)

Open filezilla and type ```sftp://sunbird.swansea.ac.uk``` or ```sftp://hawklogin.cf.ac.uk``` into the host box. Enter your username and password in the username/password boxes.

![Transferring files using FileZilla](../fig/filezilla1.png)

Click Quickconnect and a connection will be started. The first time you connect you will be asked to verify the host key, tick the "Always trust this host, add key to the cache" box to stop this message appearing again in future.

![Transferring files using FileZilla](../fig/filezilla2.png)

You should now have some files in the right hand side of the window. These are on the remote system, the list on the left hand side is your local system.

![Transferring files using FileZilla](../fig/filezilla3.png)

Files can be transferred either by dragging and dropping them from one side to the other. Or you can right click on a remote file and choose "Download" or a local file and choose "Upload". 

![Transferring files using FileZilla](../fig/filezilla4.png)
![Transferring files using FileZilla](../fig/filezilla5.png)

You can change directory on the remote host by typing a path into the "Remote site:" box. For example type in ```/scratch/user.name``` (where user.name is your username) to access your scratch directory. 

![Transferring files using FileZilla](../fig/filezilla6.png)


### Copying on the command line using SFTP or SCP

~~~
If you prefer to use a command line interface to copy files then see the [reference](reference) material on using the SFTP and SCP commands. 
~~~
{:. callout}


# Exercises

> ## Using the `df` command. 
> 1. Login to a login node
> 2. Run the command `df -h`.
> 3. How much space does /scratch have left?
> 4. If you had to run a large job requiring 10TB of scratch space, would there be enough space for it?
{: .challenge}

> ## Using the `myquota` command.

> 1. Login to a login node.
> 2. Run the `myquota` command. 
> 3. How much space have you used and how much do you have left? 
> 4. If you had a job that resulted in 60GB of files would you have enough space to store them?
{: .challenge}

> ## Copying files.

> 1. Login to a login node.
> 2. Create a file called hello.txt by using the nano text editor (or the editor of your choice) and typing `nano hello.txt`. Enter some text into the file and press Ctrl+X to save it. 
> 3. Use either Filezilla or SCP/SFTP to copy the file to your computer. 
> 4. Create a file on your computer using a text editor. Copy that file to your Supercomputing Wales home directory using Filezilla or SCP/SFTP and examine its conents with `nano` on the login node. 

{: .challenge}

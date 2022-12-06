---
title: "Filesystems and Storage"
author: "Colin Sauze, Ed Bennett, Jarno Rantaharju"
teaching: 15
exercises: 10
questions:
 - "Where can I store my data?"
 - "What is the difference between scratch and home filestore?"
objectives:
 - "Understand the difference between home and scratch directories"
 - "Understand how to copy files between your computer and your Bert home/scratch directories"
keypoints:
 - "The home directory is the default place to store data."
 - "The scratch directory is a larger space for temporary files."
 - "Quotas on home are much smaller than scratch."
 - "The SSD scratch is faster than regular scratch, but smaller."
---


# Filesystems and Storage

## What is a filesystem?
Storage on most compute systems is not what and where you think they are! Physical disks are bundled together into a virtual volume; this virtual volume may represent one filesystem, or may be divided up, or partitioned, into multiple filesystems. And your directories then reside within one of these fileystems. Filesystems are accessed over the network through mount points.

There are multiple storage/filesystems options available for you to do your work. The most common are:

* home: where you land when you first login. 50 GB per user by default. Slower access, backed up. Used to store your work long term. 
* groups: shared between all users of a project. If you're group hasn't got a space on here then you need to request one.
* scratch: temporary working space, not backed up. Larger quota, but old files might get deleted. DON'T STORE THINGS HERE LONG TERM!
* fast scratch: faster scratch space using solid state disks. You need to request access to this.


Here's a synopsis of filesystems on Bert:

|Name|Path|Default Quota|Disk Size|Backed Up|
|------|---|----|-----|---|-----|
|Home|/ibers/ernie/home/user.name|250GB|42TB|Yes|
|Groups|/ibers/repository03/groups/group.name|None currently|200TB|Yes|
|Scratch|/scratch/user.name|None currently|109TB|No|
|Fast Scratch|/fast-scratch/user.name|None currently|5.2TB|No|


**Important!! Ensure that you don't store anything longer than necessary on scratch, this can negatively affect other people’s jobs on the system.**


# Accessing your filestore

## How much quota do I have left on my home directory?

Login to the cluster (e.g. `bert.ibers.aber.ac.uk`) and run the ```quota``` command. This will tell you how much space is left in your home directory.

~~~
$ quota
~~~
{: .bash}

~~~
Quotas aren't currently working, don't abuse this!
~~~
{: .output}

## Group Filestore

If you have multiple collaborators working on a particular project and
would like to share common software or data across the project, then
it will be convenient for you to use a shared filestore. If you would like 
one setup for you, you can raise a support ticket by emailing ibers-cs@aber.ac.uk.

## How much scratch have I used?

The ```df``` command tells you how much disk space is left. The ```-h``` argument makes the output easier to read, it gives human readable units like M, G and T for Megabyte, Gigabyte and Terrabyte instead of just giving output in bytes. By default df will give us the free space on all the drives on a system, but we can just ask for the scratch drive by adding ```/scratch``` as an argument after the ```-h```.

~~~
$ df -h /scratch
~~~
{: .bash}

~~~
Filesystem         Size  Used Avail Use% Mounted on
nfs01-ib:/scratch  109T   11T   98T  10% /scratch
~~~
{: .output}

## Copying data from your PC to the cluster

You can copy files to/from your home and scratch drives using the secure copy protocol (SCP) or secure file transfer protocol (SFTP) and connecting to Bert. 

### Copying data using Filezilla

Filezilla is a graphical SCP/SFTP client available for Windows, Mac and Linux. You can download it from [Filezilla download](https://filezilla-project.org/download.php?type=client)

Open filezilla and type ```sftp://bert.ibers.aber.ac.uk``` into the host box. Enter your username and password in the username/password boxes.

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

If you prefer to use a command line interface to copy files then see the [reference](reference) material on using the SFTP and SCP commands. 


# Exercises

> ## Using the `df` command. 
> 1. Login to Bert
> 2. Run the command `df -h`.
> 3. How much space does /scratch have left?
> 4. If you had to run a large job requiring 10TB of scratch space, would there be enough space for it?
{: .challenge}

> ## Copying files.
> 1. Login to Bert
> 2. Create a file called hello.txt by using the nano text editor (or the editor of your choice) and typing `nano hello.txt`. Enter some text into the file and press Ctrl+X to save it. 
> 3. Use either Filezilla or SCP/SFTP to copy the file to your computer. 
> 4. Create a file on your computer using a text editor. Copy that file to your Bert home directory using Filezilla or SCP/SFTP and examine its conents with `nano` on the login node. 
{: .challenge}

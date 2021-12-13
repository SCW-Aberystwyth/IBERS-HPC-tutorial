---
title: "Logging in to Supercomputing Wales"
author: "Colin Sauze"
teaching: 20
exercises: 15
questions:
objectives: 
 - "Understand the difference between the login node and compute nodes."
 - "How can do I log in to Supercomputing Wales?"
objectives:
 - "Understand how to log in to the Supercomputing Wales hubs"
 - "Understand the difference between the login node and each cluster's head node."
keypoints:
 - "`ssh sunbird.swansea.ac.uk` or `ssh hawklogin.cf.ac.uk` to log in to the system"
 - "`sinfo` shows partitions and how busy they are."
 - "`slurmtop` shows another view of how busy the system is."
---


# Logging in

Before we can log in to Supercomputing Wales, we need to set a password.
The Supercomputing Wales clusters use a separate password database to
the four partner institutions, so the password must be set separately
from (and should be different to) your institutional login. To do this
visit [MySCW][myscw], log in with your institutional credentials, and
use the "Reset SCW Password" link in the left sidebar.

While you are visiting the MySCW dashboard, take a note of your
Supercomputing Wales username. Your username is
usually your institutional ID prefixed by `a.` for
Aberystwyth users, `b.` for Bangor users, `c.` for Cardiff users, and `s.`
for Swansea users. (Occasionally the part of the username after the `.`
will vary from this pattern, but the prefix should always match this.)
External collaborators will have a username beginning with `x.`.

Aberystwyth and Swansea users (and their external collaborators) should log in to the Swansea Sunbird system by typing:

~~~
$ ssh username@sunbird.swansea.ac.uk
~~~
{: .bash}

Bangor and Cardiff Users (and their external collaborators) should log in to the Cardiff Hawk system by typing:

~~~
$ ssh username@hawklogin.cf.ac.uk
~~~
{: .bash}


If you use Windows and haven't installed the Git bash shell, you can instead use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
and enter either `sunbird.swansea.ac.uk` or `hawklogin.cf.ac.uk` in the hostname box.

> ## Lockout
>
> Since the Supercomputing Wales clusters allow connections from
> anywhere in the world, they need to be relatively tough to avoid
> unscrupulous hackers gaining access to your research data.
> This means that if you enter a wrong password (or SSH key) too
> many times in short succession, then your computer will be blocked
> from accessing the cluster for a few hours.
>
> To avoid this happening in a workshop, we recommend raising a hand
> or otherwise letting an instructor know if your first attempt to log
> in fails.
>
> If you have been locked out and urgently need to get back in
> without waiting for the block to expire, then
> [contact the support desk][scw-support]. During working hours
> a member of the support team will be available to assist.
{: .callout}


## What's available?

### Supercomputing Wales

These figures may still be subject to some change and might have been sourced from out of date documents.

|Partition|Number of Nodes|Cores per node|RAM|Other|
|-------|----|----|------|----|------|
|Swansea Compute|123|40|382GB||
|Swansea Data Lake|1|72|1500GB|Installed with Swansea system, and intended for e.g. Hadoop and Elastic Stack users. Not integrated with the main Sunbird system; contact Support or your RSE team for access details.|


|Cluster|Number of Nodes|Cores per node|RAM|Other|
|-------|----|----|------|----|------|
|Cardiff Compute|134|40|190GB||
|Cardiff Compute AMD|64|64|256GB|AMD EPYC CPUs, not fully operational|
|Cardiff HTC|63|40|190GB||
|Cardiff High Memory|26|40|382GB||
|Cardiff Dev|2|40|190GB||
|Cardiff Data Lake|2|?|?|Will be installed later. Intended for Hadoop and Elastic Stack users.|

Aberystwyth and Swansea users are expected to use the Swansea system and will need to make a case for why they would need to use the Cardiff system. Bangor and Cardiff users are expected to use Cardiff, and external users are expected to use the same system as the owner of the project of which they are a member.

(There are also a number of GPU nodes available; these will be discussed
in [Running on GPUs](08-running-on-gpus).)

### Slurm

Slurm is the management software used on Supercomputing Wales. It lets you submit (and monitor or cancel) jobs to the cluster and chooses where to run them. 

Other clusters might run different job management software such as LSF, Sun Grid Engine or Condor, although they all operate along similar principles.


### How busy is the cluster?

The `sinfo` command tells us the state of the cluster. It lets us know what nodes are available, how busy they are and what state they are in.

Clusters are sometimes divided up into partitions. This might separate some nodes which are different to the others (e.g. they have more memory, GPUs or different processors).

~~~
PARTITION     AVAIL  TIMELIMIT  NODES  STATE NODELIST
compute*        up 3-00:00:00      1   fail scs0042
compute*        up 3-00:00:00      1 drain* scs0004
compute*        up 3-00:00:00      2    mix scs[0018,0065]
compute*        up 3-00:00:00     86  alloc scs[0001-0003,0005-0017,0019-0035,0043-0046,0049-0064,0066-0072,0097-0122]
compute*        up 3-00:00:00     32   idle scs[0036-0041,0047-0048,0073-0096]
development     up      30:00      1   fail scs0042
development     up      30:00      1 drain* scs0004
development     up      30:00      2    mix scs[0018,0065]
development     up      30:00     86  alloc scs[0001-0003,0005-0017,0019-0035,0043-0046,0049-0064,0066-0072,0097-0122]
development     up      30:00     32   idle scs[0036-0041,0047-0048,0073-0096]
gpu             up 2-00:00:00      4   idle scs[2001-2004]
~~~
{: .output}

 * The `*` after `compute` means that this is the default partition.
 * `AVAIL` tells us if the partition is available.
 * `TIMELIMIT` tells us if there's a time limit for jobs
 * `NODES` is the number of nodes in this partition in this particular
   state.
 * `STATE` describes what these nodes are doing:
     * `drain` means that the node will become unavailable once the
       jobs currently running on it complete.
	 * `down` means that the node is is powered off or otherwise
       unavailable for use.
	 * `alloc` means that the node is fully allocated; all CPU cores
       are in use running users' software.
	 * `mix` means that some of the CPU cores on a node are allocated
       to a user, and others are available for use.
	 * `idle` means that the node is not currently allocated, and is
       available for use.


# Exercises

> ## Logging into Supercomputing Wales
>
> If you haven't already:
>
> 1. In your web browser go to [My Supercomputing Wales](https://my.supercomputing.wales) and log in with your university username and password.
> 2. Click on "Reset SCW Password" and choose a new password for logging into the HPC. Your username is displayed in the "Account summary" box on the main page. Its usually `a.`/`b.`/`c.`/`s.` and your normal university login details.
> 3. Log in to `sunbird.swansea.ac.uk` or `hawklogin.cf.ac.uk` using your SSH client.
> 4. Run the `sinfo` command to see how busy things are.
> 5. Try `sinfo --long`, what extra information does this give?
{: .challenge}

[myscw]: https://my.supercomputing.wales
[scw-support]: https://portal.supercomputing.wales/index.php/index/submit-support-ticket/

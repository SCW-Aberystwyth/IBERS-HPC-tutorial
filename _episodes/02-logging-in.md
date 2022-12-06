---
title: "Logging in to Bert"
author: "Colin Sauze"
teaching: 20
exercises: 15
questions:
objectives: 
 - "Understand the difference between the login node and compute nodes."
 - "Understand how to log in to Bert"
keypoints:
 - "`ssh bert.ibers.aber.ac.uk` to log in to the system"
 - "`sinfo` shows partitions and how busy they are."
---


# Logging in

Before we can log in to Bert, we need to have an account.

We can then log in to the system by typing:

~~~
$ ssh username@bert.ibers.aber.ac.uk
~~~
{: .bash}



If you use Windows and haven't installed the Git bash shell, you can instead use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
and enter either `bert.ibers.aber.ac.uk` in the hostname box.

## What's available?

### Bert's Nodes

These figures may still be subject to some change.

|Partition|Number of Nodes|Cores per node|RAM|Other|
|-------|----|----|------|----|------|
|AMD|4|32|256GB||
|Intel|5*|8|96GB|3 nodes are broken|
|Highmem|1|32|512GB||
|Fat|1|16|1TB||
|GPU|1|32|768GB|Has a GPU Accelerator|


### Slurm

Slurm is the management software used on Bert. It lets you submit (and monitor or cancel) jobs to the cluster and chooses where to run them. 

Other clusters might run different job management software such as LSF, Sun Grid Engine or Condor, although they all operate along similar principles.


### How busy is the cluster?

The `sinfo` command tells us the state of the cluster. It lets us know what nodes are available, how busy they are and what state they are in.

Clusters are sometimes divided up into partitions. This might separate some nodes which are different to the others (e.g. they have more memory, GPUs or different processors).

~~~
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
gpu          up   infinite      1   idle gpu01
intel        up   infinite      1    mix node003
intel        up   infinite      1   idle node004
amd          up   infinite      4    mix node[008-011]
highmem      up   infinite      1   idle node012
fat          up   infinite      1   idle node002
~~~
{: .output}

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

> ## Logging into Bert
>
> If you haven't already:
>
> 1. In your web browser go to [the account request page](http://bioinformatics.ibers.aber.ac.uk/request.html) and enter your details.
> 2. Log in to `bert.ibers.aber.ac.uk` using your SSH client.
> 4. Run the `sinfo` command to see how busy things are.
> 5. Try `sinfo --long`, what extra information does this give?
{: .challenge}


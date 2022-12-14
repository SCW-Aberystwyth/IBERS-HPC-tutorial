---
title: "Running Jobs with Slurm"
author: "Colin Sauze"
teaching: 25
exercises: 30
questions:
 - "How do I run a job with the Slurm scheduler?"
objectives:
 - "Understand how to submit an interactive job using Slurm"
 - "Understand how to submit a batch job using Slurm"
 - "Understand how to set the parameters for your Slurm job"
 - "Understand the concept of job arrays"
 - "Know how to get email alerts from Slurm"
keypoints:
 - "Interactive jobs let you test out the behaviour of a command, but aren't pratical for running lots of jobs"
 - "Batch jobs are suited for submitting a job to run without user interaction."
 - "Job arrays are useful to submit lots of jobs."
 - "Slurm lets you set parameters about how many processors or nodes are allocated, how much memory or how long the job can run."
 - "Slurm can email you when a job starts or finishes."
---


# Working with the scheduler

The scheduler is responsible for listening to your job requests, then finding the proper compute node that meets your job's resource requirements -- RAM, number of cores, time, etc. It dispatches the job to a compute node, collects info about the completed work, and stores information about your job. If you've asked it to do so, it will even notify you about the status of your job (e.g. begin, end, fail, etc).


## Running interactive jobs

There are two ways to run jobs on a cluster. One, usually done at the start, is to get an
interactive/foreground session on a compute node. This will give you a command prompt on a compute node and let you run the commands of your choice there.

If you want to experiment with some code and test it you should run it
this way. ** Don't run jobs on the login nodes ** -- the login node
is dedicated to letting users connect and compile their
software; its resources are negligible compared to the compute nodes.

To get an interactive session, you first need to issue a `salloc` command to reserve some resources.


~~~
salloc --nodes=1 --partition=intel --reservation=XXXX --time=0:30:0
~~~
{: .bash}

(You will need to replace `XXXX` to match the reservation ID given by your instructor.)
The --time=0:30:0 will launch your job with a 30 minute time limit.

The salloc command will respond now with a job ID number.

~~~
salloc: Granted job allocation 21712
salloc: Waiting for resource configuration
salloc: Nodes node003 are ready for job
~~~
{: .output}

> ## Reservations
>
> We can optionally specify a reservation ID to
> Slurm. A reservation is where some compute nodes have been reserved for a
> particular project at a particular time. To ensure nodes are available
> for this course we may have obtained a reservation. Your instructor
> will tell you which reservation to use here. Alternatively, these can be
> specified in the `SALLOC_RESERVATION` and `SBATCH_RESERVATION` environment variables.
{: .callout}

We have now allocated ourselves a host to run a program on. The `-n 1`
tells Slurm how many copies of the task we will be running. The
`--ntasks-per-node=1` tells Slurm that we will just be running one
task for every node we are allocated. We could increase either of
these numbers if we want to run multiple copies of a task and if we
want to run more than one copy per node.

To ensure nodes are available for this training workshop a reservation
may have been made to prevent anyone else using a few nodes. In order
to make use of these you must use the `--reservation` option too; if
you don't then you'll have to wait in the same queue as everyone else.

To actually run a command we now need to issue the `srun`
command. This also takes a `-n` parameter to tell Slurm how many
copies of the job to run and it takes the name of the program to
run. To run a job interactively we need another argument: `--pty`.

~~~
srun --pty /bin/bash
~~~
{: .bash}


If you run command above you will see the hostname in the prompt
change to the name of the compute node that Slurm has allocated to
you. In the example below the compute node is called `node003`.

~~~
[abc1@login01(aber) ~]$ srun --pty /bin/bash
[abc1@node003 ~]$
~~~
{: .output}

We are now logged into a compute node and can run any commands we wish and these will run on the compute node instead of the login node. You can also confirm the name of the host that you are connected to by running the `hostname` command.

~~~
hostname
~~~
{: .bash}

~~~
node003
~~~
{: .output}


Once we are done working with the compute node we need to disconnect
from it. The `exit` command will exit the bash program on the compute
node causing us to disconnect. After this command is issued the
hostname prompt should change back to the login node's name
(e.g. `sl1` or `cl1`).

~~~
[abc1@node003  ~]$ exit
exit
[abc1@login01(aber) ~]$
~~~
{: .output}

At this point we still hold an allocation for a node, and could run
another job on it if we wished. We can confirm this by examining the
queue of our jobs with the `squeue` command. By default this will show
all users' jobs, which is a bit overwhelming, so we can use `--user=`
and our username to filter to our own jobs only.

~~~
squeue --user=abc1
~~~
{: .bash}

~~~
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           21712   intel       bash       abc1  R       3:58      1 node003
~~~
{: .output}

To relinquish the node allocation we need to issue another exit command.

~~~
[abc1@login01(aber) ~]$ exit
~~~
{: .bash}

This will display a message that the job allocation is being relinquished and show us the same job ID number again.

~~~
exit
salloc: Relinquishing job allocation 21712
~~~
{: .output}

At this point our job is complete and we no longer hold any allocations. We can confirm this again with the `squeue` command.

~~~
[abc1@login01(aber) ~]$ squeue --user=s.jane.doe
~~~
{: .bash}

~~~
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
~~~
{: .output}




## Running batch jobs

For most situations we won't want to run a job interactively, instead we will want to submit it to the cluster have it do its work and return any output files to us. We might submit many copies of the same job with different parameters in this way. This method of working is known as batch processing. To do this we must first write some details about our job into a script file. Use `nano` (or your favourite command line text editor) and create a file containing the following:

~~~
nano batchjob.sh
~~~
{: .bash}

~~~
#!/bin/bash --login
###
# job name
#SBATCH --job-name=hostname
# job stdout file
#SBATCH --output=hostname.out.%J
# job stderr file
#SBATCH --error=hostname.err.%J
# maximum job time in D-HH:MM
#SBATCH --time=0-00:01
# maximum memory of 10 megabytes
#SBATCH --mem-per-cpu=10
# run a single task, using a single CPU core
#SBATCH --ntasks=1

# specify the reservation we have for the training workshop
# replace XX with the code provided by your instructor
# remove this for your own work
#SBATCH --reservation=XXXX
# Specify the intel partition
#SBATCH --partition=intel
###

/bin/hostname

~~~
{: .bash}

This is actually a bash script file containing all the commands that
will be run. Lines beginning with a `#` are comments which bash will
ignore. However lines that begin `#SBATCH` are instructions for the
`sbatch` program. The first of these (`#SBATCH --job-name=hostname`)
tells sbatch the name of the job; in this case we will call the job
hostname. The `--output` line tells sbatch where output from the
program should be sent; the `%J` in its name means the job
number. Including the job number in the output filename means that
repeated runs of the same script won't overwrite the output file. The
same applies for the `--error` line, except here it is for error
messages that the program might generate, in most cases this file will
be blank. The `--time` line limits how long the job can run for, this
is specified in days, hours and minutes. The `--mem-per-cpu` tells
Slurm how much memory to allow the job to use on each CPU it runs on,
if the job exceeds this limit Slurm will automatically stop it. You
can set this to zero for no limits. However by putting in a sensible
number you can help allow other jobs to run on the same
node. `--account` and `--reservation` tell Slurm to count usage
against the project created for training workshops, and to use the
nodes that have been reserved for today's training. (The value after
`--reservation` changes for each workshop; your instructor will give
you a value to use.) The final line specifies the actual commands
which will be executed, in this case its the `hostname` command which
will tell us the name of the compute node which ran our job.

> ## Running on your own
>
> If you are following this guide outside of a training workshop, or want to adjust the script to use in your own research,
> you will need to remove the `--reservation` line, since there won't be a reservation in place, and change `--account` to
> the project code of an approved project that you are a member of.
{: .callout}

Lets go ahead and submit this job with the `sbatch` command.

~~~
[abc1@login01(aber) ~]$ sbatch batchjob.sh
~~~
{: .bash}


sbatch will respond with the number of the job.

~~~
Submitted batch job 3739464
~~~
{: .output}

Our job should only take a couple of seconds to run, but if we are fast we might see it in the `squeue` list.

~~~
[abc1@login01(aber) ~]$ squeue --user=s.jane.doe
~~~
{: .bash}

~~~
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           3739464      work hostname jane.doe  R       0:01      1 node003
~~~
{: .output}

Once the job is completed two new files should be created, one called `hostname.out.3739464` and one called `hostname.err.3739464`. The `.out` file is the output from the command we ran and the `.err` is the errors from that command. Your job files will have different names as they will contain the job ID you were allocated and not `3739464`. Lets go ahead and look at the `.out` file:

~~~
[abc1@login01(aber) ~]$ cat hostname.out.373464
~~~
{: .bash}

~~~
node003
~~~
{: .output}

If we check the `.err` file it should be blank:

~~~
[abc1@login01(aber) ~]$ cat hostname.err.373464
~~~
{: .bash}

~~~
~~~
{: .output}


### Over-riding the sbatch options from the command line

As well as specifying options to sbatch in the batch file, they can specified on the command line too.
Lets edit our batch file to run the command `/bin/sleep 70` before `/bin/hostname`, this will cause it to wait for 70 seconds before exiting. As our job has a one minute limit this should fail and the hostname output will never happen.


~~~
[abc1@login01(aber) ~]$ nano batchjob.sh
~~~
{: .bash}


Edit the script to have the command `/bin/sleep 70` before the `hostname` command.
~~~
#!/bin/bash --login
###
# job name
#SBATCH --job-name=hostname
# job stdout file
#SBATCH --output=hostname.out.%J
# job stderr file
#SBATCH --error=hostname.err.%J
# maximum job time in D-HH:MM
#SBATCH --time=0-00:01
# maximum memory of 10 megabytes
#SBATCH --mem-per-cpu=10
# run a single task, using a single CPU core
#SBATCH --ntasks=1
# specify the reservation we have for the training workshop
# remove this for your own work
# replace XXXX and YY with the code provided by your instructor
#SBATCH --reservation=XXXX
# Specify the intel partition
#SBATCH --partition=intel
###

/bin/sleep 70
/bin/hostname
~~~
{: .bash}


Now lets resubmit the job.

~~~
[abc1@login01(aber) ~]$  sbatch batchjob.sh
~~~
{: .bash}

~~~
Submitted batch job 3739465
~~~
{: .output}

After approximately one minute the job will disappear from the `squeue` output, but this time the `.out` file should be empty and the `.err` file will contain an error message saying the job was cancelled:

~~~
[abc1@login01(aber) ~]$  cat hostname.err.3739465
~~~
{: .bash}


~~~
slurmstepd: error: *** JOB 3739465 ON node003 CANCELLED AT 2017-12-06T16:45:38 DUE TO TIME LIMIT ***
~~~
{: .output}

~~~
[abc1@login01(aber) ~]$ cat hostname.out.3739465
~~~
{: .bash}


~~~
~~~
{: .output}



Now lets override the time limit by giving the parameter `--time 0-0:2` to sbatch, this will set the time limit to two minutes and the job should complete.

~~~
[abc1@login01(aber) ~]$ sbatch --time 0-0:2 batchjob.sh
~~~
{: .bash}

~~~
 Submitted batch job 3739466
~~~
{: .output}

After approximately 70 seconds the job will disappear from the squeue list and this we should have nothing in the `.err` file and a hostname in the `.out` file.

~~~
[abc1@login01(aber) ~]$ cat hostname.err.3739466
~~~
{: .bash}

~~~
~~~
{: .output}


~~~
[abc1@login01(aber) ~]$ cat hostname.out.3739466
~~~
{: .bash}

~~~
node003
~~~
{: .output}


### Cancelling jobs

The `scancel` command can be used to cancel a job after its submitted. Lets go ahead and resubmit the job we just used.

~~~
[abc1@login01(aber) ~]$  sbatch batchjob.sh
~~~
{: .bash}

~~~
Submitted batch job 3739467
~~~
{: .output}


Now (within 60 seconds) lets cancel the job.


~~~
[abc1@login01(aber) ~]$  scancel 3739467
~~~
{: .bash}

This will cancel the job, `squeue` will now show no record of it and there won't be a `.out` or `.err` file for it.


### Listing jobs that have run

The `sacct` command lists all the jobs you have run. By default this shows the Job ID, the Job Name, partition, Account, number of CPUs used, the state of the job and how long it ran for.

~~~
[abc1@login01(aber) ~]$  sacct
~~~
{: .bash}


~~~
       JobID    JobName  Partition    Account  AllocCPUS      State ExitCode
------------ ---------- ---------- ---------- ---------- ---------- --------
21713              bash    compute                     1  COMPLETED      0:0
21713.extern     extern                                1  COMPLETED      0:0
21713.0            bash                                1  COMPLETED      0:0
21714              bash    compute                     1  COMPLETED      0:0
21714.extern     extern                                1  COMPLETED      0:0
21714.0            bash                                1  COMPLETED      0:0
21716          hostname    compute                     1  COMPLETED      0:0
21716.batch       batch                                1  COMPLETED      0:0
21716.extern     extern                                1  COMPLETED      0:0
~~~
{: .output}


> ## Using the `sbatch` command.
>
> If you haven't done so already:
>
> 1. Write a submission script to run the hostname command on one
>    node, with one core using one megabyte of RAM and a maximum run
>    time of one minute. Have it save its output to `hostname.out.%J`
>    and errors to `hostname.err.%J`.
> 2. Run your script using `sbatch`
> 3. Examine the output file, which host did it run on?
> 4. Try running it again, did your command run on the same host?
> 5. Now add the command `/bin/sleep 70` before the line running
>    hostname in the script. Run the job again and examine the output
>    of `squeue` as it runs. How many seconds does the job run for
>    before it ends? Hint: the command `watch -n 1 squeue` will run
>    squeue every second and show you the output. Press CTRL+C to stop
>    it.
> 6. What is in the `.err` file, why did you script exit? Hint: if it
>    wasn't due to the time expiring try altering another parameter so
>    it is due a time expiration.
{: .challenge}

## Running multiple copies of a job with `srun`

So far we've only run a single copy of a program. Often we'll need to run multiple copies of something. To do this we can combine the `sbatch` and `srun` commands. Instead of just placing the command at the end of the script we'll `srun` the command.
This will allow multiple copies of the command to run. In the example below two copies of the hostname command are run on two different nodes.

~~~
#!/bin/bash --login
###
# job name
#SBATCH --job-name=hostname
# job stdout file
#SBATCH --output=hostname.out.%J
# job stderr file
#SBATCH --error=hostname.err.%J
# maximum job time in D-HH:MM
#SBATCH --time=0-00:01
# maximum memory of 10 megabytes
#SBATCH --mem-per-cpu=10
# run a two tasks
#SBATCH --ntasks=2
# run the tasks across two nodes; i.e. one per node
#SBATCH --nodes=2
# specify the reservation we have for the training workshop
# remove this for your own work
# replace XX with the code provided by your instructor
#SBATCH --reservation=XXXX
# Specify the intel partition
#SBATCH --partition=intel
###

srun /bin/hostname
~~~
{: .bash}

Save this as `batchjob_parallel.sh` and run it with `sbatch`

~~~
[abc1@login01(aber) ~]$ sbatch batchjob_parallel.sh
~~~
{: .bash}

The output will now go into `hostname.out.jobnumber` and should contain two different hostnames.


## Job Arrays

Job Arrays are another method for running multiple copies of the same job. The `--array` parameter to sbatch allows us to make use of this feature.

~~~
[abc1@login01(aber) ~]$ sbatch --array=0-2 batchjob.sh
~~~
{: .bash}

The above command will submit **three** copies of the batchjob.sh command.

~~~
[abc1@login01(aber) ~]$ squeue --user=abc1
             JOBID PARTITION     NAME     USER   ST       TIME  NODES NODELIST(REASON)
         3739590_0   compute hostname abc1  R       0:01      1 node003
         3739590_1   compute hostname abc1  R       0:01      1 node003
         3739590_2   compute hostname abc1  R       0:01      1 node004
~~~
{: .bash}

Running `squeue` as this is happening will show three distinct jobs, each with an _ followed by a number on the end of their job ID. When the jobs are complete there will be three output and three err files all with the job ID and the job array number.

~~~
[abc1@login01(aber) ~]$ ls -rt | tail -6
hostname.out.3739592
hostname.out.3739591
hostname.out.3739590
hostname.err.3739590
hostname.err.3739592
hostname.err.3739591
~~~
{: .bash}

Its possible for programs to get hold of their array number from the `$SLURM_ARRAY_TASK_ID` environment variable. If we add the command `echo $SLURM_ARRAY_TASK_ID` to our batch script then it will be possible to see this in the output file.


## Choosing the proper resources for your job

When you submit a job, you are requesting resources from the scheduler to run your job. These are:
* time
* memory
* Number of cores (CPUs)
* Number of nodes
* (sort of) queue or group of machines to use

Choosing resources is like playing a game with the scheduler: You want to request enough to get your job completed without failure, But request too much: your job is "bigger" and thus harder to schedule. Request too little: if your job goes over that requested, it is killed. So you want to get it just right, and pad a little for wiggle room.

Another way to think of 'reserving' a compute node for you job is like making a reservation at a restaurant:
* if you bring more guests to your dinner, there won't be room at the restaurant, but the wait staff may try to fit them in. If so, things will be more crowded and the kitchen (and the whole restaurant) may slow down dramatically
* if you bring fewer guests and don't notify the staff in advance, the extra seats are wasted; no one else can take the empty places, and the restaurant may lose money.

"Never use a piece of software for the first time without looking to
see what command-line options are available and what default
parameters are being used" ---[Keith Bradnam, acgt.me](http://www.acgt.me/blog/2015/4/27/the-dangers-of-default-parameters-in-bioinformatics-lessons-from-bowtie-and-tophat)
	
### Time
This is determined by test runs that you do on your code during an interactive session.
Or, if you submit a batch job, over-ask first, check the amount of time actually needed,
then reduce time on later runs. 

**Please!** Due to scheduler overhead, bundle commands for minimum of 10 minutes / job

### Memory:
We recommend that you check the software docs for memory
requirements. But since these are not stated, we can take another
approach. Try a fairly low memory limit such as 3 GB and do a trial run via
`srun` or `sbatch`. If your job was killed, look at your log files or
`sacct`. If it shows a memory error, you went over. Ask for more and
try again.

Once the job has finished, ask the scheduler how much RAM was used by using the `sacct` command to get post-run job info:

~~~
sacct -j JOBID --format=JobID,JobName,ReqMem,MaxRSS,Elapsed # RAM requested/used!!
~~~
{: .bash}

The `ReqMem` field is how much you asked for and `MaxRSS` is how much was actually used. Now go back and adjust your RAM request in your sbatch command or submission script.


### Number of Cores
You can tell Slurm how many cores you expect your software to use with the `-n` or `--ntasks` arguments. **Setting this to more than one doesn't cause multiple copies of your job to run**.
This is determined by your software, how anxious you are to get the work done, and how well your code scales. **NOTE! Throwing more cores at a job does not make it run faster!** This is a common mistake and will waste compute time and prevent other users from running jobs. Ensure your software can use multiple cores: Inspect the parameters for your software and look for options such as 'threads', 'processes', 'cpus'; this will often indicate that it has been parallelized. Then run test jobs to see how well it performs with multiple cores, inching slowing from 1 to 2, 4, 8, etc, assessing the decrease in time for the job run as you increase cores. Programs often do not scale well -- it's important to understand this so you can choose the appropriate number.

### Number of Nodes
For most software, this choice is simple: 1. There are *very* few software packages capable of running across multiple nodes. If they are capable, they will probably mention the use of technology called 'MPI' or 'openMPI'. Please talk to your local Supercomputing Wales staff about how to run this. If you wish to set this use the `--nodes` or `-N` options to sbatch.

### Partitions (Queues)

Partitions, or queues, are a grouping of computers to run a certain
profile of jobs. This could be maximum run time, number of cores used,
maximum amount of RAM, etc. Earlier on we
used the `sinfo` command to list the state of the cluster, one of the
parameters this showed was the name of the partitions.

Here is the output of `sinfo` on Bert.

~~~
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
gpu          up   infinite      1   idle gpu01
intel        up   infinite      1    mix node003
intel        up   infinite      1   idle node004
amd          up   infinite      4    mix node[008-011]
highmem      up   infinite      1    mix node012
fat          up   infinite      1    mix node002
~~~
{: .output}

The partition name is listed in the first column. The intel, amd, highmem and fat nodes are
all some form of standard compute node with different amounts of RAM and different types of CPU.
Meanwhile the `gpu` queue contains a node with an NVIDIA A100 GPU.

We can specify which partition a job runs in with the `-p` or `--partition` arguments to `sbatch`. So for example the following command will run our batch job on the compute partition.

~~~
sbatch --partition=intel batchjob.sh
~~~
{: .bash}

We could also add the following line to the batch submission script.

~~~
#SBATCH --partition=intel
~~~
{:  .bash}


### Email Alerts from Slurm

You can receive email alerts when your job begins and ends by adding the following to your Slurm script. Set `--mail-type` to `END` if you just want to be alerted about jobs completing.

~~~
#SBATCH --mail-user=abc1@aber.ac.uk
#SBATCH --mail-type=ALL
~~~
{: .bash}



# Exercises

> ## Getting email output from `sbatch`
> 1. Add the following lines to your script from the previous exercise:
> `#SBATCH --mail-user=abc1@aber.ac.uk` (change to your own email address)
> `#SBATCH --mail-type=ALL`
> 2. Submit the script with the `sbatch` command. You should get an email when the job starts and finishes.
{: .challenge}


> ## Using job arrays
> 1. Add the following to the end of your job script
> `echo $SLURM_ARRAY_TASK_ID`
> 2. Submit the script with the `sbatch --array=0-1` command.
> 3. When the job completes look at the output file. What does the last line contain?
> 4. Try resubmitting with different array numbers, for example `10-11`. Be careful not to create too many jobs.
> 5. What use is it for a job to know its array number? What might it do with that information?
> 6. Try looking at the variables `$SLURM_JOB_ID` and `$SLURM_ARRAY_JOB_ID` what do these contain?
>
> > ## Solution
> > 3. The last line of the output files should contain 0 and 1
> > 4. If you set the array IDs to 10 and 11 thne the output should contain 10 and 11.
> > 5. Its useful to act as a parameter for partitioning datasets that each job will process a subpart of.
> > 6. The job ID and the parent ID of the array job. The parent ID is usually one less than ID of the first array job.
> {: .solution}
{: .challenge}

# More information about Slurm

* [Supercomputing Wales Documentation](http://portal.supercomputing.wales)
* [Harvard University's list of common Slurm commands](https://rc.fas.harvard.edu/resources/documentation/convenient-slurm-commands/)
* [For those coming from another cluster/scheduler, check out Slurm's scheduler Rosetta stone](http://slurm.schedmd.com/rosetta.pdf)

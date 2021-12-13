---
title: "Working with Modules and Installing Software"
author: "Colin Sauze, Ed Bennett"
teaching: 15
exercises: 30
questions:
 - "How do I get access to additional software?"
objectives:
 - "Understand how to load a module"
 - "Understand how to install pip packages for Python"
keypoints:
 - "A lot of software is only available by loading extra modules. This helps prevent problems where two packages are incompatible."
 - "Python 3 is one such package."
 - "If you want to install pip packages use the `--user` option to store the packages in your home directory."
---

# Using & installing software

On most cluster systems, all the software installed is not immediately available for use;
instead, it is loaded into your environment incrementally using a module system.

The `module` command controls this.
You can get a list of available software with the `module avail` command. This should return a long list of available software.

One common piece of software that isn't installed on the Supercomputing Wales hubs (without a module) is R. If we attempt to run `R` from the command line it will respond with an error:

~~~
[s.jane.doe@sl1 ~]$ R
~~~
{: .bash}

~~~
-bash: R: command not found
~~~
{: .output}

The login nodes and the compute nodes have identical
configurations in terms of what software is available, so you can
discover if your program will run from the login nodes. (The only exception
to this is if your software requires GPUs; since these are not available
on the login nodes, you cannot test GPU software there.)

From the output of the `module avail` command there should have been
an entry `R/3.6.2` in the `/apps/modules/langauges` section
near the top. 

~~~
[s.jane.doe@sl1 ~]$ module load R/3.6.2
[s.jane.doe@sl1 ~]$ R
WARNING: ignoring environment value of R_HOME

R version 3.6.2 (2019-12-12) -- "Dark and Stormy Night"
Copyright (C) 2019 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

R is free software and comes with ABSOLUTELY NO WARRANTY.
You are welcome to redistribute it under certain conditions.
Type 'license()' or 'licence()' for distribution details.

  Natural language support but running in an English locale

R is a collaborative project with many contributors.
Type 'contributors()' for more information and
'citation()' on how to cite R or R packages in publications.

Type 'demo()' for some demos, 'help()' for on-line help, or
'help.start()' for an HTML browser interface to help.
Type 'q()' to quit R.

> q()
Save workspace image? [y/n/c]: n
[s.jane.doe@sl1 ~]$
~~~
{: .bash}

> ## Legacy HPC Wales and Raven Modules
> All of the old modules which were available on HPC Wales and the old Cardiff Raven system
> are available by running either `module load hpcw` or `module load raven`. (Raven modules are only available on Hawk.)
> Please note that much of this software is outdated and may by suboptimal as it is not compiled
> to take advantage of the newer CPU architectures on Supercomputing Wales.
{: .callout}


## Installing Python modules

Python is a popular language for researchers to use and has modules
(aka libraries) that do all kinds of useful things, but sometimes the
module you need won't be installed. Many modules can be installed
using the `pip` (or `pip3` with Python 3) command. Since we don't have
administrative rights to the supercomputer, we can't install these
into the shared base environment; instead, we need to create
a local one.

We recommend using Conda for this. Conda is a package manager
that can create self-contained Python environments, and install various
versions of Python and other related dependencies into them.
Anaconda is a popular distribution of Python for scientific computing
that is based on Conda, including a large number of frequently-used
packages. Anaconda is available on Supercomputing Wales, and can then
be used to build new Conda environments.

To load Anaconda, two commands are necessary:

~~~
> module load anaconda/2021.05
> source activate
~~~
{: .language-bash}

The first of these we saw above; the second initialises Conda within
your current shell.

Since we are using Conda for the first time, it is useful to add
`conda-forge` to our list of Conda channels. This will give us access
to a wider range of pre-built Conda packages.

~~~
$ conda config --add channels conda-forge
~~~
{: .language-bash}

With this done, we can now use Conda to create
a new environment to install the packages that we want for our own work:

~~~
$ conda create -n scw_test python=3.9 mamba
~~~
{: .bash}

This tells the `conda` command to `create` a new environment, to
give it the name `scw_test`, and to install Python 3.9 and Mamba into
it. Mamba is an alternative version of Conda, that can solve the
complicated problem of getting compatible versions of all of your
requested packages simultaneously more quickly than Conda can.

Conda will take a little time to work out what it needs to install,
and once you confirm by typing `y`, then place it in a new directory
in `~/.conda/envs`.

Once your environment is created, you can activate it so you can
use it to work in with the command

~~~
$ conda activate scw_test
~~~
{: .bash}

The prefix at the start of your prompt will now change from `base`
to `scw_test`, to indicate the environment that you have active.
Similarly, `which python` now returns
`~/.conda/envs/scw_test/bin/python`, indicating that this is now
where Python will run from if you run `python`.

So far we have created a relatively bare environemnt, but we can
install packages into the new environment just as we can on our own
machines. Let's now install Matplotlib and a recent Tensorflow
version into this environment:

~~~
$ mamba install matplotlib tensorflow-gpu\>=2.5
~~~
{: .bash}

Mamba automatically works out which extra packages need to be present
for Matplotlib and Tensorflow to work, and then prompts to install them.
In the latter case, since we requested the GPU version of Tensorflow,
it automatically installs all of the requisite CUDA libraries as well.

You could alternatively have specified the packages directly to the
`conda create` command, and it would have been installed when the
environment was created. (This would use Conda's solver, though,
which would take longer to work out what needed installing.)

If you wanted to create a full Anaconda Python installation to base
your environment on, you can do this with
`conda create -n [name] anaconda`; we don't do this here because
it creates a very large number of files and takes a substantial
time to download and install. In general, it's better to only
install packages that you need, since they are less likely to
conflict with each other.

Using `pip` works very similarly to Python; provided the Anaconda
module is loaded and your Conda environment is activated, then `pip`
will automatically install into your Conda environment and not try to
install at the system level.

For more detail on using Python with Supercomputing Wales, see the
training on [High Performance
Python](https://edbennett.github.io/high-performance-python).


## How to install other software yourself

*For Perl modules and R packages*, we encourage you to set up
directories in your home and/or lab folders for installing your own
copies locally. Instructions on how to install these are available
from the [How
To](https://portal.supercomputing.wales/index.php/index/how-to-guides-archive/)
pages on the Supercomputing Wales portal.

## Requesting additional software

*If software you need is not installed*, we encourage you to do local
installs in your home or project shared directory for bleeding-edge
releases, software you are testing, or software used only by your
project. For programs that are commonly used by your domain, field,
or department, please submit a
[software install request](email:support@supercomputingwales.ac.uk).
Note that due to demand and the complex nature of software installs,
it may take a while for us to complete these requests.

Commercial software will require the appropriate licenses.


# Exercises

> ## Running a Python script
>
> 1. Create a new file using `nano` and call it `plot.py`. Give it the
>    following contents:
>    ~~~
>    import matplotlib as mpl
>    mpl.use('Agg') #set the backend to Agg to make a png file instead of displaying on screen
>    import matplotlib.pyplot as plt
>    plt.plot(range(10))
>    plt.savefig('temp.png')
>    ~~~
>    {: .python}
> 2. Create a new job submission script called `plot.sh` containing
>    the following:
>    ~~~
>    #!/bin/bash --login
>    ###
>    # job name
>    #SBATCH --job-name=plotgraph
>    # job stdout file
>    #SBATCH --output=plotgraph.out.%J
>    # job stderr file
>    #SBATCH --error=plotgraph.err.%J
>    # maximum job time in D-HH:MM
>    #SBATCH --time=0-00:01
>    # number of tasks you are requesting
>    #SBATCH --ntasks=1
>    # memory per process in MB
>    #SBATCH --mem=2
>    # number of nodes needed
>    #SBATCH --nodes=1
>    # specify our current project
>    # change this for your own work
>    #SBATCH --account=scwXXXX
>    # specify the reservation we have for the training workshop
>    # remove this for your own work
>    # replace XX with the code provided by your instructor
>    #SBATCH --reservation=scwXXXX_YY
>    ###
>    module load anaconda/2019.03
>    source activate scw_test
>    python3 plot.py
>    ~~~
>    {: .bash}
> 3. Run the job with `sbatch plot.sh`. Did the job complete
>    successfully? Are there any errors in the error file?
> 4. Fix the cause of the errors by adjusting (or removing) the appropriate parameter.
> 5. Copy back the resulting file, `temp.png` using SCP or SFTP and
>    view it on your computer.
> 6. Add the following lines to the Python script (between the
>    `plt.plot` line and the `plt.savefig` line) to make it embed the job
>    ID into the title of the image:
>    ~~~
>    import os
>    jobid = str(os.environ.get('SLURM_JOBID'))
>    plt.title(f'Job id {jobid}')
>    ~~~
>    {: .python}
>    Run the job again and look at the output image. Try using some of
>    the other Slurm environment variables from [this
>    list](https://www.glue.umd.edu/hpcc/help/slurmenv.html), too.
>
> > ## Solution
> > 1. You will get errors about the amount of memory being used. These might show up as a segmentation fault rather than a memory error. For some reason this script can be very slow to run sometimes, so increasing the timeout can help too---only do this if you are getting timeout errors. Around 50MB of memory and 5 minutes should be enough.
> > 2. Your Python code should now read:
> >
> > ~~~
> > import matplotlib as mpl
> > mpl.use('Agg') #set the backend to Agg to make a png file instead of displaying on screen
> > import os
> > import matplotlib.pyplot as plt
> > plt.plot(range(10))
> > jobid=str(os.environ.get('SLURM_JOBID'))
> > plt.title(f'Job id {jobid}')
> > plt.savefig('temp.png')
> > ~~~
> > {: .bash}
> >
> {: .solution}
{: .challenge}


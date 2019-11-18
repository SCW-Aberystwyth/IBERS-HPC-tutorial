---
title: "HPC Best Practice"
author: "Colin Sauze"
questions:
 - "What are the best practices for using an HPC system?"
objectives: 
 - "Understand HPC best practice"
---


# HPC Best Practice

* Don't run jobs on login/head nodes
* Don't run too many jobs at once. Super Computing Wales has a limit of 26 nodes/1040 cores
* Don't use all the disk space on scratch. Don't leave old files on there.
* Don't create/leave excessive numbers of files on scratch. Large file counts (100s of thousansd or millions) can cause problems for the filesystem.
* Try to use all the cores on a node, especially if you take the node exclusively. Sometimes with large memory jobs this isn't possible.
* Make jobs that last at least a few minutes, lots of small jobs creates excess load on the scheduler. Use something like GNU Parallel to make each Slurm job do several things.


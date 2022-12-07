---
title: "What next?"
author: "Colin Sauze"
questions:
 - "What are the best practices for using an HPC system?"
 - "How can I take what i've learned so far forward and put it into practice?"
objectives:
 - "Understand HPC best practice"
 - "Know what steps are needed to use Bert for research"
keypoints:
 - "Remember that HPCs are shared systems and try avoid allocating resources which you don't use"
 - "Don't make millions of files"
 - "Make use of the Research Software Engineers to help you use the system effectively"
---


## HPC Best Practice

When you start using the machines in your own research, bear the
following points in mind:

* Don't run jobs on login nodes
* Don't run too many jobs at once.
* Don't use all the disk space on scratch. Don't leave old files on there. 
* Request data you want stored long term to be transferred to the archive. You will still have read-only access to it.
* Try to use all the cores on a node, especially if you take the node exclusively. Sometimes with large memory jobs this isn't possible.
* Make jobs that last at least a few minutes, lots of small jobs creates excess load on the scheduler. Use something like GNU Parallel to make each Slurm job do several things.

Again, working on a cluster is working in a big sandbox, with people of all ages and skills. So it is
important to work carefully and be considerate. These pages from Harvard University discuss some more detail about common pitfalls and fair use on HPC systems.

[Common Pitfalls](https://rc.fas.harvard.edu/resources/documentation/common-odyssey-pitfalls/)
[Fair Use/Responsibilities:](https://rc.fas.harvard.edu/resources/responsibilities/)


## Supercomputing Wales Research Software Engineers

While this training course is aimed at giving you enough experience
and knowledge to get started, it can't cover all possible use cases.
The Research Software Engineers who have written and delivered today's
training also work with individual researchers and research groups to
advise and assist on making optimal use of the available
facilities. Things that they can provide assistance with include:

* Converting existing software to run on the HPC system
* Optimising code to run more efficiently on HPC systems
* Writing new software
* Helping with training, on-boarding and project development

If you feel you'd benefit from more bespoke support from your local
RSE team, then speak to one of them before you leave and they will let
you know the best way to proceed.

## Using Supercomputing Wales instead

Supercomputing Wales is a joint partnership of Aberystwyth, Bangor, Cardiff and Swansea Universities. 
It offers access to shared HPC facilities based in Cardiff and Swansea. These have more CPU cores and more GPUs than Bert, 
although the most memory on one node is 384GB, on Bert it is 1TB. To access Supercomputing Wales you will need to apply via 
the [My Supercomputing Wales page](https://my.supercomputing.wales).

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
* Don't run too many jobs at once. Supercomputing Wales has a limit of 26 nodes/1040 cores
* Don't use all the disk space on scratch. Don't leave old files on there.
* Don't create/leave excessive numbers of files on scratch. Large file counts (100s of thousansd or millions) can cause problems for the filesystem.
* Try to use all the cores on a node, especially if you take the node exclusively. Sometimes with large memory jobs this isn't possible.
* Make jobs that last at least a few minutes, lots of small jobs creates excess load on the scheduler. Use something like GNU Parallel to make each Slurm job do several things.



# Using Supercomputing Wales

## Project background

Supercomputing Wales replaces the previous pan-Wales HPC system known as "HPC Wales" which ran from 2010 to 2015 and provided clusters in Aberystwyth, Bangor, Cardiff, Glamorgan and Swansea. 

Supercomputing Wales (SCW) is a new project to replace HPC Wales involving Aberystwyth, Bangor, Cardiff and Swansea universities. It started in 2015 and runs until 2021. It includes new systems in Cardiff (known as Hawk) and Swansea (known as Sunbird). 

## Research Software Engineers

Each university is employing research software engineers who will work with researchers to:

* Convert existing software to run on the HPC system
* Optimise code to run more efficiently on HPC systems
* Write new software
* Help with training, on-boarding and project development

## How to get access?

Apply for an account via the "My Supercomputing Wales" webpage at [My SCW](https://my.supercomputing.wales). You can sign into this webpage using your normal university username and password. You will then be able to set or change your Supercomputing Wales password from this page.

To use the system you will have to apply for a project as well as a user account. Everyone on this course should have been added to a training project, this project is time limited. If you would like to use Supercomputing Wales for your research then you will have to apply for your own project or join an existing one.

### Project Application Process

The project form is used to assess whether Supercomputing Wales has enough resources for what you want. PhD students and RAs need to get your supervisor/PI to approve their projects. Projects are assessed by Supercomputing Wales staff who are looking for two key targets:

  * Grant income that can be attributed to Supercomputing Wales.
  * Science Outputs (e.g. journal papers)

At this stage you do NOT need to pay any money to Supercomputing Wales, simply attribute that the grant funding required access to the system. Funding which attributes other projects funded by the Welsh European Funding Office (WEFO) cannot be counted towards Supercomputing Wales. 

If you are writing a grant application and intend to use Supercomputing Wales please mention it in the grant and let us know. There are project targets to bring in approx £8 million of funding. 
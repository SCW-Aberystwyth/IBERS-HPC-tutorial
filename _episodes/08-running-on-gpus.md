---
title: "Running on GPUs"
author: "Ed Bennett"
teaching: 10
exercises: 10
questions:
 - "How do I run software that makes use of a GPU?"
objectives:
 - "Be able to submit jobs that can run on a GPU"
keypoints:
 - "Use `--partition=gpu` or `--partition=accel_ai` to submit to a partition with GPUs"
 - "Use `--gres=gpu:1` (or similar) to specify the number of GPUs you need."
---

While first designed for making graphics in video games look more
impressive, Graphics Processing Unit (GPU) accelerators have since
been found to give very high performance at numerically-intensive
computation tasks (at the expense of the flexibility offered by a
CPU). In particular, they have recently been found to perform very
well for machine learning workflows, giving orders of magnitude
more speed than the CPU that drives them.

## What's available

Supercomputing Wales provides access to NVIDIA V100 GPUs on both
the SUNBIRD and HAWK clusters. Additionally, latest-generation NVIDIA
A100 GPUs are available on SUNBIRD as part of the
[AccelerateAI][accelerateai] facility. Since these nodes are separate
from the nodes used so far for CPU computation, we need to specify a
different partition for Slurm to allocate the correct nodes.

| System  | Partition      | GPUs available per node                           | Number of Nodes | Access                                                  |
| SUNBIRD | `gpu`          | 2 x V100 16GB                                     | 4               | Swansea and Aberystwyth users                           |
| SUNBIRD | `s_gpu_eng`    | 4 x V100 32GB                                     | 1               | Swansea Engineering users\*\*                               |
| SUNBIRD | `accel_ai` *   | 8 x A100 40GB                                     | 5               | [AccelerateAI][accelerateai] users\*\*                      |
| SUNBIRD | `accel_ai_mig` | 24 x A100 10GB, 8 x A100 5GB (multi-instance GPU) | 1               | [AccelerateAI][accelerateai] users\*\*, for interactive use |
| HAWK    | `gpu`          | 2 x P100 16GB                                     | 13              | Cardiff and Bangor users                                |
| HAWK    | `gpu_v100`     | 2 x V100 16GB                                     | 15              | Cardiff and Bangor users                                |

\* In addition to the `accel_ai` partition, there is also an 
`accel_ai_dev` partition that gives access to the same nodes, but
accepts a smaller number of shorter jobs in exchange for higher
priority access. This is designed for running short tests before
starting full runs on the `accel_ai` partition.

\*\* For the AccelerateAI and `s_gpu_eng` partitions, please include
a note in your project request that you will need access to these
resources, and how you will use them. The technical team will then
ensure that you are given access.

## `sbatch` options for GPUs

In order to submit to the GPU partition, we need to add two lines to
our job scripts:

~~~
#SBATCH --partition=partition_name_goes_here
#SBATCH --gres=gpu:number_of_gpus_goes_here
~~~
{: .language-bash}

Here, replace `partition_name_goes_here` with a partition name from
the table above, and replace `number_of_gpus_goes_here` with the
number of GPUs you want to use (most frequently 1). Slurm will then
find a free GPU and ensure it is reserved for your job. Most
GPU-enabled software (including common machine learning libraries
like Tensorflow and PyTorch) will detect which GPU Slurm has assigned
and automatically use it.

To test this, let's run an example using Tensorflow.

Firstly, we need to create a new file called `tf_simple.py`, for
example using `nano`.
The following program will use Tensorflow to perform some basic
arithmetic, after checking that the GPU is available:

~~~
import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))
print(tf.test.is_built_with_cuda())
print(tf.test.gpu_device_name())
print(tf.config.get_visible_devices())

tf.debugging.set_log_device_placement(True)

# Create some tensors
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(a, "times", b, "equals", c)
~~~
{: .language-python}

Now, to submit this to run on the cluster, we can create a job script
called `submit_tf.sh`:

~~~
#!/bin/bash --login
###
# job name
#SBATCH --job-name=tensorflow_test
# job stdout file
#SBATCH --output=tensorflow_test.out.%J
# job stderr file
#SBATCH --error=tensorflow_test.err.%J
# maximum job time in D-HH:MM
#SBATCH --time=0-00:05
# specify our current project
# change this for your own work
#SBATCH --account=scwXXXX
# Specify the GPU partition
# (If the GPU partition is busy, the instructor may
# recommend a different one)
#SBATCH --partition=gpu
# Specify how many GPUs we would like to use
#SBATCH --gres=gpu:1
###

# Load Anaconda and activate our environment with Tensorflow installed
module load anaconda/2021.05
source activate scw_test

python tf_simple.py
~~~
{: .language-bash}

This can now be submitted to the queue using `sbatch`:

~~~
$ sbatch submit_tf.sh
~~~
{: .language-bash}

Once this runs, then the output will look something like the following:

~~~
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
True
/device:GPU:0
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
tf.Tensor(
[[1. 2. 3.]
 [4. 5. 6.]], shape=(2, 3), dtype=float32) times tf.Tensor(
[[1. 2.]
 [3. 4.]
 [5. 6.]], shape=(3, 2), dtype=float32) equals tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
 ~~~
{: .output}

It shows that the GPU `/device:GPU:0` is available to this job.

> ## Train a neural network
>
> Copy the file `/home/scw1389/tensorflow/test_train.py` to your home
> directory. This program is borrowed from the Tensorflow tutorial,
> and will train a small neural network to recognise handwritten digits,
> a common example problem in machine learning.
>
> Adjust the job script we wrote above to run this code on the GPU,
> and test whether it works.
{: .challenge}

[accelerateai]: https://sa2c.github.io/AccelerateAI

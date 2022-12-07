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
 - "Use `--partition=gpu` to submit to a partition with GPUs"
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

Bert provides access to an NVIDIA A100 GPU. Since this node is separate
from the nodes used so far for CPU computation, we need to specify the gpu
partition for Slurm to allocate the correct nodes.


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
# Specify the GPU partition
#SBATCH --partition=gpu
# Specify how many GPUs we would like to use
#SBATCH --gres=gpu:1
###

# Load Anaconda and activate our environment with Tensorflow installed
module load anaconda3/2020.02
source activate workshop

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
> Copy the file `/ibers/repository/public/courses/tensorflow/test_train.py` to your home
> directory. This program is borrowed from the Tensorflow tutorial,
> and will train a small neural network to recognise handwritten digits,
> a common example problem in machine learning.
>
> Adjust the job script we wrote above to run this code on the GPU,
> and test whether it works.
{: .challenge}

[accelerateai]: https://sa2c.github.io/AccelerateAI

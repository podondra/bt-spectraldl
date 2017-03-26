# Deep Learning in Large Astronomical Archives - Notebooks

This directory contains all code used in this bachelor thesis.
Here are also some information about infrastructure.

## GPGPU

Antares has GPGPU which is great for neural networks training and evaluation.
The GPGPU is
[GeForce GTX 980](http://www.geforce.com/hardware/desktop-gpus/geforce-gtx-980).

### Installation

Installation was done according to
[Tensorflow instructions](https://www.tensorflow.org/install/install_linux#nvidia_requirements_to_run_tensorflow_with_gpu_support).
Therefore, there is CUDA Toolkit 8.0 and cuDNN v5.1 installed.

Before installation I removed previous version.
Then, I have used
[Runfile for Ubuntu](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#runfile).
Finnaly, I copied cuDNN as described
[here](https://www.tensorflow.org/versions/r0.10/get_started/os_setup).

### Usage

Only environment variable need to be set.
Run `source setup-cuda.sh`.
See the script for more details.

### Tips

Use this command to enable ssh forwarding to use Jupyter notebook
(to make Jupyter available add `c.NotebookApp.ip = '*'` to configuration
file) and Tensorboard:

    ssh -A -L 8888:antares:8888 -L 6006:antares:6006 vocloud-dev.asu.cas.cz

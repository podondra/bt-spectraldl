# Deep Learning in Large Astronomical Archives

Here are Jupyter notebooks with experiments from bachelor thesis.
The notebooks goes throug the whole process from data retrieval to evaluation.
For dependencies see `requirements.txt`.
Thesis contains more text.
On contrary some parts are not mentioned there.

All code is in **Python 3**.4,
[**HDF5**](https://support.hdfgroup.org/HDF5/) stores
all intermediate representation,
[**TensorFlow**](https://www.tensorflow.org/) is the deep learning framework
of choice
and [**scikit learn**](http://scikit-learn.org/) support the whole work.
To start working with these notebooks create virtual enviroment
and install requirements:

    python3 -m venv venv    # or virtualenv -p python3 venv
    pip install -r requirements.txt

If GPU is available look at `setup-cude.sh` to see which environment variables
you need to setup. **CUDA** and [**cuDNN**](https://developer.nvidia.com/cudnn)
are required to run NVIDIA GPU card.

## Docker

*Any file created in docker container is going to be owned by root!*

To be as reproducible as posible a `Dockerfile` is provided.
Build an image with (like to use 'spectraldl' as image name):

    nvidia-docker build -t <image-name> .    # or $ make docker

Run the container:

    nvidia-docker run -d \  # deamonize the container
        -p 8888:8888 \  # port for jupyter notebook
        -p 6006:6006 \  # port for tensorboard
        -v <path-to-notebooks-directory>:/notebooks \   # volume with notebooks
        -name <container-name> \ # name the container
        <image-name>

Find the url with authentication token of Jupyter Notebook:

    docker logs <container-name>

## GPU on Antares

Antares is server of Astronomical Institute of ASCR.
It has GPU
[GeForce GTX 980](http://www.geforce.com/hardware/desktop-gpus/geforce-gtx-980).
To setup environment for working with it run:

    # setup environment for working with CUDA
    export LD_LIBRARY_PATH=export CUDA_HOME=/usr/local/cuda
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64

CUDA Toolkit 8.0 and cuDNN v5.1 installation was done according to
[Tensorflow instructions](https://www.tensorflow.org/install/install_linux#nvidia_requirements_to_run_tensorflow_with_gpu_support).
The server has Debian Jessie install which is not officialy supported so
[Runfile](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#runfile)
for Ubuntu was used.
Installation of cuDNN has been done as described
[here](https://www.tensorflow.org/versions/r0.10/get_started/os_setup).

## Tips

Enable ssh forwarding for Jupyter notebook and Tensorboard:

    ssh -A -L 8888:antares:8888 -L 6006:antares:6006 vocloud-dev.asu.cas.cz

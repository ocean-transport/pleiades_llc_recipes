# Pleiades LLC Recipes
Examples of analysis of MITgcm LLC simulations of NASA Pleiades supercomputer using 
Pangeo tools (xarray, dask, xmitgcm).

## Outside Reading

These examples will not teach you to use Python if you are a novice.
In order to take advantage of the tools we have developed for the LLC simulations,
you must have a basic understanding of [Xarray](http://xarray.pydata.org/en/latest/),
the python library we use for analysis of multidimensional arrays.
If you have not used Xarray before, I recommend the following online lectures:
- [Xarray Fundamentals](https://rabernat.github.io/research_computing_2018/xarray.html)
- [Intermediate Xarray](https://rabernat.github.io/research_computing_2018/intermediate-xarray.html)

You will also probably need to know something about [Dask](http://dask.pydata.org),
the library we use for parallel computation. Although Dask primarily operates in the
background, it's still important to have some idea of how it works under the hood
in order to achieve good performance. You should have some basic familiarity with
[dask-jobqueue](https://jobqueue.dask.org/en/latest/), which allows us to launch
Dask clusters on Pleaides.

## Setting Up Your Environment

These tools require a highly customized python environment. To set up the proper
environment, follow these steps.

### Download and install Miniconda.

From the Pleiades command line, run:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-MacOSX-x86_64.sh
conda update -y conda
# if you use a different shell, replace "bash" with your shell (e.g. "csh")
conda init bash
```

### Create a Conda environment with the necessary packages.
A suitable enviroment file is contained in this repository at
[pangeo_pleiades_environment.yaml](pangeo_pleiades_environment.yaml).
Rather than copy and paste, you can get it by cloning this repository
```
git clone https://github.com/rabernat/pleiades_llc_recipes
cd pleiades_llc_recipes
conda env create -f pangeo_pleiades_environment.yaml
```

### Clean files from home directory.
The above command created about 3.5GB of files in your home directory at `$HOME/miniconda3`.
You only have 8GB of home storage space on Pleiades, so it is wise to clean this up a bit.
```
conda clean -tipsy
rm -rf $HOME/miniconda3/pkgs/*
```
This should get the size of the environment down to about 500MB.

### Set up configuration files

Dask needs special configuration files. Install them by running
```
cp dask_config/* $HOME/.config/dask/
```

### Test the environment

There is a test script located in this repository. From the command line, run
```
source activate pangeo
py.test -v test_llcreader_pleiades.py 
```

## From the Head Node

## Batch Scripts

## Interactive Jupyter Usage

This repo contains an example job script for launching jupyterlab on a compute node
called `launch_jupyter.sh`. You need to modify it to include your GID.
Submit the script to the queue:

```
qsub launch_jupyter.sh
```

and monitor it with `qstat`. Once it runs, you will see something like.

```
$ qstat -n -u $USER
                                               Req'd    Elap
JobID          User     Queue  Jobname TSK Nds wallt S wallt Eff
-------------- -------- ------ ------- --- --- ----- - ----- ---
6846900.pbspl1 rpaberna normal jupyter  20   1 07:59 R 00:09  0%
   r435i0n8/0*20
```

The server name is `r435i0n8`. We need to create an SSH tunel to this host.
From our **local** machine, run the command

```
ssh -L 8877:r435i0n8:8877 pfe
```

and connect to your server at <http://localhost:8877>

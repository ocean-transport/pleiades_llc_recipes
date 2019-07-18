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

1. **Download and install Miniconda.** From the Pleiades command line, run:
    ```
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    sh Miniconda3-latest-MacOSX-x86_64.sh
    ```
1. **Create a Conda environment with the necessary packages.** A suitable enviroment
   file is contained in this repository at
   [pangeo_pleiades_environment.yaml](pangeo_pleiades_environment.yaml).
   Rather than copy and paste, you can get it by cloning this repository
   ```
   git clone https://github.com/rabernat/pleiades_llc_recipes
   cd pleiades_llc_recipes
   conda env create -f pangeo_pleiades_environment.yaml
   ```
1. **Set up configuration files**.

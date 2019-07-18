#!/bin/bash
#PBS -N jupyter
#PBS -l select=1:ncpus=20:model=ivy
#PBS -l walltime=7:59:00
#PBS -j oe
#PBS -m abe

export LANG="en_US.utf8"
export LANGUAGE="en_US.utf8"
export LC_ALL="en_US.utf8"

# Setup Environment
module purge
conda activate pangeo

jupyter lab --no-browser --ip=`hostname` --port=8877

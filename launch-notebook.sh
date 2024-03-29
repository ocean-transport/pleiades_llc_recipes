#!/bin/bash
#PBS -N jupyter
#PBS -l select=1:ncpus=5:model=ivy
#PBS -l walltime=1:59:00
#PBS -j oe
#PBS -m abe

export LANG="en_US.utf8"
export LANGUAGE="en_US.utf8"
export LC_ALL="en_US.utf8"

# Setup Environment
module purge
source activate pangeo

jupyter lab --no-browser --ip=`hostname` --port=8877

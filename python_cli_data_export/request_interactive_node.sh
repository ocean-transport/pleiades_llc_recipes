#!/bin/bash

qsub -I -lselect=1:ncpus=2:model=ivy,walltime=02:00:00 -q devel

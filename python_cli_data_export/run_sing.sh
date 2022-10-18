#!/bin/bash

module load singularity

singularity shell --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 --bind /nobackupp1:/nobackupp1 --bind /nobackupp17:/nobackupp17 --bind /nobackupp19:/nobackupp19 --bind /home6/dmenemen:/home6/dmenemen  /nobackup/csjone15/notebook_pangeo.sif

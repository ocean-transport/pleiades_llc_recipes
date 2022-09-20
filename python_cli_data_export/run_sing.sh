#!/bin/bash

module load singularity

singularity shell --bind /nobackup:/nobackup --bind /nobackupp1:/nobackupp1 --bind /nobackupp17:/nobackupp17 --bind /nobackupp19:/nobackupp19 --bind /home6/dmenemen:/home6/dmenemen  /nobackup/dbalwada/notebook_pangeo.sif

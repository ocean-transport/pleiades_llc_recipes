#!/bin/bash

module load singularity

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 --bind /nobackupp1:/nobackupp1 --bind /nobackupp17:/nobackupp17 --bind /nobackupp19:/nobackupp19 --bind /home6/dmenemen:/home6/dmenemen  /nobackup/csjone15/notebook_pangeo.sif /nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/extract.sh


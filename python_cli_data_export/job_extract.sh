#PBS -S /bin/csh
#PBS -N cfd
# This example uses the Sandy Bridge nodes
# User job can access ~31 GB of memory per Sandy Bridge node.
# A memory intensive job that needs more than ~1.9 GB
# per process should use less than 16 cores per node
# to allow more memory per MPI process. This example
# asks for 32 nodes and 8 MPI processes per node.
# This request implies 32x8 = 256 MPI processes for the job.
#PBS -q normal
#PBS -l select=1:ncpus=1:mpiprocs=1:model=san
#PBS -l walltime=05:00:30
#PBS -j oe
#PBS -W group_list=s2295
#PBS -m e

#s2295 is our group number

# Load a compiler you use to build your executable, for example, comp-intel/2015.0.090.

module load singularity

singularity exec --bind /nobackup:/nobackup --bind /nobackupp12:/nobackupp12 --bind /nobackupp1:/nobackupp1 --bind /nobackupp17:/nobackupp17 --bind /nobackupp19:/nobackupp19 --bind /home6/dmenemen:/home6/dmenemen  /nobackup/csjone15/notebook_pangeo.sif /nobackup/csjone15/pleiades_llc_recipes/python_cli_data_export/extract.sh


# -end of script-

#!/bin/bash
#PBS -N dask-mpi
#PBS -W group_list=g26209
#PBS -l select=2:ncpus=24:model=has
#PBS -l walltime=00:05:00
#PBS -j oe
#PBS -m abe
#PBS -q devel

# Setup Environment
module purge
source activate pangeo

# start dask cluster
dask_dir="/nobackup/rpaberna/dask_test"
scheduler_file="$dask_dir/sched.json"

rm -f $scheduler_file
mpirun --np 48 --hostfile $PBS_NODEFILE \
       dask-mpi --nthreads 1 --no-nanny --scheduler-file $scheduler_file \
       --local-directory $dask_dir  --interface ib0 &

# let the cluster start up
sleep 10

echo "******** Connecting to Scheduler from Python Client *********"

# python script to check scheduler 
read -r -d '' PYCMD <<EOF
from dask.distributed import Client
client = Client(scheduler_file='$scheduler_file')
print(client.ncores())
print("TOTAL WORKERS: ", len(client.ncores()))
EOF

python -c "$PYCMD"

# kill scheduler
kill %1

# clean up files
rm -rf "$dask_dir/*"
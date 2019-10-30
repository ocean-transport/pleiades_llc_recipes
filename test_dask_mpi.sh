#!/bin/bash
#PBS -N dask-mpi
#PBS -W group_list=g26209
#PBS -l select=2:ncpus=24:model=has
#PBS -l walltime=00:05:00
#PBS -j oe
#PBS -q devel

# Setup Environment
module purge
source activate pangeo

# hack to not use all mpi ranks on the first node
tail -n +5 $PBS_NODEFILE > TMP_NODEFILE

# start dask cluster
dask_dir="/nobackup/rpaberna/dask_test"
scheduler_file="$dask_dir/sched.json"

rm -f $scheduler_file

# for some reason, need the full path to mpirun
MPICMD=`which mpirun`

$MPICMD --hostfile TMP_NODEFILE -x PATH \
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
rm TMP_NODEFILE

#!/bin/bash

for i in {152..1752}
do
ts=$((390528+144*$i))

ITER="$ts"


python extract_llc.py --iter ["$ITER"] --out_dir './sub-output/'
#python extract_llc.py --iter ["$ITER"] --variables='["U","V"]' --out_dir './sub-output/'
#python extract_llc.py --iter ["$ITER"] --variables='["PhiBot"]' --out_dir './sub-output/'
#python extract_llc.py --iter ["$ITER"] --variables='["Theta"]' --out_dir './sub-output/' 
#python extract_llc.py --iter ["$ITER"] --variables='["Salt"]' --out_dir './sub-output/'
#python extract_llc.py --iter ["$ITER"] --fdepth='y' --variables='["Salt"]' --out_dir './ts_output/'

done

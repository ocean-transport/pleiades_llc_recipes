#!/bin/bash

for i in {0..5}
do
ts=$((390528+144*$i))

ITER="$ts"


python extract_llc.py --iter ["$ITER"]

done

#!/bin/bash

# Usage: prog local_file s3_target_prefix [s3_end_point]
local_source_file=$1
lfn=`basename ${local_source_file}`
s3_target_key_pref=$2
end_point=${3:-"mghp.osn.xsede.org"}


echo "Transferring \"${local_source_file}\" to \""s3://"${end_point}"/"${s3_target_key_pref}"/"${lfn}\"."
CURDIR=`pwd`

AKEY=${AKEY:-SET_ACCESS_KEY}
SKEY=${SKEY:-SET_SECRET_KEY}

SFILE=`mktemp ${CURDIR}/foo.XXXXXXX`
TSUFF=${SFILE#*.}

TFILE=${s3_target_key_pref}"/"${lfn}"."${TSUFF}

RCLOC="~cnhill1/bin/rclone "
# RCOPTS=" --progress --s3-no-check-bucket --multi-thread-streams 24 --s3-upload-concurrency 12 --s3-chunk-size 100M --transfers 8 --log-file=mylogfile.txt --log-level DEBUG "
RCOPTS=" --s3-no-check-bucket --multi-thread-streams 24 --s3-upload-concurrency 12 --s3-chunk-size 100M --transfers 8 --log-file=mylogfile.txt --log-level INFO "
RCTARG=" --s3-endpoint "https://"${end_point} "
RCOPER=" copyto ${local_source_file} :s3://${TFILE}"
RCMD="${RCLOC} ${RCOPTS} ${RCTARG} ${RCOPER}"

cat <<'EOF' > ${SFILE}
#!/bin/bash
EOF
echo "hostname"     >> ${SFILE}
echo "export RCLONE_S3_ACCESS_KEY_ID=${AKEY} "     >> ${SFILE}
echo "export RCLONE_S3_SECRET_ACCESS_KEY=${SKEY} " >> ${SFILE}
echo "${RCMD}"      >> ${SFILE}
chmod +x ${SFILE}

ssh -n pfe "cd ${CURDIR}; ${SFILE} " &
## ssh -n pfe "cd ${CURDIR}; ${SFILE} " &
## ssh -n pfe "cd ${CURDIR}; ${SFILE} " &
## ssh -n pfe "cd ${CURDIR}; ${SFILE} " &

wait

cat ${SFILE}
\rm ${SFILE}

exit

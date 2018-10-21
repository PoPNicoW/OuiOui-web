#!/bin/bash

TSTAMP=$(date +"%d-%b-%Y-%H-%M-%S")
S3BUCKET="s3://ouioui-webapi"

cp /home/script/webapi.py /home/script/webapi_"$TSTAMP".py

aws s3 cp "/home/script/webapi_"$TSTAMP".py" $S3BUCKET





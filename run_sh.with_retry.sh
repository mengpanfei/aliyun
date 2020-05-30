#!/bin/bash

set -u

mkdir -p log

if [ $# -lt 1 ]; then
  echo "USAGE: sh $0 x.sh p*"
  exit 241
fi

#source ./init.mmsbi.env.sh

#执行脚本 和 参数
exefile=$1
shift
params=$*


#错误重试
# 0 正常结束
# 240 非正常结束，但无需重试
MAXTRY=9 
TRY=0
while [[ $TRY -le $MAXTRY ]];do
    let "TRY=$TRY+1"
    
    sh $exefile $params >> log/$exefile.log 2>&1
    retcode=$?
    
    echo "`date` | $exefile $params -> $retcode"
    
    [ $retcode -eq 0 ] && break
    [ $retcode -eq 240 ] && break # 240 不重试
    
    sleep 5m
    
done







exit 0
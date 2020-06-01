#!/bin/bash
#run at each minute ( crontab config )

set -u

curfilepath="`dirname $0`"
cd $curfilepath
mkdir -p log
mkdir -p data
mkdir -p tmp

source ./init.env.sh


#可以明确指定日期、小时和分钟，死机重启后恢复任务 死机期间遗漏的调度
if [[ $# -eq 3 ]]; then
    today=$1
    hour=$2
    minute=$3
elif [[ $# -eq 0 ]]; then
    today=`date +%Y%m%d`
    hour=`date +%H`
    minute=`date +%M`
else
    echo "usage:
    sh $0
    sh $0 20160824 17 59"
    exit 247
fi


nowtime="$today $hour:$minute:00" # 向前倒退x小时时使用
thishmachine=`hostname` 

# echo $nowtime

weekday=`date -d "$today" +%u` #星期几
day=`date -d "$today" +%d` #几号

#相对于today的前后日期
tomorrow=`date -d "1 day $today" +%Y%m%d`
yesterday=`date -d "-1 day $today" +%Y%m%d`
ago2=`date -d "-2 day $today" +%Y%m%d`
ago7=`date -d "-7 day $today" +%Y%m%d`
ago8=`date -d "-8 day $today" +%Y%m%d`
ago15=`date -d "-15 day $today" +%Y%m%d`
ago30=`date -d "-30 day $today" +%Y%m%d`
ago31=`date -d "-31 day $today" +%Y%m%d`
ago60=`date -d "-60 day $today" +%Y%m%d`
ago360=`date -d "-360 day $today" +%Y%m%d`


## 每天调度一次
[[ $hour = "16" && $minute = "59" ]] && (
x=0
#     cd baidudog && sh ../run_sh.with_retry.sh x.sh $yesterday &
)&



## 每小时调度一次
[[ $minute = "20" ]] && (
x=0
    _ds=`date -d "-1 hour $nowtime" +%Y%m%d`
    _hour=`date -d "-1 hour $nowtime" +%H`
     cd baidudog && $PYTHON baidudog.auto_sell_dog.py mengpanfei >> baidudog.auto_sell_dog.py.mengpanfei.log &
)&


## x小时调度一次
[[ ($hour = "04" || $hour = "10" || $hour = "16" || $hour = "22") && $minute = "20" ]] && (
x=0
    _ds=`date -d "-1 hour $nowtime" +%Y%m%d`
    _hour=`date -d "-1 hour $nowtime" +%H`
    #  cd baidudog && $PYTHON baidudog.auto_sell_dog.py mengpanfei >> ../log/baidudog.auto_sell_dog.py.log &
)&







## 每n分钟调度一次
_m=$(expr $minute % 5) 
[[ $_m -eq 0 ]] && (
x=0
    #从lizhongwei ftp拉取topnid
#     cd soa && sh ../run_sh.with_retry.sh feed2se.topnid2db.sh &
)&


## 每1分钟调度一次
(
x=0

)&

exit 0

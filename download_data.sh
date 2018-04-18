#!/bin/bash
# ECOSUR-ERIS Project
# Author: Javier Arellano-Verdejo
# Date: april 2018

url="https://oceandata.sci.gsfc.nasa.gov/cgi/getfile"
log_file="status.log"

op=$1
case $op in
  -a|--aqua)
  data_file="aqua_db"
  ;;
  -t|--terra)
  data_file="terra_db"
  ;;
  -h|--help)
  echo "usage: $0 [-a|--aqua|-t|--terra]"
  echo "  -a or --aqua for aqua satelite"
  echo "  -t or --terra for terra satelite"
  exit 1
  ;;
  *)
  echo "invalid option"
  exit 1
esac

data=`cat $data_file`
for file_name in $data
do
  if [ -e $file_name ]
  then
    echo "$file_name file is currently updated"
  else
    echo -ne "Downloading:" $file_name " ... "
    wget -q $url/$file_name
    if [ $? -eq 0 ]
    then
      echo "[ ok ]"
    else
      echo "[ error ]"
      echo $file_name >> $log_file
    fi
  fi
done

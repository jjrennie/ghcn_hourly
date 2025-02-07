#!/bin/bash
main_directory="/store/sfcnet/datasets/ghcnh"

if [ $# -eq 1 ]
then
  INFILE=$1
elif [[ $INFILE ]]
then
  true
else
  echo "Station Infile needed (ex, stations.txt) "
  exit
fi

while read stn        
do          
  echo $stn

  dataurl='https://www.ncei.noaa.gov/oa/global-historical-climatology-network/hourly/access/by-station/GHCNh_'$stn'_por.psv'
  /usr/bin/wget $dataurl        
done < $INFILE
exit

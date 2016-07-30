#!/bin/bash

SRTFILE=$1
HOUR=60*60*1000
MIN=60*1000
SEC=1000
MINISEC=1

cat $SRTFILE | grep -v '[a-zA-Z]' | \
    grep -v '^$' | grep -v '^\d\+$' | \
    awk -F' --> |[:,]' \
        '{
t1 = $1*60*60*1000+$2*60*1000+$3*1000+$4;
t2 = $5*60*60*1000+$6*60*1000+$7*1000+$8;
t[NR] = t2
dt = t2 - t1;
if (dt <= 0)
   {print $0;}

if (NR > 0 && t[NR-1] >= t1) {
   print $0;
}
}'

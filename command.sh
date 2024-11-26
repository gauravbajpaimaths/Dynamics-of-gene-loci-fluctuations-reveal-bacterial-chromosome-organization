#!/bin/bash
#ps -A | grep lmp | awk {'print $1'} | xargs kill
filename="$(echo $1 | tr -d '.in')"
for par in  0 25 50 75 100 200 500
 
do
 mkdir ${par}_${filename}_dir
 cat $1 | sed s/mn\ equal\ 1/mn\ equal\ ${par}/ > ${par}_${filename}_dir/${filename}.in
 
 done




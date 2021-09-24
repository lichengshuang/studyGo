#!/bin/bash
for i in `cat biaoti.csv`; do 
    name=$(echo $i | awk -F, '{print $1}' | sed 's/_/ /g')
    url=$(echo $i | awk -F, '{print $2}')
    echo "## [$name]($url)" >> read.md 

done

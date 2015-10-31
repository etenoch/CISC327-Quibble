#!/bin/bash
chdir input
for i in *.txt
do
    echo "running test $i"
    python ../quibble.py curevents.txt ../outputs/$i.txt < $i.txt > ../outputs/$i.log
done

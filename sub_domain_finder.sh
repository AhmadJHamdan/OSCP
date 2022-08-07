#!/bin/bash

if [ $# -eq 0 ]
then
echo "How to use: ./subfinder.sh url"
echo "example: ./subfinder.sh www.domain.com"
else
wget $1
cat index.html | grep "https://" | cut -d ":" -f 2 | cut -d "/" -f 3 | cut -d "," -f 1 | grep -v "content"| cut -d '"' -f 1 | uniq > urls.txt

for iter in $(cat urls.txt)
do
if [[ $(/usr/bin/ping -c 1 $iter) ]]
then
echo "Ping Success for $iter"
echo $iter >> valid_sub.txt
else
echo "Ping Unsuccessful for $iter"
fi
done

for iter2 in $(cat valid_sub.txt)
do
host $iter2 | uniq >> ips.txt
done

echo "Script End ... "
fi



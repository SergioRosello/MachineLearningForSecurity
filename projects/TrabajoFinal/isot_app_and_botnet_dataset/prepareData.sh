#!/bin/bash

echo "Extracting data from pcap file to csv"
# ./extraction.sh
echo "Sanitizing dataset"
python sanitize.py merged_network_benign_traffic.csv merged_network_malign_traffic.csv
echo "Appending botnet identifier to dataset and sorting"
./identifyAndsort.sh 

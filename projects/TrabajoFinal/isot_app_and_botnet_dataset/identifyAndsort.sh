#!/bin/bash

# Add a new column, indicating if it is a botnet or not
echo "Adding y column"
awk -F"," 'BEGIN { OFS = "," } {$7="0"; print}' merged_network_benign_traffic.csv > botnet_identified_network_benign_traffic.csv
awk -F"," 'BEGIN { OFS = "," } {$7="1"; print}' merged_network_malign_traffic.csv > botnet_identified_network_malign_traffic.csv

# Replace the end of the first line with a "Botnet" label instead of a 1
sed -i '1s/0$/Botnet/' botnet_identified_network_benign_traffic.csv
sed -i '1s/1$/Botnet/' botnet_identified_network_malign_traffic.csv

# Merge both files into one 
echo "Merging files into merged_traffic.csv"
head -n 1 botnet_identified_network_malign_traffic.csv > merged_traffic.csv
tail -n +2 botnet_identified_network_benign_traffic.csv >> merged_traffic.csv
tail -n +2 botnet_identified_network_malign_traffic.csv >> merged_traffic.csv

# sort on epoch_time
echo "Sorting entries into sorted_merged_traffic.csv"
head -n 1 merged_traffic.csv > sorted_merged_traffic.csv
tail -n +2 merged_traffic.csv | sort -k 1 >> sorted_merged_traffic.csv

#!/bin/bash

# Check for the first log.
# We have to remove subsequent headers.
first=true

# Concatenate all the malign files
for file in ./botnet_data/*.pcap; do
  echo "Processing $file"
  if $first; then
    first=false
    tshark -r $file -T fields -e frame.time_epoch -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -e _ws.col.Info -E separator=, -E header=y > network_malign_traffic.csv
  else
    tshark -r $file -T fields -e frame.time_epoch -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -e _ws.col.Info -E separator=, >> network_malign_traffic.csv
  fi
done

head -n 1 network_malign_traffic.csv > merged_network_malign_traffic.csv
tail -n +2 network_malign_traffic.csv >> merged_network_malign_traffic.csv

first=true

# Concatenate all the benign files
for file in ./application_data/*.pcap; do
  echo "Processing $file"
  if $first; then
    first=false
    tshark -r $file -T fields -e frame.time_epoch -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -e _ws.col.Info -E separator=, -E header=y > network_benign_traffic.csv
  else
    tshark -r $file -T fields -e frame.time_epoch -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -e _ws.col.Info -E separator=, >> network_benign_traffic.csv
  fi
done

head -n 1 network_benign_traffic.csv > merged_network_benign_traffic.csv
tail -n +2 network_benign_traffic.csv  >> merged_network_benign_traffic.csv

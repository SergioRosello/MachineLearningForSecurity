#!/bin/bash

# Check for the first log.
# We have to remove subsequent headers.
first=true

# Concatenate all the pcap files
for file in ./*/*.pcap; do
  echo "Processing $file"
  if $first; then
    first=false
    tshark -r $file -T fields -e frame.time_epoch -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -e _ws.col.Info -E separator=, -E header=y >> network_traffic.csv
  else
    tshark -r $file -T fields -e frame.time_epoch -e ip.src -e ip.dst -e _ws.col.Protocol -e frame.len -e _ws.col.Info -E separator=, >> network_traffic.csv
  fi
done

head -n 1 network_traffic.csv > sorted_network_traffic.csv
tail -n +2 network_traffic.csv | sort -k 1 >> sorted_network_traffic.csv

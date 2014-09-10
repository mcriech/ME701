#!/bin/bash
#Initialize the current directory as $PWD
current_directory=$PWD
#find the number of files in the current directory
files=$(find $current_directory -maxdepth 1 -type f -print|wc -l)
#find the number of directories in the current directory
directories=$(find $current_directory -maxdepth 1 -type d -print|wc -l)
#Add the number of files and directories
all=$((files + directories))
#Print out the results
echo "Total number of files and subdirectories in $current_directory: $all"

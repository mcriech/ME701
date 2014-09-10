#!/bin/bash
#Takes a file as an arguement
#Moves the file to the "TRASH" folder in the home directory

trash_dir="/home/michael/TRASH"

#Check to make sure ~/TRASH exists
if [ ! -d "$trash_dir" ]; then
	mkdir ~/TRASH
fi

#Check to make sure a file was given as an arguement
if [ -n "$1" ]; then
#Check to make sure that the given file exists and can be moved	
	trash_file=$1
	if [ -e $trash_file ]; then
		echo "$trash_file has been moved to the trash ($trash_dir)"		
		mv $trash_file $trash_dir
#Print an error if the specified file does not exist or cannot be moved	
	else
		echo "File $trash_file does not exist or you do not have proper permissions to move $trash_file"
	fi
#Print an error if no file was provided
else
	echo "Must provide file as argument"
fi


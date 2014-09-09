#!/bin/bash
#Declare the varialbes for farenhite and celcius temps 
#Initalize temps as ints

declare -i tempF tempC tempK

#If the use gave a temperature as an arguement, use it
#Otherwise wait for an input
if [ $# > 0];
then
  tempF=$1
else
  read tempF
fi

#Convert the temperature from F to C
tempC=($tempF-32)/9*5

#Convert C to K
tempK=($tempC-273.15)

#Print out the temperature in F (input) and C (output)
echo "$tempF degrees F = $tempC degrees C"
echo "$tempF degrees F = $tempK degrees K"

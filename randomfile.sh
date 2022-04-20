#!/bin/bash
for i in {1..1000000}
do
	#generate string randomlyand the length is 50,then use mystr to stroage 
	mystr=$(mkpasswd -l 50)

	# redirect the variable called mystr to a file called randonfile.txt
	echo $mystr >> randomfile.txt
done

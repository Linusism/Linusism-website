#!/bin/sh
git add .

read -p "Commit message: " message
git commit -m "$message"

read -p "Push or not? [Y/n] " yorn

if (( "$yorn" = "n" )) ; then
	echo not pushed.  
else
	echo pushed. 
	git push
fi

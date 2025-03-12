#!/bin/bash

program_directory=/home/kyle/Collage/CSCI361/assembler/programs/
diff_directory=/home/kyle/Collage/CSCI361/assembler/diffTables/

assember_functions=/home/kyle/Collage/CSCI361/assembler/assembler_functions.py
assembler_output=/home/kyle/Collage/CSCI361/assembler/prog.hack

programs=($program_directory*)
real_output=($diff_directory*)

for i in ${!programs[*]};do

	python3 $assember_functions ${programs[i]}

	if !(diff $assembler_output ${real_output[i]}); then
		echo "Diff failed on ${programs[i]}"
	fi
done







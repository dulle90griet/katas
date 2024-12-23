# Write a script that reads each line of a target file, then writes the line back to stdout, but with an extra blank line following. This has the effect of double-spacing the file.

# Include all necessary code to check whether the script gets the necessary command line argument (a filename), and whether the specified file exists.

# When the script runs correctly, modify it to triple-space the target file.

# Finally, write a script to remove all blank lines from the target file, single-spacing it.

#!/usr/bin/env bash

if [[ -z "$1" ]]; then
  printf "Input error: One argument expected (filename)\n"
  exit
fi

if ! [ -s "$1" ]; then
  printf "Error: File doesn't exist or is empty\n"
  exit
fi

linecount=$(wc -l "$1" | awk '{print $1}')

if [[ $2 == "--triple" ]]; then
  reps=3
else
  reps=2
fi

breaks=$( awk 'NR==1{for(n=1;n<='"$reps"';n++)printf $0}' <<< "\n" )

for i in $(seq $linecount)
do
  out="$( awk "NR==$i{print;exit}" $1 )"
  if (( $i < $linecount )); then
    printf "$out$breaks"
  else
    printf "$out\n"
  fi
done

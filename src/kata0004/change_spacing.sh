#!/usr/bin/env bash

# Write a script that reads each line of a target file, then writes the line back to stdout, but with an extra blank line following. This has the effect of double-spacing the file.

# Include all necessary code to check whether the script gets the necessary command line argument (a filename), and whether the specified file exists.

# When the script runs correctly, modify it to triple-space the target file.

# Finally, write a script to remove all blank lines from the target file, single-spacing it.

if [[ -z "$1" ]]; then
  printf "Input error: One argument expected (filename)\n"
  exit
fi

args=("$@")
file_set=false
spacing_set=false
maintain_blanks=false
skip_next=false

for i in $( seq 0 $(( $# - 1 )) )
do
  if [[ "$skip_next" == true ]]; then
    skip_next=false
    continue
  fi

  if [[ "${args[$i]:0:1}" != "-" ]]; then
    if [[ "$file_set" != true ]]; then
      filename=${args[$i]}

      if ! [ -s "$filename" ]; then
        printf "Error: File doesn't exist or is empty\n"
        exit
      fi

      file_set=true
    fi
  elif [[ "${args[$i]}" == "--maintain-blanks" ]] || [[ "${args[$i]}" == "-m" ]]; then
    maintain_blanks=true
  elif [[ "$spacing_set" != true ]]; then
    case "${args[$i]}" in

      --single)
        spacing=1
        spacing_set=true
        ;;

      --double)
        spacing=2
        spacing_set=true
        ;;

      --triple)
        spacing=3
        spacing_set=true
        ;;

      --breaks | -b)
        num_found=false
        ((i++))
        if (( i <= $# )); then
          if [[ "${args[$i]}" =~ [0-9]+ ]]; then
            spacing="${args[$i]}"
            spacing_set=true
            num_found=true
            skip_next=true
          fi
        fi
        if [[ "$num_found" != true ]]; then
          printf "Input error: Expected a number after -b or --breaks\n"
          exit
        fi
        ;;

    esac
  fi
done

if [[ "$spacing_set" != true ]]; then
  spacing=2
fi

for i in $( seq "$spacing" )
do
  break_string="${break_string}\n"
done

# replace newlines with escaped '\n' and strip trailing '\n's from file end
file_str=$( sed -z 's/\n/\\n/g; s/..$//;' "$filename" )

# remove blank lines
if [[ "$maintain_blanks" == false ]]; then
  file_str=$( sed -r 's/\\n( *\\n)+/\\n/g' <<< "$file_str" )
fi

printf "%b" "${file_str//\\n/$break_string}\n"
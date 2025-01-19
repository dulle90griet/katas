#!/usr/bin/env bash

# Write a script that takes two arguments, a destination folder/drive and a folder/file to be transferred to that destination, and uses rsync to make the transfer. After making the transfer, append '_TO_DELETE' to the original folder/file's name (allowing for human confirmation of successful transfer prior to full deletion), and in the current directory create a symbolic link to the file/folder in its new location. For now, assume that file paths containing spaces are given within quotation marks, not using escape characters.

# When this runs successfully, update the script to take any number of folders/files for transfer to the given destination, using the syntax './sync_and_link.sh destination file1 file2 file3 [etc.]'.

# Next, update the script to work with file paths using escape characters as well.

# Right now, our symbolic link only 'replaces' the file/folder in its original directory if we've run the script from that directory. Update the script so that the symbolic link will be created in the original directory regardless of where the script is run from.

rsync -az "$2" "$1" --info=progress2 --no-i-r
mv "$2" "$2_TO_DELETE"
ln -s "$1/$2" .
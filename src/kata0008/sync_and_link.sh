#!/usr/bin/env bash

# Write a script that takes two arguments, a destination folder/drive and a folder/file to be transferred to that destination, and uses rsync to make the transfer. After making the transfer, append '_TO_DELETE' to the original folder/file's name (allowing for human confirmation of successful transfer prior to full deletion), and replace the original with a symbolic link to the new destination. For now, assume that file paths containing spaces are given within quotation marks, not using escape characters.

# When this runs successfully, update the script to take any number of folders/files for transfer to the given destination, using the syntax './sync_and_link.sh destination file1 file2 file3 [etc.]'.

# Next, update the script to work with file paths using escape characters as well.
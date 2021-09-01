#!/bin/sh

`git config --global alias.root '!pwd'`

hook_folder=`git root`/".git/hooks"
file_name="pre-commit"

cp $file_name $hook_folder/$file_name
chmod +x $hook_folder/$file_name

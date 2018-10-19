#!/bin/bash

currentbranch="$(git branch | egrep "\*" | cut -d ' ' -f2)"
if [ $currentbranch = "master" ]; then
    echo Pushear a master esta prohibido
    exit 1
fi

./test.sh || exit 1
exit 0

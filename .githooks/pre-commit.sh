#!/bin/bash

# Hook que asegura que antes de un commit nuevo
# no se haga en master

# Chequeamos que no estemos en master
currentbranch="$(git branch | egrep "\*" | cut -d ' ' -f2)"
if [ $currentbranch = "master" ]; then
    echo Commitear directamente sobre master esta prohibido
    exit 1
fi

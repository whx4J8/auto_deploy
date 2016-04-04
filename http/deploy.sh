#!/usr/bin/env bash

deppath="/opt_dev/python/auto_dep_demo"

echo "git start pull at " ${deppath}

cd ${deppath}
git pull #pull data from master

echo "git pull done at " ${deppath}

#!/usr/bin/env bash
cd http

PIDS=`ps -f | grep python`
echo "PID: $PIDS"
echo $PIDS

python CallbackHandler.py
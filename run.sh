#!/bin/bash

export FLASK_PORT="5001"
docker run --rm -d -e FLASK_PORT=$FLASK_PORT -p $FLASK_PORT:$FLASK_PORT kc_l2
export FLASK_PORT="5002"
docker run --rm -d -e FLASK_PORT=$FLASK_PORT -p $FLASK_PORT:$FLASK_PORT kc_l2
export FLASK_PORT="5003"
docker run --rm -d -e FLASK_PORT=$FLASK_PORT -p $FLASK_PORT:$FLASK_PORT kc_l2
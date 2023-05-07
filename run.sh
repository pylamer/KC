#!/bin/bash

export FLASK_PORT="5001"
docker run --name web_app_1 --rm -d -e FLASK_PORT=$FLASK_PORT -p $FLASK_PORT:$FLASK_PORT kc_l2
export FLASK_PORT="5002"
docker run --name web_app_2 --rm -d -e FLASK_PORT=$FLASK_PORT -p $FLASK_PORT:$FLASK_PORT kc_l2
export FLASK_PORT="5003"
docker run --name web_app_3 --rm -d -e FLASK_PORT=$FLASK_PORT -p $FLASK_PORT:$FLASK_PORT kc_l2
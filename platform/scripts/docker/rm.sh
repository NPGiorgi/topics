#!/bin/bash

docker ps -a | awk '{ print $1,$2 }' | grep platform:local | awk '{print $1 }' | xargs -I {} docker stop {}
docker ps -a | awk '{ print $1,$2 }' | grep platform:local | awk '{print $1 }' | xargs -I {} docker rm {}

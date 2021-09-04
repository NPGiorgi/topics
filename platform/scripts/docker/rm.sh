#!/bin/bash

echo "This will take a few seconds..."

# stop all containers for platform
docker ps -a | awk '{ print $1,$2 }' | grep platform:local | awk '{print $1 }' | xargs -I {} docker stop {}

# remove all containers for platform
docker ps -a | awk '{ print $1,$2 }' | grep platform:local | awk '{print $1 }' | xargs -I {} docker rm {}

# remove all images for platform
docker image ls | awk '{ print $1,$2,$3 }' | grep platform | awk '{print $3 }' | xargs -I {} docker image rm {}

echo "Done"

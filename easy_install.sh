#!/bin/bash

# run as root
if [[ $EUID -ne 0 ]]; then
    echo -e "\nPlease, use sudo!\n"
    exit 1
else

    echo -e "\nInstalling the prerequisites on the Linux platform\n"

    echo -e "\nInstalling docker\n"
    curl -sSL https://get.docker.com/ | sh 

    echo -e "\nadding your user to the docker group\n"
    usermod -aG docker $USER

    echo -e "\Installing docker-compose\n"
    curl -L --fail https://github.com/docker/compose/releases/download/1.25.0/run.sh -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose

    echo -e "\Cloning repo\n"
    git clone https://github.com/lobocode/twitterCollect && cd twitterCollect/docker

    echo -e "\Installing docker-compose\n"
    docker-compose up

fi
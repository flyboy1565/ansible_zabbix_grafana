#!/usr/bin/env bash

sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo systemctl restart sshd
#!/bin/bash

# Update the package index
sudo apt update

# Install dependencies to allow apt to use a repository over HTTPS
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    python3-pip

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add the Docker repository to APT sources
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Update the package index (again) after adding Docker repository
sudo apt update

# Install the latest version of Docker Engine
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Add the current user to the docker group to run Docker commands without sudo
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions to the Docker Compose binary
sudo chmod +x /usr/local/bin/docker-compose

# Create a symbolic link to allow running docker-compose from any directory
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

# Display Docker and Docker Compose versions
docker --version
docker-compose --version

sudo chown root:docker /usr/local/bin/docker-compose
sudo chmod g+s /usr/local/bin/docker-compose


touch /home/vagrant/.hushlogin
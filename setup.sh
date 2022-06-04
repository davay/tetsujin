#!/bin/bash

# Dependencies

packages=("jq" "moreutils" "python3")

for pkg in ${packages[@]}; do

	is_pkg_installed=$(dpkg-query -W --showformat='${Status}\n' ${pkg} | grep "install ok installed")
	if [ "${is_pkg_installed}" == "install ok installed" ]; then
		echo "${pkg} is installed."; else
		sudo apt install -yq ${pkg}
	fi
done

pip3 install -r requirements.txt

# Ask for user Discord Bot Token

discord_token=""
current_dir=$(pwd)

printf "\n"
echo "====================================================================================="
echo "Please input Discord Bot Token, see https://discord.com/developers/applications > Bot"
echo "====================================================================================="
printf "\n"

read -p "Token: " discord_token

# Insert token to src/resources/config.json

echo $(jq --arg token "$discord_token" '.DISCORD_TOKEN = $token' $current_dir/src/resources/config.json) | sponge $current_dir/src/resources/config.json

# Create Service File

echo "[Unit]
Description=Mokujin Tekken Discord Bot

[Service]
Type=simple
User=$USER
ExecStart=/usr/bin/python3 $current_dir/src/mokujin.py
Restart=on-failure
RestartSec=60s

[Install]
WantedBy=multi-user.target" | sudo dd of=/etc/systemd/system/mokujin.service status=none

sudo systemctl enable mokujin.service
sudo systemctl start mokujin.service

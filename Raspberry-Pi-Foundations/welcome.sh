#!/bin/bash
echo -e "\e[1;3;4;35mHello"
echo -e "\e[33mWelcome to \e[1;33m$HOSTNAME"
sleep 1
echo -e "\e[0;35mIt's \e[1;35m$(date +%A)"
echo -e "\e[31mWelcome"
echo -e "\e[32mWelcome"
echo -e "\e[33mWelcome"
echo -e "\e[34mWelcome"
echo -e "\e[35mWelcome"
echo -e "\e[36mWelcome"
echo -e "\e[37mWelcome"

for i in {0..255} ; do echo -en "\e[48;5;${i}m ${i} \e[0m" ; done ; echo







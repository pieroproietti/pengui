CODENAME=`egrep 'UBUNTU_CODENAME|VERSION_CODENAME' /etc/os-release | sort | head -1 | cut -d= -f2`
if [ -z "$CODENAME" ]
then
   CODENAME=`lsb_release -c -s`
fi
wget -O - https://nuitka.net/deb/archive.key.gpg | sudo apt-key add -
sudo apt-get install ca-certificates
sudo echo >/etc/apt/sources.list.d/nuitka.list "deb https://nuitka.net/deb/stable/$CODENAME $CODENAME main"
sudo apt-get update
sudo apt-get install nuitka

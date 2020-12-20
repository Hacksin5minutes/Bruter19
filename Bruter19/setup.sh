if [ $(id -u) -ne 0 ]; then
	echo "This script must be ran as root! / Bu arac root olarak calistirilmalidir!"
	exit 1
fi
apt install python3 -y
pip3 install clint
python3 banner/installation_banner.py
apt-get update
apt-get install chromium -y
apt-get install curl
apt install python3 -y
apt install python3-pip -y
apt-get install xterm
apt install zenity
pip3 install colored
wget https://chromedriver.storage.googleapis.com/83.0.4103.39/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
cp chromedriver path/
rm chromedriver*
pip3 install certifi
pip3 install -r requirements.txt
git clone https://github.com/SusmithKrishnan/torghost.git
bash torghost/build.sh
bash torghost/install.sh
rm *.deb

sudo apt update
sudo apt upgrade

# Python2.7 (and pip3)
sudo apt install -y python2.7 python-pip
sudo apt install -y python3-pip

# NVM
curl -o- https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
nvm --version
nvm install node
nvm install 6
nvm install 8

# echo versions
lsb_release -a ## echo ubuntu version
python --version
python3 --version
pip --version
pip3 --version
nvm ls

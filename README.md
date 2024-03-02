# Description
This tool was created as a way to self-host a password manager.
When you pay for a large-scale password manager you are putting your passwords in the hands of the company.
You don't always know what the password manager is doing with your passwords, often your passwords end up getting sold on the dark web.
But self hosting a password manager eliminates this threat.
Not to mention this manager generates super secure passwords, just try it once and you'll see what we mean.
Run all of the commands below in a linux terminal adding sudo permissions where required.
# How To Run
apt update

apt install git -y

git clone https://github.com/CreepyCrawler14/Password-Manager.git

apt install pip -y

pip install flask

cd Password-Manager

python3 password-manager.py

Then in your web browser go to http://127.0.0.1:5000

Note: In the "Password Name" field input what you want the password to be labeled as in the "my_passwords.txt" file.

# compiler
sudo yum install gcc gcc-c++ automake autoconf
# ssl
sudo yum install openssl-devel
# other dependencies
yum install zlib-devel bzip2-devel sqlite sqlite-devel
# change locales
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
# install python 3.5
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
tar xvf Python-3.5.2.tgz
./configure
make -j 10
make altinstall
# shutdown firewall
sudo service firewalld stop
# install database
sudo yum install mariadb
sudo yum install mariadb-devel
sudo yum install mariadb-server
# essential python packages
pip3 install mysqlclient
pip3 install django
pip3 install django-cors-headers
# setup mysql
sudo service mysqld start
# or
sudo systemctl start mariadb
mysql_secure_installation
# insert data
mysql -u xxx -p < backup.sql
# setup django and run
python3 ./manage.py migrate
nohup python3 ./manage.py runserver 0.0.0.0:8000 &

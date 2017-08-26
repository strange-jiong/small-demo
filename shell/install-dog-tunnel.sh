#!/bin/bash
echo "===============install go======="

#!/bin/bash
apt-get install software-properties-common
apt-get install python-software-properties
add-apt-repository ppa:gophers/go
apt-get install golang-go git-core mercurial

echo "===============create GOPATH=============="
echo "export GOPATH=/opt/go" >> ~/.bashrc
source ~/.bashrc
mkdir /opt/go
chmod 777 /opt/go
cd /opt/go

mkdir bin pkg src
chmod 777 bin pkg src
echo "=========install dog tunnel dependency====="
go get github.com/go-sql-driver/mysql
go get github.com/go-sql-driver/mysql
go get github.com/klauspost/reedsolomon
go get github.com/cznic/zappy
go get -u -d github.com/vzex/dog-tunnel  
cd $GOPATH/src/github.com/vzex/dog-tunnel/ 
git checkout master 
make

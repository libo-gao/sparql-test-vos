#!/bin/bash
cd /var/lib/virtuoso/db

mkdir -p dumps

cd dumps

wget http://db.uwaterloo.ca/watdiv/watdiv.10M.tar.bz2
wget http://db.uwaterloo.ca/watdiv/watdiv.100M.tar.bz2
tar xvf watdiv.10M.tar.bz2
tar xvf watdiv.100M.tar.bz2
git clone https://github.com/nosrepus/sparql-test-vos.git

virtuoso-t +wait +foreground


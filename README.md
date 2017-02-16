# love-pastel

# 서버 첫 구축시
- sudo apt-get update
- sudo apt-get install npm
- sudo apt-get install python3-pip
- npm install -g bower
- ln -s /usr/bin/nodejs /usr/bin/node

## nginx 
- sudo apt-get install nginx

## github
- sudo apt-get install git

## pip3 install 
- flask
- Flask-SQLAlchemy
- uwsgi
- xlrd
- psycopg2
- Blueprint

## DB install
- postgresql

## linux 배포시
- 참고 : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04
- sudo apt-get install libpq-dev(psycopg2 dependency)
- sudo apt-get install postgresql postgresql-contrib

# uwsgi로 실행
- uwsgi --ini love-pastel.ini
FROM ubuntu:12.04
MAINTAINER rvddool

# Install Postgres operational database
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y install wget
RUN wget --quiet --no-check-certificate -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >> /etc/apt/sources.list
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install postgresql-9.3 postgresql-contrib-9.3 postgresql-9.3-postgis-2.1 postgis
#RUN echo "host    all             all             0.0.0.0/0               md5" >> /etc/postgresql/9.3/main/pg_hba.conf
#RUN service postgresql start && /bin/su postgres -c "createuser -d -s -r -l docker" && /bin/su postgres -c "psql postgres -c \"ALTER USER docker WITH ENCRYPTED PASSWORD 'docker'\"" && service postgresql stop
RUN echo "listen_addresses = '*'" >> /etc/postgresql/9.3/main/postgresql.conf
RUN echo "port = 5432" >> /etc/postgresql/9.3/main/postgresql.conf

# Install Redis key-value database
RUN apt-get -y install redis-server

# Install Zato 
RUN apt-get -y install curl rsync bzip2 sudo
RUN mkdir /opt/zato-bin
RUN cd /opt/zato-bin && curl -O https://zato.io/download/zato-1.1.tar.bz2 && tar -xjf zato-1.1.tar.bz2 && cd zato-1.1 && curl -O https://zato.io/hotfixes/hotfixman.sh && bash hotfixman.sh 
RUN sed -i s/"apt-get install"/"apt-get install -y"/g /opt/zato-bin/zato-1.1/_install-deb.sh # add -y option to apt-get command to skip confirmation
RUN cd /opt/zato-bin/zato-1.1 && ./install.sh

# Create a zato quickstart cluster
RUN /opt/zato-bin/zato-1.1/bin/zato quickstart create /opt/zato/qs postgresql localhost 5432 zato1 zato1 localhost 6379 --verbose

# Expose ports for load-balancer, server1, server2 and web-admin
EXPOSE 11223 17010 17011 8183

# Startup script for running the docker image
ADD start.sh /opt/start.sh
RUN chmod 0755 /opt/start.sh
CMD ["/opt/start.sh"]


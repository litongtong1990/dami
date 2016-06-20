FROM centos:latest
RUN yum -y install wget gcc g++ gcc-c++ openssl-devel openssl libuuid-devel cmake vim
RUN cd /opt; wget https://github.com/warmcat/libwebsockets/archive/v1.3-chrome37-firefox30.tar.gz;tar zxvf v1.3-chrome37-firefox30.tar.gz;cd libwebsockets-1.3-chrome37-firefox30;mkdir build; cd build;cmake .. -DLIB_SUFFIX=64;make install
ADD mosquitto.conf /etc/mosquitto/
ADD lib64c.conf /etc/ld.so.conf.d/
ADD mosquitto-1.4.8 /opt/mosquitto-1.4.8
RUN ldconfig
RUN useradd mosquitto
RUN cd /opt/mosquitto-1.4.8;make binary;make install
EXPOSE 1883 10001
ENTRYPOINT ["mosquitto", "-v","-c","/etc/mosquitto/mosquitto.conf"]

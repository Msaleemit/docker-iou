FROM ubuntu:14.04

ENV DEBIAN_FRONTEND noninteractive  

RUN dpkg --add-architecture i386

RUN echo "deb http://ppa.launchpad.net/gns3/ppa/ubuntu trusty main" >> /etc/apt/sources.list
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 9A2FD067A2E3EF7B

RUN apt-get update


RUN apt-get install iouyap

RUN apt-get install -y lib32z1
RUN apt-get install -y libssl1.0.0
RUN apt-get install -y 'libssl1.0.0:i386'
RUN ln -s /lib/i386-linux-gnu/libcrypto.so.1.0.0 /lib/i386-linux-gnu/libcrypto.so.4


ENV IOURC /images/iourc.txt
ENV HOSTNAME gns3vm

RUN mkdir /images

ADD NETMAP . 
ADD iouyap.ini .


ADD iourc.txt /images
ADD iou.bin /images
RUN chmod 700 /images/iou.bin

ADD boot.sh .
CMD /bin/bash ./boot.sh

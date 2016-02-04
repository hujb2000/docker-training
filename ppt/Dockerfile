FROM node
MAINTAINER hujiabao
RUN mkdir -p /usr/src/app
COPY . /usr/src/app
ENV  VERSION 1.0.0
RUN npm install
WORKDIR /usr/src/app/netease/bin
USER node
EXPOSE 80
ONBUILD echo 'I lurking in the parent image'
ENTRYPOINT ["./start.sh"]

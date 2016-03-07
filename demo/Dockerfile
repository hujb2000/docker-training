FROM node:5.5.0-wheezy

MAINTAINER hujb

RUN mkdir -p /usr/src/app

COPY package.json /usr/src/app

WORKDIR /usr/src/app

RUN npm install

COPY . /usr/src/app


CMD ["node","timer_schedule.js"]


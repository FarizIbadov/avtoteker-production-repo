FROM node:12.20.1-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

WORKDIR /app

COPY . .

RUN npm ci --only=production


CMD ["npm","start"]
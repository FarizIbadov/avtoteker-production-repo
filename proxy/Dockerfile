FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./ssl /etc/ssl

USER root

RUN mkdir -p /vol/static
RUN chmod -R 755 /vol/static

USER nginx 

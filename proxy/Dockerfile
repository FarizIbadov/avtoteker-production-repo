FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN  mkdir -p /vol/
# RUN  mkdir -p /vol/static
# RUN  mkdir -p /vol/media

RUN  chmod -R 755 /vol/
# RUN  chmod 755 /vol/


USER nginx 
FROM python:3.8.5-slim-buster

RUN apt-get update && apt-get install gcc -y
ENV PATH="/scripts:${PATH}"

WORKDIR /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*

COPY /requirements.txt .
RUN pip install -r requirements.txt

COPY /backend .

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static


RUN useradd -ms /bin/bash user

RUN chown -R user:user ./locale

RUN chown -R 777 ./locale/en/LC_MESSAGES/django.mo
RUN chown -R 777 ./locale/en/LC_MESSAGES/django.po

RUN chown -R 777 ./locale/ru/LC_MESSAGES/django.mo
RUN chown -R 777 ./locale/ru/LC_MESSAGES/django.po

RUN chown -R 777 ./locale/tr/LC_MESSAGES/django.mo
RUN chown -R 777 ./locale/tr/LC_MESSAGES/django.po

RUN chown -R 777 ./locale/az/LC_MESSAGES/django.mo
RUN chown -R 777 ./locale/az/LC_MESSAGES/django.po


RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user


CMD ["entrypoint.sh"]
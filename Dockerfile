FROM python:3

RUN mkdir /flutter_server

WORKDIR /flutter_server

ADD . /flutter_server

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python manage.py runserver 0:8080
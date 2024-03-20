FROM python:3.8

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY ./requirements.txt ./
RUN pip install psycopg2
RUN pip install flask
RUN pip install -U flask-cors
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install flask_sqlalchemy
RUN pip install python-dotenv



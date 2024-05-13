FROM python:3.11.4-alpine3.18

RUN mkdir /app
COPY . /app

WORKDIR /app

#RUN apt-get update && apt-get upgrade && apt-get install -y curl

RUN pip install -U pip

RUN pip install -r requirements.txt

RUN mkdir /tmp/ansible
RUN chmod 777

CMD ["litestar", "run", "--reload", "--host", "0.0.0.0"]
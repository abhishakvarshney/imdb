FROM python:3.7.4-alpine

WORKDIR /usr/src/app

RUN apk add g++
RUN apk add mariadb-dev libgcc


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD 'ls'
CMD ["python" , "-u" , "manage.py", "runserver", "0:8000"]
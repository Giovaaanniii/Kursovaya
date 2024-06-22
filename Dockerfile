FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip uninstall -r requirements.txt -y
RUN pip install -r requirements.txt

COPY . /usr/src/app/

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
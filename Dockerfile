FROM python:3.9-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install Pillow
RUN pip install django-debug-toolbar
RUN pip install djangorestframework-filters
RUN pip install django-filter --upgrade
RUN pip install pylint
RUN pip install pylint-django
RUN pip install -U drf-yasg
RUN pip install black
COPY . /usr/src/app/

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
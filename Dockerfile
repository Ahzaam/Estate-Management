FROM python:3.7-alpine
ENV PYTHONNUNBUFFER 1

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:80

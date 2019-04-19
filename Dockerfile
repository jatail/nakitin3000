FROM python:3.6

RUN mkdir /nakitin
WORKDIR /nakitin
ADD . /nakitin
COPY requirements.txt /nakitin/
RUN pip install -r requirements.txt
COPY . /nakitin/

#RUN python manage.py
#RUN python manage.py makemigrations
#RUN python manage.py migrate
#RUN python manage.py runserver 0.0.0.0:8000
#RUN python manage.py createsuperuser --username admin --email admin@localhost

#RUN python bootstrap_helper.py

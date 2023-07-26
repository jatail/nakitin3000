FROM python:3.11-bookworm

RUN mkdir /nakitin
WORKDIR /nakitin
ADD . /nakitin
COPY requirements.txt /nakitin/
RUN pip install -r requirements.txt
COPY . /nakitin/

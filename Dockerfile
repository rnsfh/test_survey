FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /oprosnik
WORKDIR /oprosnik
COPY requirements.txt /oprosnik/
RUN pip install -r requirements.txt
COPY . /oprosnik/
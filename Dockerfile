FROM python:3.11-alpine
ENV PYTHONDONTWRITEBYTECODE 1
# for setting python output directly to the terminal with out buffering
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY . /code/


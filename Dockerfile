FROM python:3.11

RUN mkdir /bewise_app

WORKDIR /bewise_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .



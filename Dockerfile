FROM python:3.6-alpine

RUN apk add --no-cache curl python pkgconfig python-dev openssl-dev libffi-dev musl-dev

ADD ./requirements.txt /opt/webapp-resource/

WORKDIR /opt/webapp-resource

RUN pip install -r requirements.txt

ADD . /opt/webapp-resource

EXPOSE 8080

ENTRYPOINT ["python", "app.py"]

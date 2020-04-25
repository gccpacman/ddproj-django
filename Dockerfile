FROM python:3.7-alpine

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories 
RUN apk add --update mysql-dev build-base jpeg-dev zlib-dev libjpeg

WORKDIR /app

ADD requirements.txt /app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "ddproj.wsgi"]


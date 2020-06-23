FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1


RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories
RUN apk add --update mysql-dev build-base jpeg-dev zlib-dev libjpeg curl mysql-client

RUN mkdir /root/.pip/ && \
    printf "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple\ntrusted-host = pypi.tuna.tsinghua.edu.cn" > /root/.pip/pip.conf && \
    pip3 install --no-cache --upgrade pipenv

RUN pip install pipenv --no-cache-dir

RUN set -ex && mkdir /app

WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

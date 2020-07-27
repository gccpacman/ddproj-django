FROM ubuntu:18.04

RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list \
    && sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list \
    && apt-get update
RUN apt-get install -y libmysqlclient-dev curl python3 python3-pip 
RUN apt-get install -y build-essential

ENV PYTHONUNBUFFERED=1

RUN mkdir /root/.pip/ && \
    printf "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple\ntrusted-host = pypi.tuna.tsinghua.edu.cn" > /root/.pip/pip.conf

RUN set -ex && mkdir /app

WORKDIR /app
RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8080

RUN mkdir /app/data
VOLUME [ "/app/data" ]

CMD ["gunicorn", "ddproj.wsgi", "--bind", "0.0.0.0:8080", "--workers", "4"]

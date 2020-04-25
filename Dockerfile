FROM python:3.7-alpine

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories 
RUN apk add --update mysql-dev build-base

RUN pip install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "8080"]

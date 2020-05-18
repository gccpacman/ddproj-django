FROM python:3.7-alpine

RUN sed -i "s/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g" /etc/apk/repositories 
RUN apk add --update mysql-dev build-base jpeg-dev zlib-dev libjpeg curl mysql-client

WORKDIR /app
COPY Pipfile Pipfile.lock ./

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy --ignore-pipfile \
    pip uninstall -y pipenv virtualenv-clone virtualenv

EXPOSE 8080
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

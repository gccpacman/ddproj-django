FROM python:3

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "8080"]
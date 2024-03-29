FROM python:3.9-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3", "app.py"]
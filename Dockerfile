FROM python:3.7.3-stretch

WORKDIR /usr/src/app

COPY . .

# hadolint ignore=DL3013
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD ["python", "maange.py", "runserver"]
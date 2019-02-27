FROM python:3.6
RUN mkdir -p /usr/app
WORKDIR /usr/app
COPY . . 
RUN apt-get update && apt-get install default-libmysqlclient-dev 
RUN pip install -U setuptools && pip install -r requirements.txt
EXPOSE 8000
ENV PYTHONUNBUFFERED 1
ENTRYPOINT [ "python" ]
CMD ["./manage.py","runserver"]

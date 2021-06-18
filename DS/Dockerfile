FROM ubuntu
RUN apt-get update -y && apt-get install -y python3-pip python-dev
ADD ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
CMD ["python3", "./app.py"]

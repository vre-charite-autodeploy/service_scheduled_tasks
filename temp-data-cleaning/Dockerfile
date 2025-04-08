FROM 10.32.42.225:5000/python:3.7-buster

USER root
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt --proxy="http://proxy.charite.de:8080/"

COPY temp-data-cleaning.py .

RUN chmod u+x temp-data-cleaning.py
CMD ["./temp-data-cleaning.py"]

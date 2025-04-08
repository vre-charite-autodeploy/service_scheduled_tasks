FROM 10.32.42.225:5000/python:3.7-buster

USER root

COPY workdir-cleaning.py .

RUN chmod u+x workdir-cleaning.py
CMD ["./workdir-cleaning.py"]

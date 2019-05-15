FROM python:latest
RUN apt-get -y update
RUN pip install psutil

COPY metrics.py /usr/local/share/

CMD ["metrics.py", "-cpu|mem"]

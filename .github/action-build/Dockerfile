FROM python:3.6

RUN apt update -yqq
RUN apt install git

COPY entrypoint /usr/local/bin/entrypoint
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN chmod +x /usr/local/bin/entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint"]
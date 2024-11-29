FROM python:3.10-slim

WORKDIR /TPwutang

COPY requirements.txt /TPwutang/

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y nano

COPY . /TPwutang

EXPOSE 5000

CMD ["flask", "run"]
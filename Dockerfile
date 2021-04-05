
FROM python:3.6-alpine

WORKDIR /app

ADD requirements.txt /app

run cd /app && \
	pip install -r requirements.txt


ADD Blockchain.py /app

EXPOSE 5000

CMD ["python", "Blockchain.py", "--port", "5000"]
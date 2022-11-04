FROM python:3

RUN apt-get update -y
RUN apt-get install tk -y

RUN python -m pip install requests

WORKDIR /app
COPY . .
EXPOSE 80

CMD ["app/cotacao.py"]
ENTRYPOINT ["python3"]
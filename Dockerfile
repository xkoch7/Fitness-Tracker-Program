FROM python:3.6-slim-stretch

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /src/my_package

COPY . .

CMD ["python", "./main.py"]
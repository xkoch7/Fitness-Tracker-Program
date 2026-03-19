FROM python:3.6-slim

COPY requirements.txt ./

RUN pip install -r requirements.txt

WORKDIR /src

COPY . .
#RUN ls /
CMD ["python", "my_package/main.py"]
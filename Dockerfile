FROM python:3.6-slim

COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y tk8.6

WORKDIR /app

COPY . .
#RUN ls 
CMD ["python", "src/my_package/main.py"]
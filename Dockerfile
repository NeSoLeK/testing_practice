FROM python:3.11

RUN pip install requests allure-pytest pytest Faker

COPY . /app

WORKDIR /app

RUN apt-get update && apt-get install -y nodejs npm

RUN npm install --save-dev allure-commandline

RUN npm install -g allure-commandline

RUN apt install -y default-jre

CMD ["bash", "start.sh"]
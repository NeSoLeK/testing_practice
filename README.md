# Производственная практика



## Установка и запуск (рекомендуемый способ)

```sh
git clone https://github.com/NeSoLeK/testing_practice.git
```
```sh
npm install -g json-server
```
```sh
python3 -m venv venv
source \venv\bin\activate
pip3 install -r requirements.txt
```

Запуск json-server. Порт 3000
```sh
json-server --watch db.json --port 3000
```
json-server доступен по ссылке: http://localhost:3000/
Запуск тестирования
```sh
python3 -m pytest --alluredir allure-results ./tests/tests.py
```
Отчёт
```sh
allure serve allure-results --port 9999
```
Отчёт доступен по ссылке: http://localhost:9999/


## Запуск через Docker (не рекомендуемый способ)
```sh
docker-compose up
```
> Note: Не рекомендуется в связи с большим количеством зависимостей, таких как Java, Node.js.
> Итоговый вес контейнера достигает 1.7 ГБ. И около 5 минут подкачки. 




## Tech

- [json-server](https://github.com/typicode/json-server)
- [Pytest](https://docs.pytest.org/en/7.4.x/)
- [Allure Report](https://allurereport.org/)
- [Requests](https://pypi.org/project/requests/)
- [Faker](https://faker.readthedocs.io/en/master/index.html#)
- [Logging](https://docs.python.org/3/library/logging.html)
- [json-server-docker](https://github.com/codfish/json-server-docker) - json-server, used in docker-compose









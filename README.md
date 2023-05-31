# QAA Tests portfolio

Набор автотестов на сайт http://selenium1py.pythonanywhere.com/ru/
Сделан по результатам курса https://stepik.org/course/575/syllabus

Используется selenium и pytest

# Запуск
## Через терминал:
1. Клонировать и открыть проект
```
git clone https://github.com/dekur/qaa_tests_suite.git
```
```
cd .\qaa_tests_suite\
```
2. Создать и войти в виртуальное окружение
```
pipenv —python 3.10.5
```
```
pipenv shell
```
3. Установить requirements.txt
```
pip install -r .\requirements.txt
```
4. Запустить тесты
```
pytest tests
```
## Через PyCharm:
1. Клонировать и открыть проект
2. Создать виртуальное окружение
3. Установить модули из requirements.txt
4. Убедиться, что pytest выбран как **Default test runner** в **Settings > Tools > Python Integrated Tools**
5. Запустить тесты через любую конфигурацию pytest

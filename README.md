# Набор автотестов на сайт http://selenium1py.pythonanywhere.com/ru/

Сделан по результатам курса https://stepik.org/course/575/syllabus

# Requirements
Устанавливать из requirements.txt:
selenium
pytest

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

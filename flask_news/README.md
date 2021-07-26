# News app using APIs

## Installation
1. clone repo
```shell
git clone https://github.com/zuzanakorma/python_projects.git
```
2. change to flask_news directory
```shell
cd flask_news
```
3. create virtual env
```shell
python3 -m venv venv
```
4. activate venv
```shell
source venv/bin/activate
```
5. install dependencies
```shell
pip install -r requirements.txt
```
6. this app uses free APIs from https://newsapi.org/docs/authentication, you have to configure API_KEY as env variable with value from website
```shell
echo API_KEY=7fcf44b8ba7a434390341455ea7e97d9 > .env
```
7. change SECRET_KEY in news/\_\_init__.py for better security

8. run app
```shell
export FLASK_APP=news
flask run
```

9. access application http://127.0.0.1:5000

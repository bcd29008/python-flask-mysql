[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

# Exemplo de python Flask e MySQL

Um simples exemplo de como fazer um aplicativo com [Flask](http://flask.pocoo.org/docs/1.0/tutorial/) e [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/). Em [The Flask Mega-Tutorial](https://github.com/miguelgrinberg/microblog) tem um tutorial bem completo e com soluções mais adequadas para aplicações mais complexas.

## Preparando ambiente com virtualenv

#### Python 3
```
python3 -m venv venv
```

#### Python 2.7
```
sudo easy_install virtualenv
virtualenv venv
```

### Instalando pacotes

```
source venv/bin/activate
pip install -r requirements.txt
```
### Executando

```shell
python app.py
```
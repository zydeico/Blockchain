# Blockchain

A small Blockchain build on Python for know more about this technology and their implementation.

Project based on Learn Blockchains by Building One

This project are only for study purposes

## Installation
1. Run python 3.6+
2. Install pipenv

```
$ pip install pipenv 
```
3. Install all the requirements (Flask and request install over pipenv)
```
$ pipenv install
```
4. Run the server
```
    * `$ pipenv run python Blockchain.py`
    * `$ pipenv run python Blockchain.py -p 5001`
    * '$ pipenv run python Blockchain.py --port 5002'
```
5. Do some request using postman using this endpoint
```
http://0.0.0.0:5000/mine
```

NOTE: If you have any error importing request or flask running 4th commands, you can try:
```
$ pipenv run pip install flask && pipenv run pip install request
```

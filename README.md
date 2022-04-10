# Blockchain

A small Blockchain build on Python for know more about this technology and their implementation.

Project based on Learn Blockchains by Building One

This project are only for study purposes

## Installation
1. Run python 3.6+
2. Install pipenv
3. Verify that you have pip3 installed

```
$ pip3 install pipenv 
```
3. Install all the requirements (Flask and request install over pipenv)
```
$ pipenv install
```
4. Run the server
```
    * $ pipenv run python3 Blockchain.py
    * $ pipenv run python3 Blockchain.py -p 5001
    * $ pipenv run python3 Blockchain.py --port 5002
```
5. Do some request using postman using this endpoint
```
http://0.0.0.0:5000/mine
```

NOTE: If you have any error importing request or flask running 4th commands, you can try:
```
$ pipenv run pip3 install flask && pipenv run pip3 install requests
```

## Check how it works in postman
Well, you can check the postman and see how it works.
You can do a POST request to this endpoint and see how it works.
```
$ http://192.168.1.104:5010/nodes/register?chain=1287d04faacf3231b6f7464ae68c2c63d4549c9ca27374b8d54aa6bc81e26c6b48&length=15514013
```

To check your nodes, do a GET request to this endpoint
```
$ http://192.168.1.104:5010/nodes/register?chain=1287d04faacf3231b6f7464ae68c2c63d4549c9ca27374b8d54aa6bc81e26c6b48&length=15514013
```
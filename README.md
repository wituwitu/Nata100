# Project's name

This repository contains the main project of group 9 of software engineering 

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/DCC-CC4401/2020-2-grupo9.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ cd 2020-2-grupo9
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Developers (Group 9):

- Beltrán Amenábar
- Juan Carlos Araya
- Cristian Bustos
- Diego Wistuba
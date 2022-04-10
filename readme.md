# Flask structure single app

A ready-to-work template is a blueprint for a single flash app

## Installation
- mkdir project-name
- cd project-name

* install and activate virtualenv

```bash
python3 -m venv venv 
```

or

```cmd
python -m venv venv 
```

If you are using the Windows platform

```cmd
venv\Scripts\activate.bat 
```

But if you are using linux or unix

```bash
source ./venv/bin/activate 
```

- now clone from this repo

```cmd
git clone https://github.com/sheerien/flask-structure-single-app.git
```

- rename folder from flask-structure-single-app to src
- cd src

- install all flask-project dependencies 

```bash
pip install -r requirements.txt
```
- create .env file

```cmd
touch .env
```

copy data from .env.example to .env

And write these values into the .env file

- FLASK_ENV= development 
- FLASK_APP= run.py

- run app

```cmd
flask run
```


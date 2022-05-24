# Django_Vue_app

Python 3.9.5
django 3.2

Node.js 14.17.1

MySQL 5.7




`docker-compose up -d`

## frontend
```shell
docker-compose exec frontend /bin/bash
vue create app_name
yarn serve
```
http://localhost:8080/


## backend
```shell
docker-compose exec backend /bin/bash
django-admin startproject app_name
python3 manage.py runserver 0.0.0.0:8000
```
http://localhost:8000/


## MySQL
settings.py
```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',
        'USER': 'dbadmin',
        'PASSWORD': 'dbadmin',
        'HOST': 'db',
        'PORT': '3306'
    }
}
```

## phpmyadmin
http://localhost:3000/
# Froney Backend (Python 3)

> Django backend for Froney App

## Getting Started (windows)

#### `Setup Environment and Activate`

```
git clone https://github.com/ibrahimawadhamid/froney_backend.git
cd froney_backend
pip install virtualenv
virtualenv venv
.\venv\Scripts\activate
```

#### `Install Prerequisites`

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata fixtures/users.json
```

#### `Start Server`

```
python manage.py runserver
```


## License

[MIT](https://github.com/ibrahimawadhamid/froney_backend/blob/master/LICENSE)
